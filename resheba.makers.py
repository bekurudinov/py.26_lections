# # x =int(input('Введите число1: ')) 
# # y = int(input('Введите число2: ')) 

# # if x % y == 0:
# #     print('x делится на y')
# #     print(f'Частное : {x // y}')

# # else:
# #     print('x не  делится на y')
# #     print(f'Частное : {x // y}')
# #     print(f'Остаток: {x % y}')
# # ===============================================

# # name = 'john snow man'

# # Step_2  = name[0:13:2]
# # Step_3  = name[0:13:3]

# # print(Step_2)
# # print(Step_3)



# # print(name[0:13:2])


# string1 = "America" 
# string2 = "Japan"
# a = [0:13:3]#America Japan
# print(a)







# import random

# ls = ['Plov', 'Manty', 'kuurdak', 'Lagman', 'oromo']
# P = 0
# M = 0
# k = 0
# L = 0
# o = 0

# for x in range (0, 1_0000):
#     choice = random.choice(ls)
#     # print(choice)

#     if choice.lower()=='plov':
#         P +=1
#     elif choice.lower()=='manty':  
#         M +=1
#     elif choice.lower()=='kuurdak':
#         k +=1
#     elif choice.lower()=='lagman':
#         L +=1
#     elif choice.lower()=='oromo':
#         o += 1


# print('Результаты голодных игр:')
# print(f'plov{P}\nManty: {M}\kuurdak: {k}\nLagman: {L}\nOromo: {o}')


# suitcase = []
# num = suitcase.append['футболка', 'шорты', 'сланцы', 'очки', 'кепка'] 
# num1 = suitcase.pop
# print(num1)
#========================================================
#2 list_ = [comprehension  for comprehension in range (1, 50) if comprehension % 2 != 0 ]
# print(list_)

#3 list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x for x  in list_ if x % 2 == 0 and x > 0]
# print(int_list)

#4 list_ = [x **2 for x in range (1,26)]
# print(list_)

#5 str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [ int(x) for x in str_list]
# print(int_list)

#6 list_ = [x ** 2 if x % 2 == 0 else x for x in range(1, 11)]
# print(list_)

#7 list_  = [x == False if x % 2 != 0 else True for x in range(1,11)]
# print(list_)

#8 list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(i) <= 4 else 'longer' for i in list_name]
# print(new_list)

#9 dict_ ={x: x ** 2 for x in range(1,11)}
# print(dict_)

#10 n = int(input())
# dict_ = {i: i ** 2 for i in range(n, 501) if i % n == 0}
# print(dict_)


#11  a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: list(range(1,v+1)) for k, v in a.items()}
# print(dict_)

#12 dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: 'odd' if v % 2 != 0 else 'even' for k, v in dict_.items()}
# print(a)

#13 string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# a = [int(i) for i in filter(lambda x: x.isnumeric(),string_.split())]
# list_ = list(map(str,a))
# print(list_)

# 16 list_ = [x * 2 for x in range (1, 13)]
# print(list_)

#17 list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x-x+1 if x < 0 else x for x in list_]
# print(int_list)

# 20 list_ = [False, True, False, True, False, True, False, True, False, True]
# list1 = [x+0 if x == False else 1 for x in list_]
# print(list1)

# 21 list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [len(x) for x in list_name]
# print((new_list))

# 22 list_ = [x for x in range(1,1000,125) if x % 2 == 0]
# print(list_)

# 23 list1 = [44,54,64,74,104]
# list2 = [x+6 for x in list1]
# print(list2)

#24 list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [x for x in list1 if x**2 > 50]
# print(list2)

#25string = "happy birthday!"
# list_= [x for x in string if x != " " and x != "!"]
# print(list_)

# 26 dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list1 = [y for k,v in dict_.items() for x,y in v.items()]
# print(list1)

#27  list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# dict1 = {k : len(k)**2 for k in list_name if len(k)>4}
# print(dict1)

#28 dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# list1 = [key.upper() for key,value in dict_.items() if 200 < value < 5000]
# print(list1)


# 29 dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i',''):k.count('i') for k,v in dict1.items()} 
# print(dict2)

#30 list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []] 
# list2 = [x for x in list1 if x]
# print(list2)


#1 try:
#     print("text")
# except:
#     print("none code")
# else:
#     print("non code")
# finally:
#     print("the end")


#2 try: 
#     b = 10
#     c = 11 
#     print(a) 
# except: 
#     print('Такой переменной не существует!')



#3  try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1/num2)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')

#4 try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(res)


# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key1'])
# except KeyError:
#     print('Нет такого ключа!')

# 6 list_ = [1, 4, 9, 16, 25, 36] 
# try:
#     print(list_[3])
# except:
#  print('Нет такого элемента!'


#7 try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError)as error:
#     print('Произошла ошибка!')

#1  def add(num1 , num2):
#     return num1 + num2
# print(add(23,1))
# from typing  import Optional



#1 var = 'переменная в foo' 
# def foo(): 
#     global var 
#     var = 'переменная foo' 
#     print('переменная в foo: ', var)

#     def bar():
#         global var 
#         var = 'переменная bar' 
#     bar() 
# foo() 
# print('переменная в foo: ', var)

#2 x = "Я глобальная переменная!" 
# def my_func(): 
#     global x 
#     print(x) 
#     x = "Я могу изменяться" 
    
# my_func() 
# print(x)

#3 num = 3
# def mul():
#     global num
#     num = num **2
# mul()
# mul()
# mul()
# print(num)

#4  balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount
# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print(f'Вы заплатили {amount} сом за {log_name}')
#     return balance
# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()
    
#5 result = 0 
# def pow_first(x,y): 
#     global result 
#     result = x ** y 
# def pow_second(z): 
#         global result 
# result = result % z 
# pow_first(2, 3) 
# pow_second(3) 
# print(result)

#6 a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16} 
# for k, v in a.items(): 
#     if v >= 17: print(f'{k}, Вы можете войти в клуб') 
# else: 
#     print(f'{k}, извините, Вы не проходите по age-control')

# a = ['father', 'mother', 'brother', 'sister'] 
# b = [] 
# for i in a: b.append(i.capitalize()) 
# print(b)


#1 from functools import reduce
# list_ = [1, 2, 3, 4] 
# result = reduce(lambda x, y:x + y,list_)
# print(result)


#2 list_ = [5, 8, 4, 6, 7] 
# result = all(int>3 for int in list_)
# print(result)

# list_ = [5, 8, 4, 6, 7] 
# result = all(x>0 for x in list_)
# print(not result)


# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda x: len(x)>7,list_))
# print(result)
