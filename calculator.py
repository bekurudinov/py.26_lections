# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Данный операции нет в системе!")




#========================================================================================



from string import digits

symbols = digits + '-' + '.'
flag = True

while flag:
    is_correct_number = True
    num1 = input('Введите первое число: ')
    for x in num1:
        if  not x in symbols:
            print('Вы ввели неправильное число!')
            is_correct_number = False
            break

    if not is_correct_number:
        continue

    num2 = input('Введите второе число: ')
    for x in num2:
        if  not x in symbols:
            print('Вы ввели неправильное число!')
            is_correct_number = False
            


    if not is_correct_number:
        continue



    num1 = float(num1) if '.' in num1 else int(num1) 
    num2 = float(num2) if '.' in num2 else int(num2) 


    operator = input('Введите оператор(+, -, *, /): ')


    if operator == '+':
        print(f'Результат: {num1 + num2}')
    elif operator == '-':
        print(f'Результат: {num1 - num2}')
    elif operator == '*':
        print(f'Результат: {num1 * num2}')
    elif operator == '/':
        print(f'Результат: {num1 / num2}')
    else:
        print('Вы ввели не правильный опретор!')

    choice = input('Хотите продолжить(yes/no)? ')
    if choice.lower().strip() == 'no':
        flag = False
        print('Досви дос!')