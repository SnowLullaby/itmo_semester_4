import numpy as np

# Исходная выборка (Бернулли)
np.random.seed(10)
sample = np.random.binomial(1, 0.5, 30)
n = len(sample)

# Оценка параметра p через выборочное среднее (метод моментов)
p_mean = np.mean(sample)

# Исправленная (несмещённая) выборочная дисперсия
var_corrected = np.var(sample, ddof=1)

# Оценка параметра p через дисперсию (решаем квадратное уравнение)
D = var_corrected
discriminant = np.sqrt(1 - 4 * D)

p1 = (1 + discriminant) / 2
p2 = (1 - discriminant) / 2

# Вывод результатов
print(f"Оценка p (по среднему): {p_mean:.4f}")
print(f"Исправленная дисперсия: {var_corrected:.4f}")
print(f"Оценки p через дисперсию: {p1:.4f} и {p2:.4f}")