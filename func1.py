# def sum_of_args(a, b, c, d):#params
#     return a + b + c + d

# result = sum_of_args
# print(result)
# print(result(5, 10, 15, 20))


#-------------------------------------------
# позиционые и именнованное аргументы

# def printParams(a=None, b=None, c=None):
#     print(a, 'is stored in parama a')
#     print(b, 'is stored in parama b')
#     print(c, 'is stored in parama c')

# printParams(a = 5, c = 15)

# def sum_of_args(a, b, c, d):#params
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20))#arguments (поозицонные аргументы)
# print(sum_of_args(a=5, c=15, d=20, b=10)) #keyword arguments(именнованные аргументы)                                     
# print(sum_of_args(5, 10, d=20, c=15))


#--------------------------------------------------------------------------
#опертор *
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)

#--------------------------------------------------------------------------------
# *args **kwargs в функциях

# def printScores(student, *args):
#     print(f'Student name: {student}')
#     print(args)

# printScores('John Snow', 100, 99, 95, 90)


# def printScores(student, *args):
#     print(f'Student name: {student}')
#     print(type(args))
#     for x in args:
#         print('args:', x)

# printScores('John Snow', 100, 99, 95, 90)




# def print_pet_names(onwer, **pets):
#     print(f'Owner name: {onwer}')
#     # print(pets)
#     # print(dict(**pets))
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')
# print_pet_names('John snow', dog='Rex', cat='Garfild', fish=['Nemo', 'DORI', 'Alex'], turtle = 'Leonardo')


# def get_some_data(a, b, *args, **kwargs):
#     print('Параметры a и  b:', a, b)
#     print('Аргументы:', args)
#     print('Именованные аргументы:', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])

# get_some_data(1, 2, 3, 4, 5, lang= 'Python', name = 'john Snow', car = 'BMW M8')


# def generate_random_string(len_):
#     import string as s
#     import random
#     random_str = ''.join(random.choice(s.ascii_letters +s.digits) for i in range (0, len_))
#     return random_str

# print(generate_random_string(25))



#----------------------------------------------------------------




def add(a , b): return a + b

def substract(a, b): return a - b

def multiplay(a, b): return a * b

def divide(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


def calc(num1,  num2):
    operator = input('Введите опертор (+,-,*,/):')
    if operator == '+': return add (num1, num2)
    elif operator == '-': return substract (num1, num2)
    elif operator == '*': return multiplay (num1, num2)
    elif operator == '/': return divide (num1, num2)
    else:return 'Вы ввели неверный опертор!'

def main():
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели некоректнные данные')
        main()
        return
    while True:
        result = calc(num1, num2)
        if type(result) == float:
            print(f"Result: {result}")
            break
        else:
            print(f"Result: {result}")

    question = input('Хотите продолжить (YES/NO)? ')
    if question.lower() == 'yes':
        main()
    else:
        print('Спасибо зa использование нашего калькулятора! Пока!')
main()
    

    