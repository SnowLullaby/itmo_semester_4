import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from decimal import Decimal, getcontext

# Устанавливаем точность для Decimal
getcontext().prec = 10

def f(x):
    return (1 / 4) * x ** 4 + x ** 2 - 8 * x + 12

def f_pr(x):
    return x ** 3 + 2 * x - 8

def f_pr2(x):
    return 3 * x ** 2 + 2

# Половинное
def refined_bisection_method(a, b, eps):
    iterations = []

    a, b, eps = Decimal(a), Decimal(b), Decimal(eps)

    while (b - a) > 2 * eps:
        x1 = (a + b - eps) / 2
        x2 = (a + b + eps) / 2

        f1, f2 = f(float(x1)), f(float(x2))  # Преобразуем обратно в float для вычисления функции
        iterations.append((float(a), float(b), float(x1), float(x2), f1, f2))

        if f1 > f2:
            a = x1
        else:
            b = x2

    # Приближённый минимум
    x_min = (a + b) / 2
    f_min = f(float(x_min))

    return float(x_min), float(f_min), iterations

# Золотое
def golden_section_method(a, b, eps):
    iterations = []
    phi = Decimal((1 + np.sqrt(5)) / 2)

    a, b, eps = Decimal(a), Decimal(b), Decimal(eps)

    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f1, f2 = f(float(x1)), f(float(x2))

    while (b - a) > 2 * eps:
        iterations.append((float(a), float(b), float(x1), float(x2), f1, f2))

        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = b - (b - a) / phi
            f1 = f(float(x1))
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + (b - a) / phi
            f2 = f(float(x2))

    # Приближённый минимум
    x_min = (a + b) / 2
    f_min = f(float(x_min))
    return float(x_min), float(f_min), iterations


# Хорды
def secant_method(a, b, eps):
    iterations = []
    a, b, eps = Decimal(a), Decimal(b), Decimal(eps)

    while True:
        x_new = a - (Decimal(f_pr(float(a))) * (a - b)) / (Decimal(f_pr(float(a))) - Decimal(f_pr(float(b))))
        f_new = f_pr(float(x_new))

        if abs(f_new) < eps:
            break

        iterations.append((float(a), float(b), float(x_new), f_new))

        if f_new > 0:
            b = x_new
        else:
            a = x_new

    # Приближённый минимум
    x_min = float(x_new)
    f_min = f(float(x_min))

    return x_min, f_min, iterations

# Ньютон
def newton_method(x0, eps):
    iterations = []
    x = Decimal(x0)
    eps = Decimal(eps)

    while True:
        f1 = Decimal(f_pr(float(x)))
        f2 = Decimal(f_pr2(float(x)))

        if abs(f1) < eps:
            break

        x_new = x - f1 / f2  # Шаг метода Ньютона
        iterations.append((float(x), float(x_new), float(f1), float(f2)))

        x = x_new

    x_min = float(x)
    f_min = f(x_min)

    return x_min, f_min, iterations

# График средних и золотого
def print_plt(x, fnk, steps, method_name):
    x_vals = np.linspace(a - 0.1, b + 0.1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x)", color="black")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

    colors = plt.cm.rainbow(np.linspace(0, 1, len(steps)))

    for i, (a_i, b_i, x1_i, x2_i, f1_i, f2_i) in enumerate(steps):
        plt.scatter([x1_i, x2_i], [f1_i, f2_i], color=colors[i], zorder=3)
        plt.plot([a_i, b_i], [f(a_i), f(b_i)], color=colors[i], alpha=0.5)

    plt.scatter([x], [fnk], color="red", label=f"Найденный минимум", zorder=3)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"{method_name}")
    plt.legend()
    plt.grid()
    plt.show()

# График хорды
def print_plt_secant(x, fnk, steps, method_name):
    x_vals = np.linspace(a - 0.1, b + 0.1, 400)
    y_vals = f_pr(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f'(x)", color="black")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

    colors = plt.cm.rainbow(np.linspace(0, 1, len(steps)))

    for i, (a_i, b_i, x_new, f_new) in enumerate(steps):
        plt.scatter([x_new, x_new], [f_new, 0], color=colors[i], zorder=3)
        plt.plot([x_new, x_new], [f_new, 0], linestyle="dashed", color=colors[i], alpha=0.7)
        plt.plot([a_i, b_i], [f_pr(a_i), f_pr(b_i)],  color=colors[i], alpha=0.6)

    plt.scatter([x], 0, color="red", label=f"Найденный минимум", zorder=3)
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.title(f"{method_name}")
    plt.legend()
    plt.grid()
    plt.show()

# Строим Ньютона
def print_plt_newton(x, fnk, steps, method_name):
    x_vals = np.linspace(a - 0.1, b + 0.1, 400)
    y_vals = f_pr(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f'(x)", color="black")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

    colors = plt.cm.rainbow(np.linspace(0, 1, len(steps)))

    for i, (x_old, x_new, f1, f2) in enumerate(steps):
        plt.scatter([x_new], [0], color=colors[i], zorder=3)
        plt.scatter([x_old], [f_pr(x_old)], color=colors[i], zorder=3)
        plt.plot([x_old, x_new], [f_pr(x_old), 0], linestyle="dashed", color=colors[i], alpha=0.7)

    plt.scatter([x], 0, color="red", label=f"Найденный минимум", zorder=3)
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.title(f"{method_name}")
    plt.legend()
    plt.grid()
    plt.show()

# Красивые выводы
def print_iterations(steps, method_name):
    if not steps:
        print(f"\n{method_name} - нет итераций (метод сошелся сразу).\n")
        return

    col_count = len(steps[0])

    if method_name == "Метод Ньютона" and col_count == 4:
        columns = ["Шаг", "x_старый", "x_новый", "f'(x)", "f''(x)"]
    elif method_name == "Метод хорд" and col_count == 4:
        columns = ["Шаг", "a", "b", "x", "f(x)"]
    elif method_name == "Метод золотого сечения" and col_count == 6:
        columns = ["Шаг", "a", "b", "x1", "x2", "f1", "f2"]
    elif method_name == "Метод половинного деления" and col_count == 6:
        columns = ["Шаг", "a", "b", "x1", "x2", "f1", "f2"]
    else:
        print(f"Ошибка: несоответствие количества данных и названий столбцов в {method_name}")
        return

    steps_with_index = [(i + 1,) + step for i, step in enumerate(steps)]
    df = pd.DataFrame(steps_with_index, columns=["Шаг"] + columns[1:])

    print(f"\n{method_name}:\n")
    print(df.to_string(index=False))
    print("\n" + "=" * 50 + "\n")


# Начальные параметры
a, b = 0, 2
eps = 0.0001

# Половинное деление
x_min, f_min, refined_bisection_steps = refined_bisection_method(a, b, eps)
print("Метод половинного деления:")
print("Точка минимума", x_min, "; Значение функции", f_min)
print_iterations(refined_bisection_steps, "Метод половинного деления")
print_plt(x_min, f_min, refined_bisection_steps, "Метод половинного деления")

# Метод золотого сечения
x_golden, f_golden, golden_section_steps = golden_section_method(a, b, eps)
print("Метод золотого сечения:")
print("Точка минимума", x_golden, "; Значение функции", f_golden)
print_iterations(golden_section_steps, "Метод золотого сечения")
print_plt(x_golden, f_golden, golden_section_steps, "Метод золотого сечения")

# Метода хорд
x_secant, f_secant, secant_steps = secant_method(a, b, eps)
print("Метод хорд:")
print("Точка минимума", x_secant, "; Значение функции", f_secant)
print_iterations(secant_steps, "Метод хорд")
print_plt_secant(x_secant, f_secant, secant_steps, "Метод хорд")

# Метод Ньютона
x_newton, f_newton, newton_steps = newton_method(2, eps)
print("Метод Ньютона:")
print("Точка минимума", x_newton, "; Значение функции", f_newton)
print_iterations(newton_steps, "Метод Ньютона")
print_plt_newton(x_newton, f_newton, newton_steps, "Метод Ньютона")