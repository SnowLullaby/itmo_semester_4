import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(10)

theta = 0.2
epsilon = 0.2
n_values = range(100, 1001, 100)

results = []

for n in n_values:
    sample = np.random.binomial(1, theta, n)
    sample_mean = np.mean(sample)

    std_dev = np.sqrt(sample_mean*(1-sample_mean))
    z = stats.norm.ppf(1 - epsilon / 2)

    margin_of_error = z * (std_dev / np.sqrt(n))
    lower_bound = round(sample_mean - margin_of_error, 4)
    upper_bound = round(sample_mean + margin_of_error, 4)

    results.append([n, round(sample_mean, 4), lower_bound, upper_bound])


df = pd.DataFrame(results, columns=["Размер выборки (n)", "Среднее значение выборки", "Нижняя граница", "Верхняя граница"])
pd.set_option('display.max_columns', None)
print(df)

plt.figure(figsize=(8, 6))
plt.plot(df["Размер выборки (n)"], df["Нижняя граница"], label="Нижняя граница", marker='o')
plt.plot(df["Размер выборки (n)"], df["Верхняя граница"], label="Верхняя граница", marker='o')
plt.axhline(y=theta, color='r', linestyle='--', label='Тета')
plt.xlabel('Размер выборки (n)')
plt.ylabel('Границы доверительного интервала')
plt.title('Границы доверительного интервала в зависимости от размера выборки')
plt.legend()
plt.grid(True)
plt.show()
