# ile <expression>:
#     <body>wh

# i = 0
# while i < 10:
#     i += 1
#     print(f'цикл выполнился {i} раз!')


# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' or name2.lower() != 'raychel':
#     name1 = input('Vvedite imya1: ')
#     name2 = input('Vvedite imya2: ')
#     i += 1
#     if i >= 5:
#         print('цикл остановлен')
#         break
#     else:
#         print('Vy vveli pravil\'noe imaya!')
#====================================================================
# 'Моржовый опертор'

# user = {'username': 'John', 'password': 'i lovepython123'}
# i = 3
# # password = None
# while (password := input(f'{user["username"]}) vvedite parol\':') != user ['password']):
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany na 5 dney! ')
#         break

# else:
#     print(f'{user["username"]} vy uspeshno zahli v sistemu!')
#===========================================================
# for <variable> in <iterable object>:
    #<body>

# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_[::-1])
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# import random
# ls = []
# for x in range(1, 101):
#     ls.append(random.randint(1, 1000))
# print(ls)
# ls.sort()
# res = []
# for x in ls:
#     if x % 2 == 0:
#         res.append(x)

# print(res)

# # 100
# 1,
# 2, 4, 5, 10,


x  = 100

res = [1, x]
for i in range(2, int((x ** 0.5) +1)):
    if x % i == 0:
        res.extend({i, x // i})
res.sort()    
print(res)