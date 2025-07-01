import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(10)


theta = 3
epsilon = 0.15
n_values = range(100, 1001, 100)

results_dot = []
results_assimp = []

for n in n_values:
    sample = np.random.uniform(0, theta, n)
    sample_mean = np.mean(sample)
    sample_max = np.max(sample)

    z = stats.norm.ppf(1 - epsilon / 2)

    # Точечная
    lower_bound_dot = sample_max
    upper_bound_dot = sample_max / (epsilon ** (1/n))

    # Асимптотическая
    margin_of_error_normal = z / np.sqrt(3*n)
    lower_bound_assimp = 2 * sample_mean / (1 + margin_of_error_normal)
    upper_bound_assimp = 2 * sample_mean / (1 - margin_of_error_normal)

    results_dot.append([n, round(sample_max, 4), round(lower_bound_dot, 4), round(upper_bound_dot, 4)])
    results_assimp.append([n, round(sample_mean, 4), round(lower_bound_assimp, 4), round(upper_bound_assimp, 4)])

df_dot = pd.DataFrame(results_dot, columns=["Размер выборки (n)", "Значение выборки", "Нижняя граница (точечная)", "Верхняя граница (точечная)"])
df_assimp = pd.DataFrame(results_assimp, columns=["Размер выборки (n)", "Среднее значение выборки", "Нижняя граница (асимпт)", "Верхняя граница (асимпт)"])

pd.set_option('display.max_columns', None)
print("Точечные результаты:\n", df_dot)
print("\nАсимптотические результаты:\n", df_assimp)

plt.figure(figsize=(8, 6))
plt.plot(df_dot["Размер выборки (n)"], df_dot["Нижняя граница (точечная)"], label="Нижняя граница (точечная)", marker='o')
plt.plot(df_dot["Размер выборки (n)"], df_dot["Верхняя граница (точечная)"], label="Верхняя граница (точечная)", marker='o')
plt.axhline(y=theta, color='r', linestyle='--', label=f'Тета')
plt.xlabel('Размер выборки (n)')
plt.ylabel('Границы доверительного интервала')
plt.title('Точечные границы доверительного интервала')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(df_assimp["Размер выборки (n)"], df_assimp["Нижняя граница (асимпт)"], label="Нижняя граница (асимпт)", marker='o')
plt.plot(df_assimp["Размер выборки (n)"], df_assimp["Верхняя граница (асимпт)"], label="Верхняя граница (асимпт)", marker='o')
plt.axhline(y=theta, color='r', linestyle='--', label=f'Тета')
plt.xlabel('Размер выборки (n)')
plt.ylabel('Границы доверительного интервала')
plt.title('Стандартные границы доверительного интервала')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(df_dot["Размер выборки (n)"], df_dot["Нижняя граница (точечная)"], label="Нижняя граница (точечная)", marker='o')
plt.plot(df_dot["Размер выборки (n)"], df_dot["Верхняя граница (точечная)"], label="Верхняя граница (точечная)", marker='o')
plt.plot(df_assimp["Размер выборки (n)"], df_assimp["Нижняя граница (асимпт)"], label="Нижняя граница (асимпт)", marker='x')
plt.plot(df_assimp["Размер выборки (n)"], df_assimp["Верхняя граница (асимпт)"], label="Верхняя граница (асимпт)", marker='x')
plt.axhline(y=theta, color='r', linestyle='--', label=f'Тета')
plt.xlabel('Размер выборки (n)')
plt.ylabel('Границы доверительного интервала')
plt.title('Сравнение доверительных интервалов (точечный vs асимптотический)')
plt.legend()
plt.grid(True)
plt.show()

