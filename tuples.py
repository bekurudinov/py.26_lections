#tuple()-> кортеж,неизменяемый тип данных

# thistyple = (6,)
# print(thistyple)
# print(type(thistyple))

# mytyple = ('apple', 'pineapple', 'pan')
# print(mytyple)
# print(type(mytyple))


# for x in range(1, 5): #1) x = 1
#     print(x)          #2) x = 2

#Пример
# dict1 = {1: 'one', 2: 'two', 3:'Three'}
# print(dict1.items())
# for x, y in dict1.items(): #1) x = 1 y ='one'
#     print(x, y)



#Пример 2
# a = [ (1, 2), (3, 4), (5, 6)]
# for x, y in a:
#     print(x, y)

# ls = list(range(1, 100_001))
# tp = tuple(range(1, 100_001))
# print(ls)
# print(tp)
# print('LIST', ls.__sizeof__())
# print('TUPLE', tp.__sizeof__())

# tuple_ =(1,2,3,4,5)
# ls = [1,2,3,4,5]
# del tuple_[-1] # не изменяемый
# print(tuple)


# tuple_= (1,2,3,4,5,6,7,8,2,2,2,2,2,2)
# print(tuple_.index(5))
# print(tuple_.count(2))         




# tp = ('apple', 'cherry', 'banana', 'john')
# for x in tp:
#     print(x)
#     print(x * 3)





# i = 0

# while i<50:
#     print(i)
#     i += 1 #инкримент i = i +1
#            #дикримент i -=1




# tp = ('apple', 'cherry', 'banana', 'john')
# x = 0
# while x < len(tp):
#     print(tp[x], f'index: {x}')
#     x += 1

# + *




# 1) input
# tp = (1,8,3,4,5,8,8,9,2)
# target = 8
# #output:result(8,3,4,5,8) 

# #2) input
# tp = (1,2,3,8,5,1,2)
# target = 8
# output: result = (8,5,1,2)

# tp = (1,8,3,4,5,8,8,9,2)
# target = 8
# result = ()
# for result in tp[1:6]:
#     print(result)

# tp = (1,8,3,4,5,8,8,9,2)
# target = 8

# if tp.count(8) > 1:
#     first = tp.index(8)
#     second = tp.index(8, first+1)
#     result = tp[first: second + 1]
# else:
#     first = tp.index(8)
#     result = tp[first:]

# print(tp, target)
# print(result)


# nums = [2,7,11,15]
# target = 9
# result = []
# first =(nums.index[2])
# second =(nums.index[7])
# result = target-nums
# result = target+nums
# print(result)

# nums = [2,7,11,15]
# target = 9


# for x in nums:
#     num = target -x
#     if num in nums:
#         print(nums.index(x), nums.index(num))
#         break




