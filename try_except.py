# Обработка  исключений 
# оператор try except

# ошибки -> связаны с кодом 
# SyntaxError
# IndexError
# TabError


#исключение -> Invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# IndexError
# ValueError
# ImportError
# BaseException # прородитель всех исключений 

# try except

# try:
#     <body try>
# except <Exception>:
#     <body>
# else:
#     <body> Только если все окей
# <finally>:
#     <body> в любом случае в конце

# num1 = int(input('Введите число'))
# print(num1)
# print('Important')

# try:

#     num1 = int(input('Введите число'))
# except ValueError:
#     print('Invalid Value')
# else:
#     print(num1)


# print('Important')

# try:
#     num1 = int(input('Введите  первое число : '))
#     num2 = int(input('Введите  первое число : '))
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError) as error:
#     print('Вы вели некоректные данные !')
#     print(error)

# try:
#     num1 = int(input('Введите  первое число : '))
#     num2 = int(input('Введите  первое число : '))
#     print(num1 / num2)
# except Exceptionas  as error:
#     print('Вы вели некоректные данные !')
#     print(error)


# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Vvedite index : '))
#     res = list_[index]
#     print(res)
# except ValueError:
#     print('Value error!')

# except IndexError:
#     print('Index error!')

# try:

#     num1 = int(input('Enter:'))
#     num2 = int(input('Enter:'))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('na o delit\' nal\'zya!')
# except ValueError:
#     print('invalid symbols for int()!')
# else:
#     print(result)
# finally:
#     print('The end!')



# num1 = 28
# num2 = 65
# num3 = 1100
# num4 = 54
# num5 = 32

# def operations(num):
#     print({"2": num ** 2, "3": num ** 3, "100": num / 100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)
# dict1 = {"2": num1 ** 2, "3": num1 ** 3, "100": num1 / 100}
# dict2 = {"2": num2 ** 2, "3": num2 ** 3, "100": num2 / 100}
# dict3 = {"2": num3 ** 2, "3": num3 ** 3, "100": num3 / 100}
# dict4 = {"2": num4 ** 2, "3": num4 ** 3, "100": num4 / 100}
# dict5 = {"2": num5 ** 2, "3": num5 ** 3, "100": num5 / 100}
# print(dict1,dict2,dict3,dict4,dict5)

# Функиция - это именнованная часть программы, котороя содерижит в себе набор инструкций , и котороя может вызываться в других частях программы столько раз сколько угодно


# def name_of_function(<a, b>):# параметры
    #<body> # код какая та логика который возрашаяет конечный результат
    #<return># оператор для возрашение результата

# name_of_function(<5, 6> #аргументы)

# Паркаметры функции - переменные которые будут принимать даныые которые мы переедаем в функцию
# Аргументы данные которые мы передаем в фуекцию в моменте когда ее вызывает

# return - опертор который нужен для того чтобы функцияя возрашала результат, если return не указать, то функция возрашет None



ls = [1,2,3,4,5,6,7]
str1 = 'Hello world svami Kani!'
def our_len(obj):
    i = 0
    print(obj)
    for x in obj:
        i += 1
    print('result:', i)
    return i

print(our_len(ls), '!!!')
our_len(str1)


# res = max([1,2,3,4])
# print(res)

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# print(isEven(7))
# print(isEven(9))
# print(isEven(10))

# def isEven(obj: int) -> bool:
#     '''Our function returns True Or False While Checking number for even number!'''
#     if obj % 2 == 0:
#         return True
#     return False
# print(isEven(10))

# ls = [1,2,3]
# print(ls.reverse())
# print(ls)


# def my_func(a,b,c):

#     pass
# my_func(1,2)



# tenet, ded, anna, kazak
# from typing import List

# def get_polindom(words: List[str]) -> List(str):
#     '''Function return a polindrom list of strings!'''
#     result = []
#     for x in words :
#         if x.lower() == x[::-1].lower():
#             print('Polindrom find : {x}!')
#             result.append(x)

#     return result

# ls = ['John', 'Ono', 'kazak', 'peter', 'dovod', 'radar', 'apa', 'piko']
# print(f'Result: {get_polindrom(ls)}')

# def get_percentage(money:float, period:int)-> float:
#     '''returns final amount of money'''
#     if money <30000:
#         raise ValueError("Invalid value for money parameter!")

#     elif period<3:
#         raise ValueError("Invalid value for period parameter!")

#     i = 0
#     while i < period:
#         money+= money * 0.1
#         #money = money * 1.1
#         #money = (money/100 * 10)
#         i+=1

#     return money
# try:
#     money = float(input("Vvedite summa deneg: "))
#     year = int(input("Vvedite  srok vashego deposita: "))

# except ValueError:
#     print("Invalid values!")
# else:
#     print(get_percentage(money, year))


#====================================

# Default parameters 
# def func():
#   print('Hello world!')

# func()

# def print_welcome(name = "User"):
#     print(f'Welcome, {name}')

# print_welcome('John Snow')


# def introduce(name: str, last_name: str, work: str = None):

#     print(f'This persons name is {name}!')
#     print(f'This perSONS lst name is {last_name}!')
#     if work:
#         print(f'This persons work is {work}!')


# introduce('John', 'Snow', 'King')
# introduce('sultan', 'katana')

# '-------------------------------------'
# def get_reverse_text(text: str) -> str:
#     '''reversing the text'''
#     ls = text.split(' ')
#     return '  '.join(ls[::-1])

# str1 = 'Hello world ! My name is John Last name is Snow. Nice to meet you!'
# print(get_reverse_text(str1))