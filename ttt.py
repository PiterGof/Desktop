import timeit, random, prettytable
array = [900231, 278902, 1230, 6111111, 7457895, 2323, 112345667890, 987650, 5345399, 4143145, 6311237, 5313, 36]
array2 = [36, 1230, 2323, 5313, 278902, 900231, 987650, 4143145, 5345399, 6111111, 6311237, 7457895, 112345667890]
array3 = [112345667890, 7457895, 6311237, 6111111, 5345399, 4143145, 987650, 900231, 278902, 5313, 2323, 1230, 36]



def a(array):
    for i in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                t = array[i]
                array[i] = array[i + 1]
                array[i + 1] = t

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



def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]

        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return QuickSort(L) + M + QuickSort(R)





print(timeit.timeit('a(array)', setup='from __main__ import a, array', number=1))
print(timeit.timeit('InsertionSort(array)', setup='from __main__ import InsertionSort, array', number=1))
print(timeit.timeit('QuickSort(array)', setup='from __main__ import QuickSort, array', number=1))

print()
print(timeit.timeit('a(array2)', setup='from __main__ import a, array2', number=1))
print(timeit.timeit('InsertionSort(array2)', setup='from __main__ import InsertionSort, array2', number=1))
print(timeit.timeit('QuickSort(array2)', setup='from __main__ import QuickSort, array2', number=1))

print()
print(timeit.timeit('a(array3)', setup='from __main__ import a, array3', number=1))
print(timeit.timeit('InsertionSort(array3)', setup='from __main__ import InsertionSort, array3', number=1))
print(timeit.timeit('QuickSort(array3)', setup='from __main__ import QuickSort, array3', number=1))