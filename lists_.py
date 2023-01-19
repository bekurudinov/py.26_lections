'Тип данных - List(списки)==========================='



# List - изменяемый тип данных который предсавляет с собой колекцию какой либо посдежвательности

# list_ =[12, 23, True,  False, [12, 'astr'], 'str', None, [12, []]]'=============================

#index y list 

# list_ = [1, 2, 8, 10]

# print(list_[2]) #8
# print(list_[1::2])#[2, 10]

# list_ = [10, 5, 2, 10, [0,0,0,1,0]]
# print(list_[4][3])

'----------------------------------------------------------------'


# str_ = 'helloworld'
# list_= list(str_) # list()- функция
# print(list_) #['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']


# list_ = [1, 2, 3, 4, 5, 20, True, False, None, 'str']
# lists_len =len(list_) # len - функция для подчета элементов
# print(lists_len) #10

'===========================Тип данных -Tuple(кортеж)========================'
#tuple - Неизменяемый тип данных ,являющейся последовательностью элементов ,литералами являются запятые и круглые скобки

# tuple_ =(1, 2, 3, 4)#tuple- круглые скобки
# list_ =[1, 2, 3,4]#list- квадратные скобки
# print(tuple_)
# print(list_)

'========================= Range=============================='

#range(start, end, step) - это генератор последовательности
# в новой версии питона это тип данных

# range_ = range(0, 11)

# print(list(range_)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] list()
# print(tuple(range_))#(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) tuple()


'=====================Циклы(for, while)==========='


#for - это цикл который работает до конца интерируемого обьекта
#while- это цикл который работает пока условие True

# meshok_ = ['potato', 'tomato', 'onion']
# kastrula = []
# for ovoshi in meshok_:
#     kastrula.append(ovoshi)

# print(kastrula)



# for i in range (0,11,2): #0,2,4,6,8,10
#     print(i**2)#0, 1, 4, 9, 16, 25...

# for i in 'makers bootcamp':
#     print(f'Это буква -{i}')







'WHILE'
# i = 0
# while i <= 10:
#     print(f'hello world, это {i} итерация')
#     i+=1


'BREAK, CONTINUE'
#break -  это оператор циклов, который ломает цикл и выходит из нее
#continue- это оператор циклов который пропумкает итерацию

# i = 0
# while True:
#     if i == 5:
#         break
#     print(f'hello world, это {i} итерация')
#     i+=1


# i = 0
# while i<5:
#     i+=1
#     if i == 5:
#         continue
#     print(f'hello world, это {i} итерация')




'------------------------------------------------------------------------------'

# # for i  in range(11):
# #     if i == 5:
# #         break   #ломает цикл и заканивает его когда i == 5
# #     print(f'Это {i} итерация')
    

# for i  in range(11):
#     if i == 5:
#         continue #пропускает итерацию когда i == 5 и продалжает работу цикла
#     print(f'Это {i} итерация')



'===================================Методы list(списков)====================='
# print(dir(list)) #функция для просмотра методов листа


'APPEND()'
#list.append(element)- это метод листов который добавляет указанный элемент в конец листа 


# list_ = []
# for i in range(0, 11, 2):
#     list_.append(i)

# print(list_)


# list_ = []
# for i in range(11):
#     if i % 2 == 0:
#        list_.append(True)
#     elif i == 0:
#         list_.append(None)
#     else:
#         list_.append(False)

# print(list_)
'=========================================================================='


# list_ = [1, 2, 3, True, False, 'Rem']

# list_.append('Anton')
# print(list_)

'=============================================================================='

'EXTEND()'

#list_1.extend(list_2)- Это метод листов который расшираяет первый лист засчет второго листа


# list_1 = [1, 2, 3]
# list_2 = [1, 2, 3]

# list_1.append(list_2) #1,2,3,[4,5,6] - APPEND
# print(len(list_1))
'==========================================================================='
'INSERT()'

#list.insert(index, element) - это метод листов который на место index добавляет element

# list_ = [0,0,0,0,0,0,0,0]

# list_.insert(5, True)

# print(list_) 
'========================================================'

# list_ = [25, 12, 1, 'makers, None, [1, 2, 3, 0, 5, 10]]

# list_[5].insert(5, 'hello')

# print(list_)

'INDEX'

#list.index(element, start, end) - это метод листов который находит индекст указанного элемента


# list_ = ['NYC', 'Moscow', 'SP', 'Bishkek', 'Osh']

# for city in list_:
#     print(f'Город - {city} под индексом {list_.index(city)}')

'====================================================='

'POP'
#list.pop() - это метод листов котрый удаляет  и возрашяет элемент по указанному индексу если индекест  не указать он удалит последний элемент.

# list_ = [1, 2, 3, 12, 123, 43, 12, 4, 5]

# pop_element = list_.pop(3)
# print(list_)
# print(pop_element)
'=============================================='
# list_ = [1, 2, 3, 12, 123, 43, 12, 4, 5]

# pop_element = list_.pop()

# print(list_)
# print(pop_element)
'========================================================'

'REMOVE()'

#list.remove - это метод листов для удаление какого либо элемента если такого элемента нет то выйдет ошибка

'============================================================='
# list_ =[1, 2, 3, 4, 5, 6, 6, 7]
# list_.remove(6)

# print(list_)
'================================================================'
'SORT'
#list.sort(key = len,reverse=True)- это метод листов для сортировки его элементов

# list_ = ['Sultan', 'sanjar', 'Aigerim', 'Erkaym']

# list_.sort(key=len, reverse=False )#True
# print(list_)

'============================================================================'
# list_ = [1,4,5,6,7,8,9,7,]]

# list_.sort(key=len, reverse=False )#True
# print(list_)

'=========================================='
'COUNT'
#list.count(element) - это метод листов который счетает сколько element есть в листе

# list_ = [1, 3, 4, 5, 7, 'hello1' ]

# count_list = list_.count('1') # 2 встречается строка '1' в этом листе
# print(count_list)  #2
'==============================================================================='
'COPY(), DEEPCOPY()'


#list.copy() это метод листов который копирует лист поверхностно
#copy.deepcopy()- это метод листов который копирует лист углубленго


# list_ =[1, 2, 3, 4, 5]

# copy_list = list_.copy()

# print(list_)
# print(copy_list)

'======================================================='
# import copy
# list_1 = [1,2,3,4,5]

# copy_list = copy.deepcopy(list_1)

# print(list_1)
# print(copy_list)

'REVERSE()'
#list.reverse() - это метод который переварачивает лист

# a = {'x': 1, 'y': 2, 'z': 1}
# element = a.clear()
# print(element)
# print()
'Задача'
# if len(lists) == 1:
#     print(f'max_list {lists[0]}')
#     print(f'min_list {None}')
# else:
#     list_of_len = []
#     for x in lists:
#         list_of_len.append(len(x))

#     min_value = min(list_of_len)
#     max_value = max(list_of_len)
#     if min_value == max_value:
#         max_index = list_of_len.index(max_value)
#         print(f'max_list {lists[max_index]}')
#         print(f'min_list {None}')
#     else:
#         min_index = list_of_len.index(min_value)
#         max_index = list_of_len.index(max_value)
#         print(f'max_list {lists[max_index]}')
#         print(f'min_list {lists[min_index]}')



'задача'

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_value = max(lists, key=len)
# min_value = min(lists, key=len)


# if max_value == min_value:
#     print(f'max_list {max_value}')
#     print(f'min_list {None}')

# else:
#     print(f'max_list {max_value}')
#     print(f'min_list {min_value}')