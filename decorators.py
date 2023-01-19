# функция вышего порядка  - это функция котороя в качестве аргумента принимает другую функцию

#Декоратоор - это функция котороя позволяет без изменения кода обернуть другую функцию для того чтобы расширить функционала обернутый функции

# def decorator(func):
#     print(f'Called Func name: {func.__name__}') 
#     return (func)

# def hello():
#     print('Vsem privet!')
#     return 'hello'

# def john():
#     print('Hello my name is John Snow!') #4
#     return 'John Snow' # 5


# # hello()
# # john()
# a = decorator(hello) #1
# b = decorator(john)
# print(a, b)

# from typing import Callable

# def benchmark(func: Callable):
#     import time
#     start = time.time()
#     res = func()
#     finish = time.time()
#     print(f'Время выполнения функции {func.__name__}: заняло {finish - start}')
#     return (res)


# def loop():
#     i = 1
#     range_number = 100_000
#     while i <= range_number:
#         # print(i)
#         i += 1
#     return i
# print(benchmark(loop))



# users = ['Nurkamila']

# def login_required(post):    # post
#     def wrapper(user, post_):   # user, post_
#         if user in users:
#             return post(user, post_)
#         else:
#             return 'There is no such user'
#     return wrapper


# @login_required
# def post(user, post_):
#     return 'Succesfully posted'

# print(post('Nurkamila', 'cakes'))


lang = 'en'

if lang == "en":
    print('This is english')
elif lang == "ru":
    print('Это русский')
elif lang =='de':
    print('Das ist Deutsch')
elif lang == 'kg':
    print('Бул кыргыз тили')