
# Проведите эксперимент, подтверждающий, что оператор индекса для списков имеет O(1)

import timeit
import random
import matplotlib.pyplot as plt


def plot_indexing_complexity():
    sizes = []
    times = []

    for i in range(10000, 1000001, 20000):
        random_elem = random.randint(0, i - 1)
        x = list(range(i))

        # Измеряем время выполнения операции индексации для списка
        lst_time = timeit.timeit(lambda: x[random_elem], number=1000)

        sizes.append(i)
        times.append(lst_time)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-')
    plt.title('Time Complexity of List Indexing')
    plt.xlabel('Size of the List')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()


def set_dict_value(d, key, value):
    d[key] = value


def plot_dict_operations_complexity():
    sizes = []
    get_times = []
    set_times = []

    for i in range(10000, 1000001, 20000):
        d = {j: j for j in range(i)}
        random_key = random.randint(0, i - 1)

        # Измеряем время выполнения операции получения элемента из словаря
        get_time = timeit.timeit(lambda: d[random_key], number=1000)

        # Измеряем время выполнения операции записи элемента в словарь
        set_time = timeit.timeit(lambda: set_dict_value(d, random_key, random_key), number=1000)

        sizes.append(i)
        get_times.append(get_time)
        set_times.append(set_time)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, get_times, marker='o', linestyle='-', label='Get Operation')
    plt.plot(sizes, set_times, marker='x', linestyle='-', label='Set Operation', color='red')
    plt.title('Time Complexity of Dictionary Operations')
    plt.xlabel('Size of the Dictionary')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_delete_dict_list_operations_complexity():
    sizes = []
    get_times = []
    set_times = []

    for i in range(10000, 1000001, 20000):
        d = {j: j for j in range(i)}
        random_key = random.randint(0, i - 1)

        # Измеряем время выполнения операции получения элемента из словаря
        get_time = timeit.timeit(lambda: d[random_key], number=1000)

        # Измеряем время выполнения операции записи элемента в словарь
        set_time = timeit.timeit(lambda: set_dict_value(d, random_key, random_key), number=1000)

        sizes.append(i)
        get_times.append(get_time)
        set_times.append(set_time)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, get_times, marker='o', linestyle='-', label='Get Operation')
    plt.plot(sizes, set_times, marker='x', linestyle='-', label='Set Operation', color='red')
    plt.title('Time Complexity of Dictionary Operations')
    plt.xlabel('Size of the Dictionary')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_del_complexity():
    sizes = []
    list_times = []
    dict_times = []

    for i in range(10000, 1000001, 40000):  # Увеличенный шаг до 40,000
        random_index = random.randint(0, i - 1)
        print(f'Итерация {i}')
        random_key = random_index  # Для словаря ключ будет таким же, как и индекс для списка

        # Измеряем время выполнения операции del для списка
        list_code = f'''
lst = list(range({i}))
del lst[{random_index}]
'''
        list_time = timeit.timeit(list_code, number=10)  # Уменьшено количество итераций до 50

        # Измеряем время выполнения операции del для словаря
        dict_code = f'''
d = dict.fromkeys(range({i}), 0)
del d[{random_key}]
'''
        dict_time = timeit.timeit(dict_code, number=10)  # Уменьшено количество итераций до 50

        sizes.append(i)
        list_times.append(list_time)
        dict_times.append(dict_time)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_times, marker='o', linestyle='-', label='List del Operation')
    plt.plot(sizes, dict_times, marker='x', linestyle='-', label='Dict del Operation', color='red')
    plt.title('Time Complexity of del Operator')
    plt.xlabel('Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


def partition(nums, low, high):
    pivot_index = random.randint(low, high)
    pivot = nums[pivot_index]
    nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


def quickselect(nums, k):
    low, high = 0, len(nums) - 1
    while low <= high:
        pivot_index = partition(nums, low, high)
        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

# Пример использования:
