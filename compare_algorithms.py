import timeit
import random

# ---------- 1. Insertion Sort (Сортування вставками) ----------
def insertion_sort(arr):
    # Копіюємо масив, щоб не змінювати оригінал при тестуванні
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a


# ---------- 2. Merge Sort (Сортування злиттям) ----------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------- 3. Timsort (Вбудований sorted) ----------
def tim_sort(arr):
    return sorted(arr)


# ---------- Функція тестування ----------
def compare_algorithms():
    print(f"{'Algorithm':<25} | {'Size':<10} | {'Time (sec)':<15}")
    print("-" * 60)

    sizes = [100, 1000, 5000]

    for size in sizes:
        # Генеруємо список випадкових чисел
        test_data = [random.randint(0, 100_000) for _ in range(size)]

        # 1. Insertion Sort: O(n^2)
        time_insertion = timeit.timeit(lambda: insertion_sort(test_data), number=1)

        # 2. Merge Sort: O(n log n)
        time_merge = timeit.timeit(lambda: merge_sort(test_data), number=1)

        # 3. Timsort: O(n log n), гібридний
        time_timsort = timeit.timeit(lambda: tim_sort(test_data), number=1)

        print(f"{'Insertion Sort':<25} | {size:<10} | {time_insertion:.5f}")
        print(f"{'Merge Sort':<25} | {size:<10} | {time_merge:.5f}")
        print(f"{'Timsort (Built-in)':<25} | {size:<10} | {time_timsort:.5f}")
        print("-" * 60)


if __name__ == "__main__":
    compare_algorithms()