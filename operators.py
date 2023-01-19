# операторы сравнение
# Условные операторы
# Логические операторы

# операторы сравнение 
# <, >, ==, <=, >=, !=(не равно)
# num1 = 18
# num2= 15
# print(num1 >= num2)

# stroka1 = 'hello'
# stroka2 = 'world'
# print(stroka1 > stroka2)

# print(ord('H'))
# print(ord('W'))
# print(chr(1100))

# text = 'Hello world! My name is john'

# if  ord(text[0])== 72:
#     print('Yes')
# else:
#     print('Noo')

# условные операторы они созданы чтобы программа могла выполнять разные участки кода в зависимости от условия
#'if' , 'elif', 'else'

# if <condition>:
#     <body if>
#     <body if>#сработает только если true
# elif <condition>:
#     <body elif>
# elif <condition>:
#     <body elif>
# else:
#     <body else>#сработает только если во ысех остальных false

# string = input('enter smt: ')

# if string == 'Hello':
#     print('hello stranger')
# elif string == 'john':
#     print('welcome back john snow')
# elif string == 'Mersedez':
#     print('mersedez benz S class')
# else:
#     print('совпадений не найдено')

# print('The end')


# email = input('Enter Email: ')
# password1 = input('Enter password: ')
# if len(password1) < 8:
#     raise Exception('Password too short! (password need at least 8 characters!)')

# password2 = input('Enter password confirmation: ')

# if password1 != password2:
#     raise Exception('Passwords did\t match!')
# else:
#     print('Successfully signed up!')


# age = input('введите свой возраст: ')

# if age.isdigit():
#     age = int(age)
#     print(f'Your age:  {age}!')

# else:
#     raise Exception('Enter the valid age(only digits!)')

# if age > 170:
#     raise Exception('Invalid age')

# if age < 18:
#     print('Chuvak prihodi cherez {18-age} let/goda!')
# else:
#     print('Ty prohodish\' po vozrastu, Welcome!')

#лоигическое операторы

# and -> логическое и
# or -> лог или
# not -> лог отрицание

# операторы идентификации
# in -> провверяет наличие элемента вннутри массива либо 
# строки
# is -> сравнивет ячейки памяти
# == сравнивает значение
# is not -> орицальное сравнение двух ячеек 
    
# my_age = 20
# other_age = 18
# result = my_age == 21 or other_age == 18
# #true    #true

# print(result)

# result = not my_age == 15
#     #true
# print(result)


# cash = int(input('Enter your cash: '))

# if cash > 1000 and cash < 10000:
#     print('Sredne')
# elif cash >= 10000 and cash < 100_000:
#     print('mnogo')
# elif cash >= 100_000:
#     print('krasavchik!')
# else:
#     print('pechal\'no!')


# is_google_user = False
# is_github_user = True
# is_age_less_21 = True
# user_coin = 3000

# if (is_google_user or is_github_user) and (is_age_less_21 or user_coin > 5000):
#     print('You enter the system')
# else:
#     print ('Sorry you couldn\'t enter! ')

str1 = 'Hello world'
choice = input('Enter the character: ')

if choice in str1:
    print(f'Символ {choice} есть в строке :"{str1}" ')
else:
     print(f'Символ {choice} нет в строке :"{str1}" ')  



;      mark = int(input('Введите значение: '))
; if mark >= 90:
;     print('Отлично, Ваша оценка 5!')
; elif mark >= 80:
     print('Здорово, Ваша оценка 4!')
 elif mark >= 70:
     print('Хорошо, Ваша оценка 3!')
 elif mark >= 60:
     print('Вам стоит подучить материал!')

 else:
     print('Вы не сдали экзамен')