import numpy as np


def f(x):
    x1, x2 = x
    return x1 ** 2 + 3 * x2 ** 2 + 3 * x1 * x2 - x1 - 2 * x2 - 1


def df_dx1(x):
    x1, x2 = x
    return 2 * x1 + 3 * x2 - 1


def df_dx2(x):
    x1, x2 = x
    return 6 * x2 + 3 * x1 - 2


def gradient(x):
    return np.array([df_dx1(x), df_dx2(x)])


# Метод покоординатного спуска
def coordinate_descent(start, ep, max_iter=1000):
    x = np.array(start, dtype=float)
    history = [x.copy()]

    for _ in range(max_iter):
        x_old = x.copy()

        # Минимизация по x1
        x[0] = (1 - 3 * x[1]) / 2

        # Минимизация по x2
        x[1] = (2 - 3 * x[0]) / 6

        history.append(x.copy())

        if np.linalg.norm(x - x_old) < ep:
            break

    return np.array(history)


# Метод градиентного спуска
def gradient_descent(start, ep, max_iter=1000, alpha=0.24, decay=0.8):
    x = np.array(start, dtype=float)
    history = [x.copy()]
    current_alpha = alpha

    for _ in range(max_iter):
        x_old = x.copy()
        grad = gradient(x)

        # Делаем шаг
        x_new = x - current_alpha * grad

        # Проверяем улучшение
        if f(x_new) < f(x):
            x = x_new
            current_alpha = alpha
        else:
            current_alpha *= decay

        history.append(x.copy())

        # Проверка условия останова
        if abs(f(x_new)-f(x_old)) < ep:
            break

    return np.array(history)


# Метод наискорейшего спуска
def steepest_descent(start, ep, max_iter=1000):
    x = np.array(start, dtype=float)
    history = [x.copy()]

    for _ in range(max_iter):
        x_old = x.copy()
        grad = gradient(x)

        grad_norm = np.linalg.norm(grad)
        if grad_norm < ep:
            break

        S = -grad / grad_norm

        S1, S2 = S
        x1, x2 = x

        numerator = (2 * x1 * S1 + 6 * x2 * S2 + 3 * x1 * S2 + 3 * x2 * S1 - S1 - 2 * S2)
        denominator = (2 * S1 ** 2 + 6 * S2 ** 2 + 6 * S1 * S2)

        if abs(denominator) < 1e-10:
            break

        lam = -numerator / denominator

        x = x + lam * S
        history.append(x.copy())

    return np.array(history)


# Вывод результатов
def print_results(method_name, history):
    np.set_printoptions(suppress=True)
    print(f"\n{method_name}")
    print(f"Начальная точка: {history[0].round(4)}")
    print(f"Финальная точка: {history[-1]}")
    print(f"Значение функции: {f(history[-1]):.4f}")
    print(f"Итераций выполнено: {len(history) - 1}")
    print("+" * 30)


start_point = [3.0, 3.0]
epsilon = 0.0001

# Покоординатный спуск
cd_history = coordinate_descent(start_point, epsilon)
print_results("Метод покоординатного спуска", cd_history)

# Градиентный спуск
gd_history = gradient_descent(start_point, epsilon)
print_results("Метод градиентного спуска", gd_history)

# Наискорейший спуск
sd_history = steepest_descent(start_point, epsilon)
print_results("Метод наискорейшего спуска", sd_history)