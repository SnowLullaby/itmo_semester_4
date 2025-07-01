import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Данные выборки
sample = np.array([2.47, 2.98, 2.83, 3.86, 3.22, 2.82, 3.41, 1.96, 2.55, 2.30,
                  2.40, 2.39, 2.81, 3.44, 2.05, 2.33, 3.98, 2.56, 3.14, 2.85,
                  3.11, 2.93, 3.43, 2.38, 2.42, 2.49, 3.25, 1.19, 2.90, 3.10,
                  2.60, 2.73, 2.65, 3.52, 3.15, 3.55, 2.14, 3.01, 3.39, 3.38,
                  3.03, 1.08, 0.72, 1.26, 1.90, 2.37, 2.00, 3.29, 2.78, 3.12,
                  2.03, 2.90, 2.08, 1.85, 2.36, 2.42, 3.66, 3.33, 2.03, 3.96,
                  3.50, 2.78, 3.82, 2.34, 0.90, 3.17, 2.89, 2.27, 3.16, 1.06,
                  2.82, 3.54, 3.19, 4.05, 3.22, 2.94, 3.48, 3.17, 2.84, 2.20,
                  1.26, 2.78, 3.38, 2.15, 2.25, 1.31, 2.55, 2.13, 2.50, 2.28,
                  2.84, 1.93, 0.68, 3.64, 2.49, 2.46, 2.79, 2.61, 1.54, 2.49])

# Блок 1
sorted_sample = np.sort(sample)
a = np.floor(sorted_sample[0] * 10) / 10
b = np.ceil(sorted_sample[-1] * 10) / 10
h = (b - a) / 10

print(f"Вариационный ряд (отсортированные данные): {sorted_sample}")
print(f"Левая граница интервала a: {a}")
print(f"Правая граница интервала b: {b}")
print(f"Шаг h: {h:.2f}")

# Блок 2
intervals = np.arange(a, b + 0.001, h)
counts = np.histogram(sample, bins=intervals)[0]
frequencies = counts / len(sample)

midpoints = (intervals[:-1] + intervals[1:]) / 2
y = midpoints

m_hat = np.sum(frequencies * y)
S_squared = np.sum(frequencies * (y - m_hat)**2)
F_x = np.cumsum(frequencies)

# Гистограмма
plt.figure(figsize=(10, 6))
plt.hist(sample, bins=intervals, density=True, alpha=0.6, color='g', label='Гистограмма')

x_range = np.linspace(a, b, 10000)
normal_pdf = stats.norm.pdf(x_range, loc=m_hat, scale=np.sqrt(S_squared))

plt.plot(x_range, normal_pdf, label='Нормальное распределение', color='b', linestyle='--')
plt.title('Гистограмма и плотность вероятности')
plt.xlabel('Значения выборки')
plt.ylabel('Плотность')
plt.legend()
plt.grid(True)
plt.show()

print("Границы интервалов:", intervals)
print("Средние точки интервалов:", midpoints)
print("Частоты попадания:", frequencies)

# ЭФР
plt.figure(figsize=(10, 6))
plt.step(midpoints, F_x, label='Функция накопления частот (ЭФР)', where='post', color='purple')
plt.plot(x_range, stats.norm.cdf(x_range, loc=m_hat, scale=np.sqrt(S_squared)),
         label='Нормальное распределение (CDF)', color='b', linestyle='--')
plt.title('Функция накопления частот (ЭФР) и нормальное распределение')
plt.xlabel('Значения выборки')
plt.ylabel('Накопленная вероятность')
plt.legend()
plt.grid(True)
plt.show()

# доверительный интервал
t_critical = 1.96
CI_lower = m_hat - t_critical * np.sqrt(S_squared / len(sample))
CI_upper = m_hat + t_critical * np.sqrt(S_squared / len(sample))
print(f"Среднее (математическое ожидание): {m_hat:.4f}")
print(f"Дисперсия: {S_squared:.4f}")
print(f"СКО: {np.sqrt(S_squared):.4f}")
print(f"Доверительный интервал для математического ожидания: ({CI_lower:.4f}, {CI_upper:.4f})")

# Блок 3
left_intervals = intervals[:-1]
right_intervals = intervals[1:]

z_left = (left_intervals - m_hat) / np.sqrt(S_squared)
z_right = (right_intervals - m_hat) / np.sqrt(S_squared)

z_left[0] = -np.inf
z_right[-1] = np.inf

laplace_left = stats.norm.cdf(z_left)
laplace_right = stats.norm.cdf(z_right)

P_i = laplace_right - laplace_left
n = 100
expected_counts = n * P_i

chi_square = np.sum((counts - expected_counts) ** 2 / expected_counts)

print(f"Значения z для левых границ интервалов: {z_left}")
print(f"Значения z для правых границ интервалов: {z_right}")
print(f"Значения функции Лапласа для левых границ интервалов: {laplace_left}")
print(f"Значения функции Лапласа для правых границ интервалов: {laplace_right}")
print(f"Теоретическая вероятность попадания в каждый интервал P_i: {P_i}")
print(f"Теоретическое число попаданий в интервал: {expected_counts}")
print(f"Значение статистического критерия χ^2: {chi_square:.4f}")

chi_square_critical = 14.1
print(f"Критическая точка χ^2 для α = 0.05 и r = 7: {chi_square_critical}")

if chi_square < chi_square_critical:
    print("Гипотеза о нормальности данных принимается.")
else:
    print("Гипотеза о нормальности данных отвергается.")