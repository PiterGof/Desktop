import bisect

#N, M = input().split()
# list1 = [int(input()) for _ in range(int(N))]
# list2 = [int(input()) for _ in range(int(M))]
list1 = [1, 1, 3, 3, 5, 7, 9, 18, 18, 57, 12]
list2 = [57, 3, 9, 1, 179]

for x in list2:
    i = bisect.bisect_left(list1, x)
    print(i)
    if list1[i] == x:
        print(i + 1, bisect.bisect(list1, x, i))
    else:
        print(0)