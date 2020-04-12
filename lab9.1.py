array = [90, 22, 10, 61, 75, 23, 1, 0, 99, 45, 67, 53, 36]

print(array)
# Пузырек
for i in range(len(array)):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            t = array[i]
            array[i] = array[i + 1]
            array[i + 1] = t

print(array)

# Сортировка вставками
def InsertionSort(A):
    for i in range(1, len(A)):
        # В new_elem сохранили значение A[i]
        new_elem = A[i]
        # Начиная с элемента A[i - 1]
        j = i - 1
        # все элементы, которые больше new_elem
        while j >= 0 and A[j] > new_elem:
            # сдвигаем вправо на 1
            A[j + 1] = A[j]
            j -= 1
        # На свободное место записываем new_elem
        A[j + 1] = new_elem
    return A
print(InsertionSort(array))


def corting(A):
    p = 6
    array_min = []
    array_max = []
    for i in range(len(A) - 1):
        if A[i] > p:
            if A[-(i - 1)] < p:
                A[i], A[-(i - 1)] = A[-(i - 1)], A[i]
    return A

print(corting(array))