import random

num = random.randint(1,10)
user = int(input("Угадайте число: "))
count = 1
for i in range(3):
    if user == num:
        print("Отлично! Вы угадали число", num, "с", count, "попытки!")
        break
    elif i != 2:
        print("К сожалению не правльное число")
    count += 1
    user = int(input("Попробуйте ещё раз: "))
else:
    print("Не смогли отгадать число", num, "c 3 попыток.")

a = input('Хотите продолжить yes/no?')
