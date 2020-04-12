f = open('input.txt', 'r')
data = f.read()
f.close()
data = data[:-1]
array = ['()', '{}', '[]', '<>']
for i in range(len(data)):
    for q in array:
        data = data.replace(q, '')

if data == '':
    print('YES')
else:
    print(data)
    print('NO')




# array = []
#
# print(data)
# # for i in range(len(data) - 1):
# #     del data[i]
# #     array.append(data[i])
# #     if data[i] in [')', '}', ']', '>']:
# #         for q in range(len(array) - 1):
# #             if array[q] == '(':
# #                 array[q] = ')'
# #             elif array[q] == '[':
# #                 array[q] = ']'
# #             elif array[q] == '{':
# #                 array[q] = '}'
# #             else:
# #                 array[q] = '>'
# #         break
# # print(array)
#
# array = [data[i] for i in range(len(data) - 1) if data[i] not in [')', '}', ']', '>']]
#
# array = array[::-1]
# for q in range(len(array) - 1):
#     if array[q] == '(':
#         array[q] = ')'
#     elif array[q] == '[':
#         array[q] = ']'
#     elif array[q] == '{':
#         array[q] = '}'
#     else:
#         array[q] = '>'
# for i in array:
#     if i in data:
#         del
# print(array)


