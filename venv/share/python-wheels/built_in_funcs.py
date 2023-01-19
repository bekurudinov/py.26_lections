# Всторенные функции

#map
# filter
# lambda
# enumerate
# zip, all, any
# (reduce)


# Анонанимные функции - lambda(такие же функции толлько без название)
# lambda функции могут принимать сколько угодно аргументов, но всегда возращают одно выражение


# def sum_of_args(a, b):
#     res = a +b
#     return res

# print(sum_of_args(1,2))

# a = sum_of_args
# print(a(5, 15))

# sum_of_args2 = lambda a, b, c: sum([a + b + c])
# print(sum_of_args2(5, 15, 20))

# x = lambda a ,b, c: (a*b)%c
# print(x(11, 5, 10))


# get_last = lambda ls: ls[-1]
# ls = [1,2,3,4,5,6, True, False, [1,2,3], 'last']
# print(get_last(ls))


# def  myFunc(n):
#     return lambda a: a * n

# myDoubler = myFunc(2)
# myTripler = myFunc(3)
# print(myDoubler(50))
# print(myDoubler(100))
# print(myDoubler(23))
# print(myTripler(55))


# dict_ = {'John': 50_000, 'Sultan': 5, 'Jamie': 1000000000000, 'Aigerim':1_000_000}
# res = dict(sorted(dict_.items(), key = lambda x:x[1], reverse=True))
# print(res)


#=====================================
# map(function, iterable) - применяет функцию к каждому элменту из последовательности и возращет mapobject(интертор)с результатом


# ls = ['one', 'two', 'three', 'four']
# # for i in range(0, len(ls)):
# #     ls[i] = ls[i].upper()

# # print(ls)

# res =list(map(str.upper, ls))
# print(res)


# names = ['john', 'sultan', 'jamie', 'raychel']
# res =list(map(lambda name:f'Hello mr/ms {name}', names))
# print(res)



# dict_ = {1:2, 3:4, 5:6}
# res = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(res)

#======================================================
# filter(function, iterble) - > применяет ко всем элементом iterable функцию которую мфы передали и возращает итератор с теми элементами для которых функция вернуала True



# ls = ['one', 'two', '', 'list', '100', '1', 'john']
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)

# print(res)

# res = list(filter(str.isdigit, res))
# print(res)

# ls = ['john', 'makers', 'sultan', 'ono', 'mama', 'bek', 'fgftggdf']
# res = list(filter(lambda stroka: len(stroka)>5, ls))
# print(res)



# ls = [
#     {'name': 'Python', 'point': 10},
#     {'name': 'c++', 'point': 6},
#     {'name': 'js', 'point': 8},
#     {'name': 'Java', 'point': 3},
#     {'name': 'c#', 'point': 0},
# ]
# res = list(filter(lambda dict_:dict_['point'] >= 7, ls))
# print(res)

# users = [
#     {'username':'John', 'comments':['I love you', 'Really good']},
#     {'username':'Raychel', 'comments':[]},
#     {'username':'Steven', 'comments':['Bishkek', 'Python']},
#     {'username':'Hello', 'comments':[]},
#     {'username':'Kira', 'comments':['The best post']}
# ]
# inactive_users = list(filter(lambda dict_obj: not dict_obj['comments'], users))
# print(inactive_users)
#===============================================================

# names = ['raychel', 'sultan', 'Aigerim', 'john', 'kira', 'bob']
# new_names = list(map(lambda name: f'Your name is {name}!',filter(lambda x: len(x)>4, names)))
# print(new_names)

#==============================================
# from functools import reduce

# ls = [1,2,3,4,5,6]
# sum = reduce(lambda a, b:a + b,ls)
# res = reduce(lambda a, b:a * b,ls)
# print(sum)
# print(res)




#===============================================
# ls = ['john', 'sultan','katana','Aigerim']
# for i, obj in enumerate(ls):
#     print(i, obj)

#============================================

# import string as s
# import random

# def generate_rand_str():
#     symbols = s.ascii_letters + s.digits
#     res = ''.join(random.choice(symbols) for i in range(0, 10))
#     return res

# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())

#==================================================



# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = '_()$%@+-#!'

# q_pass = int(input('введите количество паролей: '))

# res = {
#     f(choices(ascii_letters, k=10), choices(digits, k =5), choices(symbols, k =2))
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }
# print(res)
# print(f'Количество паролей: {len(res)}')

# from statistics import mean

# dlina = [len(x) for x in res]
# print(f'Average len:{mean(dlina)}')7
#==================================================


# # zip(iterables) -она соединает каждый элемент итерируемых обьектов между собой по их рааспаковку в тип  данных typle и возрашет

# # ls1 = [1, 2, 3]
# # ls2 = [100, 200, 300]

# # res = list(zip[ls1, ls2])
# # print(res)

# # ls1 = [1,2,3,4,5]
# # ls2 = [100, 200, 300, 400, 500]
# # ls3 = [10, 20, 30]
# # res =list(zip(ls1, ls2, ls3))
# # print(res)

# #zip для создание словарей

# a =dict([(1, 2),(3, 4)])
# print(a)

# d_keys = ['hostname', 'loaction', 'vendor', 'model', 'ios','ip']
# d_values = ['apple_r1', 'winterfell', 'jobs', 'wach', '16.0', '10.255.0.1']
# res= dict(zip(d_keys,d_values))
# print(res)


# d_keys = ['hostname', 'loaction', 'vendor', 'model', 'ios','ip']
# date = {
#     'r1': ['london_r1', 'New globle Walk','cisco', '4451','15.4', '10.255.1'],
#     'r2': ['london_r2', 'Noth london','cisco', '5541','16', '10.255.10'],
#     'r3': ['london_r3', 'South_West','cisco', '3850','156.4', '10.255.144']
      
# }
# res1 = dict(zip(d_keys,date))
# res2 = dict(zip(d_keys,date))
# res3 = dict(zip(d_keys,date))
# print(res1)
# print(res2)
# print(res3)


# print(date)
# for k in date:
#     date[k] = dict(zip(d_keys,date[k]))
# print(date)


# all(), any()

# all(iterablle) -  вохзрашает True,если все элементы внутри обьекта исттина ,иначе возрашает False

# [1,2]->True
# all([True])->False
# all(['False', 'John',5,6,7,])->True
# all([[1,2,3], 5, None])-False

# print(all([[1,2], 5, 'stroka', True, 1,]))


# ip = '10.10.10.10'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)


# any - возрашает True, если хотябы один элемент исттинна


# ls = [0, 0, 0,'', False,1]
# print(any(ls))


ignore =['rm -rf', 'reset', 'alias']
command = input("Vvedite comandu: ")
# sudo nano file

if any(word in command for word in ignore):
    raise Exception('Invalid command')
print('vse ok!')


