from decimal import Decimal, getcontext

getcontext().prec = 10

def f(x):
    return (Decimal(0.25) * x ** 4) + (x ** 2) - (Decimal(8) * x) + Decimal(12)


def step2(x1, delta_x, epsilon1, epsilon2):
    x2 = x1 + delta_x
    return step3(x1, x2, delta_x, epsilon1, epsilon2)


def step3(x1, x2, delta_x, epsilon1, epsilon2):
    f1, f2 = f(x1), f(x2)
    return step4(x1, x2, f1, f2, delta_x, epsilon1, epsilon2)


def step4(x1, x2, f1, f2, delta_x, epsilon1, epsilon2):
    if f1 > f2:
        x3 = x1 + 2 * delta_x
    else:
        x3 = x1 - delta_x
    return step5(x1, x2, x3, f1, f2, delta_x, epsilon1, epsilon2)


def step5(x1, x2, x3, f1, f2, delta_x, epsilon1, epsilon2):
    f3 = f(x3)
    return step6(x1, x2, x3, f1, f2, f3, delta_x, epsilon1, epsilon2)


def step6(x1, x2, x3, f1, f2, f3, delta_x, epsilon1, epsilon2):
    f_min = min(f1, f2, f3)
    x_min = {f1: x1, f2: x2, f3: x3}[f_min]
    return step7(x1, x2, x3, f1, f2, f3, x_min, f_min, delta_x, epsilon1, epsilon2)


def step7(x1, x2, x3, f1, f2, f3, x_min, f_min, delta_x, epsilon1, epsilon2):
    numerator = ((x2 ** 2 - x3 ** 2) * f1 + (x3 ** 2 - x1 ** 2) * f2 + (x1 ** 2 - x2 ** 2) * f3)
    denominator = ((x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3)
    x_bar = Decimal('0.5') * numerator / denominator
    return step8(x1, x2, x3, f1, f2, f3, x_min, f_min, x_bar, delta_x, epsilon1, epsilon2)


def step8(x1, x2, x3, f1, f2, f3, x_min, f_min, x_bar, delta_x, epsilon1, epsilon2):
    f_bar = f(x_bar)

    if x_bar == 0:
        return x_bar(x_min, delta_x, epsilon1, epsilon2)

    condition1 = abs(f_min - f_bar) / abs(f_bar) < epsilon1
    condition2 = abs(x_min - x_bar) / abs(x_bar) < epsilon2

    print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}, x_bar = {x_bar}, con_1 = {condition1}, con_2 = {condition2}")

    if condition1 and condition2:
        print(f"Минимум найден: x = {x_bar}, f(x) = {f_bar}")
        return x_bar

    if x1 <= x_bar <= x3:
        new_x_min = x_min if f(x_min) < f(x_bar) else x_bar
        points = sorted([x1, x2, x3, x_bar])
        idx = points.index(new_x_min)

        if 0 < idx < len(points) - 1:
            new_x1, new_x3 = points[idx - 1], points[idx + 1]
        else:
            return step2(x_bar, delta_x, epsilon1, epsilon2)

        return step6(new_x1, new_x_min, new_x3, f(new_x1), f(new_x_min), f(new_x3), delta_x, epsilon1, epsilon2)

    return step2(x_bar, delta_x, epsilon1, epsilon2)


x_start = Decimal(1)
delta_x = Decimal(0.5)
epsilon1 = Decimal(0.0001)
epsilon2 = Decimal(0.0001)
step2(x_start, delta_x, epsilon1, epsilon2)

