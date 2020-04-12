n = 0
letter = None

while True:
    letter = input('Ѕуква: ')
    if letter in ['ш', 'и', 'н', 'а']:
        n += 1

    if n == 4:
        print("Yes")
        break

    if letter == '!':
        print('No')
        break
