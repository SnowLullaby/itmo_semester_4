import math
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

# Исходная выборка данных
data = [0.83, 0.56, 1.58, 0.81, 0.89, 0.19, -1.77, -0.89, -3.99, -0.40, 0.48, -0.74, -3.43, -3.47, -4.55, -1.51, 1.29, -3.09, -0.76, 0.80, -4.77, 0.75, -1.13, -3.03, -3.60, -3.65, -3.67, -0.13, -3.22, -3.56, 0.75, 0.99, -1.12, -4.42, -4.60, -4.35, 0.36, -3.80, 0.18, -3.43, 0.39, -3.85, 1.84, -4.63]

# Функция для создания вариационного ряда в виде таблицы
def create_variation_series(data_in_f):
    data_counter = Counter(data_in_f)

    values = list(data_counter.keys())
    frequencies = list(data_counter.values())

    values_str = [val for val in values]
    probabilities_str = [freq for freq in frequencies]

    df = pd.DataFrame([values_str, probabilities_str])
    print(df.to_string(index=False, header=False))

    return df

# Расчет размеров бакетов и частот попадания
def group_and_count(data_for_f):
    min_value = min(data_for_f)
    max_value = max(data_for_f)
    min_value_rounded = math.floor(min_value * 10) / 10.0
    max_value_rounded = math.ceil(max_value * 10) / 10.0

    # Вычисляем количество интервалов по формуле Стерджеса
    n = len(data_for_f)
    k = math.ceil(1 + math.log2(n))
    print(f'k = {k}')
    h = (max_value_rounded - min_value_rounded) / k
    print(f'h = {h:.2f}')

    # Строим интервалы и группируем данные
    bins = [min_value_rounded + i * h for i in range(k + 1)]
    grouped_data = pd.cut(data_for_f, bins, right=False)
    frequencies = grouped_data.value_counts()
    otn_frequencies = frequencies/n
    bin_centers = [(bins[i] + bins[i + 1]) / 2 for i in range(len(bins) - 1)]

    # Создаем DataFrame для отображения
    df = pd.DataFrame({
        'Интервал': [f'[{bins[i]:.1f}, {bins[i+1]:.1f})' for i in range(k)],
        'Середина интервала': [f'{bin_centers[i]:.2f}' for i in range(k)],
        'Частота': frequencies.values,
        'Относительная частота': otn_frequencies.values
    })

    # Выводим таблицу
    print("Группированная выборка с частотами:")
    print(df.to_string(index=False))

    return bins, frequencies, min_value_rounded, max_value_rounded, bin_centers

# Печатаем ЭФР
def print_cdf(bins, frequencies, n, bin_centers):
    cumulative_frequencies = frequencies.cumsum()
    ecdf_values = cumulative_frequencies / n
    ecdf_values = np.concatenate(([0], ecdf_values))

    intervals = [f"x <= {bin_centers[0]:.2f}"]
    intervals += [f"{bin_centers[i]:.2f} < x <= {bin_centers[i + 1]:.2f}" for i in range(len(bin_centers) - 1)]
    intervals += [f"{bin_centers[-1]:.2f} < x"]

    df = pd.DataFrame({
        'Интервал': intervals,
        'ЭФР': ecdf_values
    })

    # Приводим таблицу к нужному формату
    print("Эмпирическая функция распределения:")
    print(df.to_string(index=False))


# Строим ЭФР
def plot_cdf(bins, frequencies, n, bin_centers, minimum, maximum):
    cumulative_frequencies = frequencies.cumsum()
    cdf = cumulative_frequencies / n

    ecdf_x = bin_centers
    ecdf_y = cdf

    graph = list(zip([min(ecdf_x)-1] + [i for i in ecdf_x] + [max(ecdf_x)+1],
                     [0.] + [j for j in ecdf_y] + [1.]))

    for i in range(len(graph) - 1):
        plt.plot([graph[i][0], graph[i + 1][0]], [graph[i][1], graph[i][1]], color='blue')

    for i in range(1, len(graph) - 1):
        plt.scatter(graph[i][0], graph[i][1], edgecolor='blue', facecolor='white', s=10, zorder=2)

    # Строим теоретическую ЭФР для равномерного распределения
    x_vals = np.linspace(minimum, maximum, 1000)
    uniform_cdf = (x_vals - minimum) / (maximum - minimum)
    plt.plot(x_vals, uniform_cdf, color='red', linestyle='--')

    x_vals = np.linspace(-5.1322,2.0146, 1000)
    from_5_task = (x_vals - (-5.1322)) / (2.0146 - (-5.1322))
    plt.plot(x_vals, from_5_task, color='orange', linestyle='--')

    x_vals = np.linspace(min(data),max(data), 1000)
    from_5_task = (x_vals - min(data)) / (max(data) - min(data))
    plt.plot(x_vals, from_5_task, color='green', linestyle='--')

    plt.xlabel("Значение")
    plt.ylabel("Распределение")
    plt.title("Эмпирическая функция распределения")
    plt.grid(True)
    plt.show()

# Строим гистограмму
def plot_histogram(bins, frequencies, n, min_value, max_value):
    normalized_frequencies = frequencies / n

    x_vals = np.linspace(min_value,  max_value, 1000)
    uniform_height = 1 / (max_value - min_value)
    uniform_pdf = np.ones_like(np.linspace(min_value,  max_value, 1000)) * uniform_height

    x_vals_task_5 = np.linspace(-5.1322,  2.0146, 1000)
    uniform_height_task_5 = 1 / (2.0146 - (-5.1322))
    uniform_pdf_task_5 = np.ones_like(np.linspace(min_value,  max_value, 1000)) * uniform_height_task_5

    x_vals_task_6 = np.linspace(min(data),  max(data), 1000)
    uniform_height_task_6 = 1 / (max(data) - min(data))
    uniform_pdf_task_6 = np.ones_like(np.linspace(min(data), max(data), 1000)) * uniform_height_task_6

    plt.bar(bins[:-1], normalized_frequencies, width=np.diff(bins), align='edge', edgecolor='black', alpha=0.7)
    plt.plot(x_vals, uniform_pdf, label='Равномерное распределение', color='red', linestyle='--')
    plt.plot(x_vals_task_5, uniform_pdf_task_5, label='Равномерное распределение', color='orange', linestyle='--')
    plt.plot(x_vals_task_6, uniform_pdf_task_6, label='Равномерное распределение', color='green', linestyle='--')
    plt.xlabel('Значения')
    plt.ylabel('Частота (нормированная)')
    plt.title('Нормированная гистограмма по группированным данным')
    plt.show()


# Функция для вычисления статистик
def calculate_statistics(bin_centers, frequencies, n):
    probabilities = frequencies / n

    mean = np.sum(bin_centers * probabilities)
    variance = np.sum((bin_centers - mean) ** 2 * probabilities)
    std_deviation = np.sqrt(variance)

    return mean, variance, std_deviation


# Вариационный ряд исходных чисел
df_variation_series = create_variation_series(sorted(data))

bins, frequencies, min_value_rounded, max_value_rounded, bin_centers  = group_and_count(sorted(data))
n = len(data)
print_cdf(bins, frequencies, n, bin_centers)
plot_cdf(bins, frequencies, n, bin_centers, min_value_rounded, max_value_rounded)
plot_histogram(bins, frequencies, n, min_value_rounded, max_value_rounded)

# Рассчитываем статистики
mean, variance, std_deviation = calculate_statistics(bin_centers, frequencies, n)

# Выводим результаты
print(f"Математическое ожидание: {mean:.4f}")
print(f"Дисперсия: {variance:.4f}")
print(f"Среднеквадратическое отклонение: {std_deviation:.4f}")