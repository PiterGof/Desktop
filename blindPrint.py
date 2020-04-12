import random
symbols = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9')
mistakes = 0
random_message = ''

for i in range(151):
    for i in range(11):
        random_message += symbols[random.randint(0, len(symbols) -1)]
    print(random_message)
    answer = input('Answer: ')
    if answer != random_message:
        mistakes += 1
    random_message = ''
print('Number of mistraiks: %d' % mistakes)