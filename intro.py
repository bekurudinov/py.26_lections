#типы данных в питоне

#1.none type - ничего пустота->
#2.Boolean - истина или ложь->True/False
#3.str() -> Строки->"Hello world", 'hello world'
#4.Числовые типы данных 
#  a) integer - int() - целое число -> -1, 2, 555
#  b) float() - Число с плавающей точкой- >1.5 , 15.2
#  c) complex() - 3+5i6
#5.Списковые типы даных (колекция)
   #a. list(массив/список) -> [1, 2, 3]
   #b. tuple(кортеж)->(1, 2 , 3,None)
   #c. ranger(последовательность)->range(1, 10)
#6.set() -> множества -> {1,2,3,4,5,6,8,}
#7.dict(словари) -|> содержат данные в себе в виде ключа и значения {1: 'one', 2: ' two'}  


# ***********************************************


#Mutable(изменяемые типы данных)
#1.list
#2.set
#3.dict
#immutble(неизменяемые типы данных)
# 1.nonetype
# 2. boolean
# 3. int,float,complex
# 4.str
# 5.range
# 6.tuple
# 7.froxenset

#***********************************************************************

num= 5
stroka = 'hello world! my name is john!'

#'''Стандартный вывод данных'''

#в пайтоне для вывода данных в терминал используя встроенная функция print()

stroka = "hello world! my name is john snow!"
print(stroka)
print(27+5)


"""
стандартный ввывод данных через терминал
используется функция input()
"""

# a = input('Введите число:')
# print(a)


' Типы данных Строки'




'Строки это(str) набор последователтных сималов которые мы используем для хранения и представление текстовой информации'
 


#=========================================================================================

'срезы'

'Срезы по исндексам это когда мы получаем оперделенную часть строки при помощи индексов'

# name = 'john'
# '       0123'

# print(name[3])

# 'Срезы [start , end, step]'
# start  - начало среза начальный индекс по умолчанию стоит 0
# end - конец среза конечный индекст который не включает по умолчанию берет до конца
# step - шаг среза который указывает через сколько элементов проходиться по умалчанию стоит 1

# name = 'john snow man'
# snow_1= name[5:9] #snow
# snow_2= name[5:]
# print(snow_1)
# print(snow_2)

# john = name[0:4]
# print(john)


# name = 'john snow man'

# Step_2  = name[0:13:2]
# Step_3  = name[0:13:3]

# print(Step_2)
# print(Step_3)



# print(name[0:13:2])#john snowman ->jh nwmn



# name = 'john Snow man'
# reversed_name = name[::-1]
# print(reversed_name)

# name = 'john Snow man'
# reversed_name_naM= name[12:9:-1]
# reversed_name_wnoS = name[-8:-4]
# print(reversed_name_naM_)
# print(reversed_name_wnoS_)
#==================================================
# склейивание строки (конкатенция)

# first_name = 'sultan'
# second_name = 'taalaibekov'
# full_name = first_name + ' ' +second_name
# print(full_name)

# print(full_name*2) 
#===================================================
#форматирование строк
'''
1) с помощью %
2) с помощью ( . format())
3) интерполяция строк(f'строка')
'''

# 1) %s

# name = input('ВВедите свое имя: ')
# print('привет меня зовут ', name)
# print('привет меня зовут' + ' ' + name + ' ' + 'talaibekov')
# print('привет меня зовут %s talaibekov' %(name))

# 2).format


# name = input('Введите свое имя: ')
# age = 25
# result = 'привет , мое имя {}, мне {} лет'.format(name,age)
# print(result)

# 3)f'строки

# name = input('введите свое имя: ')
# age = 31
# result = f'привет мое имя {name} мой возраст - {age} год'
# print(result)

#============================================================
# Экранирование строк
# \n - перенос строки
# \t-гортзантальная тобуляция
# \v-вертикальная табуляция


# print('hello world\nmy name is anton')
# print('hello world\n\tmy name is bek')
# print('hello world\vSup')
# print('hello world\n\tSup')





