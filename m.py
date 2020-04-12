import pickle
n = int(input())
m = int(input())
ver = []
index = {}
A = [[0] * m for i in range(m)]
print(A)
for i in range(n):
    v1,v2 = input().split()
    for v in v1,v2:
        if v not in index:
            ver.append(v)
            index[v] = len(ver) - 1
    v1_i = index[v1]
    v2_i = index[v2]
    A[v1_i][v2_i] = 1
    A[v2_i][v1_i] = 1
    print(A)
    print(index)
    print(ver)

print(A)


with open('input.txt', 'wb') as f:
    pickle.dump(A, f)

with open('input.txt', 'rb') as f:
    array = pickle.load(f)
print(array)


# def load(n):
#     G = {}
#     for i in range(1, n):
#         v1, v2 = input().split()
#         if v1 not in G:
#             G[v1] = {v2}
#         elif v1 in G:
#             G[v1].add(v2)
#         # for v, u in (v1, v2), (v2, v1):
#         #     if v not in G:
#         #         G[v] = {u}
#         #     else:
#         #         G[v].add(u)
#     return G