n = 0
letter = None

while True:
    letter = input('�����: ')
    if letter in ['�', '�', '�', '�']:
        n += 1

    if n == 4:
        print("Yes")
        break

    if letter == '!':
        print('No')
        break
