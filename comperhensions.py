# list  -> 0 : 200-> num % 2 == 0

# ls  = list (range (0, 200,2))
# print(ls)


# list -> 0: 300 -> num % 2 == 0 and num % 3 == 0
# ls = []
# for x in range (0, 300):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)


# print(ls)


# # ls = []
# for x in range (0, 100):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     else:
#         ls.append(x)

# print(ls)


#======================================================================================
'List comperehensions' 
#генераторы списков , упрощенный подход к созданию списков , который  задействует цикл for ,  атак же коснтрукции  if else для оперделение условий в генерации



# ls = [x for x in range (0, 200) if x % 2 == 0]
# print(ls)


# 1)ls = []
# for x in range (0, 300):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)

# print(ls)


# 2)ls = [x for x in range (0, 200) if x % 2 == 0 and x % 3 == 0]
# print(ls)


#===============================================================================
#ls = []
# for x in range (0, 100):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     else:
#         ls.append(x)

# print(ls)

# ls = [x ** 2 if x % 2 == 0 else x for x in range(0, 100)]
# print(ls)


# ls = [x ** 2 for x in range (1, 11)]
# print(ls)


# ls = [x ** 3 if x % 2 != 0 else x + 100 for x in range (1, 11)]
# print(ls)




# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = [x + 10 if x % 2 == 0 else x** 2 for inner  in ls for x in inner]
# print(result)





# from datetime import datetime
# from time import sleep

# start = datetime.now()
# print(start)
# sleep(5)
# finish = datetime.now()
# print(finish)
# print(finish - start)



# from datetime import datetime
# ls = []
# for x in range(1, 10000):
#     ls.append(x)
# finish = datetime.now()
# print(finish - start)


# fruits = ['apple', 'banana', 'kiwi', 'mango', 'limon', 'mandarin']

# ls = [x for x in fruits if x != 'apple']
# print(ls)

# ls = [x for x in fruits if not x.startswith('m')]
# print(ls)

#=========================================================
#Множества
# a = {x for x in range (0, 11)}
# print(a)
# print(type(a))
#========================
#Dict 
# dict_ = {x: x ** 2 for x in range(1, 15)}
# print(dict_)


dict1 = {'a': 1, 'b':2, 'c':3, 'd':4,'e':5, 'f':6, 'g':7, 'h':8}
#'a': 'odd', 'b': 'even'

new_dict = {k: 'odd' if v % 2 != 0 else 'even' for k, v in dict1.items()}
print(new_dict)