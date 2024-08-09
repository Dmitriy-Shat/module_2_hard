import random


def random_number():
    number = random.randint(3, 20)  # функцию вставил потому что мог
    return number


number = random_number()
print('Случайное значение первого столба:', number)
list_ = []
for i in range(1, number):
    for j in range(1, number):
        if number % (i + j) == 0 and i < j:
            list_.append(f'{i}' + f'{j}')
password = ''
for k in list_:
    password += k
print('Пароль:', password)
