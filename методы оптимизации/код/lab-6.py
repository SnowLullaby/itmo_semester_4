import random
import numpy as np

# Матрица расстояний
DIST_MATRIX = [
    [0, 4, 5, 3, 8],
    [4, 0, 7, 6, 8],
    [5, 7, 0, 7, 9],
    [3, 6, 7, 0, 9],
    [8, 8, 9, 9, 0]
]

# Параметры
POPULATION_SIZE = 4
MUTATION_RATE = 0.01
GENERATIONS = 3
NUM_CITIES = 5

# Расчёт расстояния
def calculate_distance(route):
    total = 0
    for i in range(NUM_CITIES - 1):
        total += DIST_MATRIX[route[i] - 1][route[i + 1] - 1]
    total += DIST_MATRIX[route[-1] - 1][route[0] - 1]
    return total

# Создание популяции
def create_population():
    population = [list(range(1, NUM_CITIES + 1)) for _ in range(POPULATION_SIZE)]
    for route in population:
        random.shuffle(route)
    return population

# Отбор родителей
def selection(population):
    fitness_values = [1 / calculate_distance(route) for route in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]

    # Выбираем 4 разных маршрута для формирования двух пар
    indices = np.random.choice(len(population), size=4, replace=False, p=probabilities)

    # Формируем две пары: [indices[0], indices[1]] и [indices[2], indices[3]]
    pair1 = [population[indices[0]], population[indices[1]]]
    pair2 = [population[indices[2]], population[indices[3]]]

    return [pair1, pair2], probabilities

# Скрещивание
def crossover(parent1, parent2, start, end):
    child = [-1] * NUM_CITIES

    for i in range(start, end + 1):
        child[i] = parent2[i]

    # Находим второй элемент сегмента в parent1 (начало перебора)
    segment = parent1[start:end + 1]
    start_element_index = (start + 1) % NUM_CITIES

    # Создаём циклический порядок элементов parent1, начиная со второго элемента сегмента
    parent1_cycle = parent1[start_element_index:] + parent1[:start_element_index] + parent1

    parent1_index = 0
    pos = 0

    while -1 in child:
        while child[pos] != -1:
            pos = (pos + 1) % NUM_CITIES

        candidate = parent1_cycle[parent1_index]
        if candidate not in child[start:end + 1]:
            child[pos] = candidate
            pos = (pos + 1) % NUM_CITIES
        parent1_index += 1

    return child

# Мутация
def mutate(route):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(NUM_CITIES), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Основной алгоритм
def genetic_algorithm():
    population = create_population()
    best_distance = float('inf')
    best_route = None

    for gen in range(GENERATIONS):
        print(f"\n=== Поколение {gen + 1} ===")

        # 1. Исходная популяция с расстояниями и вероятностями
        print("Исходная популяция:")
        fitness_values = [1 / calculate_distance(route) for route in population]
        total_fitness = sum(fitness_values)
        probabilities = [f / total_fitness for f in fitness_values]
        for i, (route, dist, prob) in enumerate(zip(population, [calculate_distance(r) for r in population], probabilities)):
            print(f"Маршрут {i + 1}: {route}, Расстояние: {dist}, Вероятность: {prob:.4f}")

        # 2. Отбор двух уникальных пар родителей
        parent_pairs, parent_probs = selection(population)
        print("\nВыбранные пары родителей (на основе вероятностей):")
        print(f"Пара 1: Родитель 1 = {parent_pairs[0][0]}, Родитель 2 = {parent_pairs[0][1]}")
        print(f"Пара 2: Родитель 1 = {parent_pairs[1][0]}, Родитель 2 = {parent_pairs[1][1]}")

        # 3. Выбор интервала для скрещивания
        start, end = sorted(random.sample(range(NUM_CITIES), 2))
        print(f"\nВыбранный интервал для скрещивания: позиции {start + 1}-{end + 1}")

        # 4. Скрещивание для каждой пары
        children = []
        for i, (parent1, parent2) in enumerate(parent_pairs):
            child1 = crossover(parent1, parent2, start, end)
            child2 = crossover(parent2, parent1, start, end)
            children.extend([child1, child2])
            print(f"\nСкрещивание для пары {i + 1}:")
            print(f"Потомок 1: Родитель 1 = {parent1}, Родитель 2 = {parent2}, Сегмент: {child1}, Расстояние: {calculate_distance(child1)}")
            print(f"Потомок 2: Родитель 1 = {parent2}, Родитель 2 = {parent1}, Сегмент: {child2}, Расстояние: {calculate_distance(child2)}")

        # 5. Мутация для всех потомков
        children = [mutate(child) for child in children]
        print("\nПосле мутации:")
        for i, child in enumerate(children):
            print(f"Потомок {i + 1}: {child}, Расстояние: {calculate_distance(child)}")

        # 6. Формирование полной популяции (4 предка + 4 потомка)
        original_population = population.copy()
        new_population = original_population + children
        print("\nПредки + Потомки (все 8 маршрутов):")
        for i, route in enumerate(new_population):
            print(f"Маршрут {i + 1}: {route}, Расстояние: {calculate_distance(route)}")

        # 7. Сокращение популяции (оставляем 4 маршрута, убирая 4 с наибольшей длиной)
        distances_new = [(route, calculate_distance(route), i) for i, route in enumerate(new_population)]
        distances_new.sort(key=lambda x: x[1], reverse=True)  # Сортировка по убыванию расстояния
        indices_to_remove = [distances_new[i][2] for i in range(4)]  # Убираем 4 с наибольшей длиной
        population = [new_population[i] for i in range(len(new_population)) if i not in indices_to_remove]
        removed_routes = [new_population[i] for i in indices_to_remove]
        print("\nИтоговая популяция:")
        for i, route in enumerate(population):
            print(f"Маршрут {i + 1}: {route}, Расстояние: {calculate_distance(route)}")
        print("Убранные маршруты (с наибольшей длиной):")
        for i, route in enumerate(removed_routes):
            print(f"Маршрут {i + 1}: {route}, Расстояние: {calculate_distance(route)}")

        # Выбор лучшего маршрута
        for route in population:
            dist = calculate_distance(route)
            if dist < best_distance:
                best_distance = dist
                best_route = route.copy()

    return best_route, best_distance

# Запуск
best_route, best_distance = genetic_algorithm()
print(f"\nЛучший маршрут: {best_route}")
print(f"Лучшее расстояние: {best_distance}")