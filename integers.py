# Типы данных числа -> int, float

# = -> оператор присваевание 
#variable(переменная) - это именнованная ячейка в памяти в который хрянятся данные и к мы можем обратитсья через имя перенной

# num = 5
# print(num)
# num = 51
# print(num)



# abc -> Нижний регистр
# ABC -> Верхний регистр


#PEP8
#tommorow_day = '15.12.2022' #Snake case
#tommorowDay = '15.12.2022' #Camel case

#+
# num1 = 5
# num2 = 15
# result = num1 + num2
# print(result)


# num1 = 100
# num2 = 105
# num3 = 500 #int
# num4 = 54.55 #float
# print(num1 + num2 + num3 + num4)
# #type ()функция для просмотра типа даных в переменной

# str1 = 'hello'
# print(type(str1))


# -
# print('Result:',996 - 67.98)

# num1 = input('Enter the number1: ')
# num2 = input('Enter the number2: ')
# print(type(num1), type(num2))
# num1 = int(num1)
# num2 = int(num2)
# print(type(num1), type(num2))
# result = num2 - num1
# print(result)

# *
# print('Result: 505 * 240000 =', 505 * 240000)

#/ and // and %
# / ->обычное деление
# // ->деление без остатка
# % ->модульное деление 

# num1 = 7 
# num2 = 3
# print('/' , num1 / num2)
# print('//' , num1 // num2)
# print('%' , num1 % num2)

# ** -> возведение числа
#print(5 ** 2)




#==================================================================
'Методы строк'

#print(dir(str))  # список методов

'REPLACE'
# str.replace(старая значение,новое значение,кол-во,это метод строк ,который меняет старое значение на новое,если указать количество то поменяет столько сколько раз мы указали)

# text = 'ha ha ha ha'
# result = text.replace('a', 'o', 2)
# print(result) 


'STRIP'
#str.strip() - метод строк,который убирает пробелы в начале и в конце строки 


# text = '   hello world    '
# result = text.strip()
# print(result) #           hello world
# print(result)#hello world

# print(len(text))
# print(len(result))
#=====================================================
#str.rstrip()- убирает пробелы с права(в конце)

# text = '           hello world          '
# print(len(text.rstrip)) #'     hello world'
#=====================================================
#str.lstrip()- убирает пробелы слева(в начале)

# text = '      hello world    '
# result = text.lstrip() # убирает все пробелы
# print(result) #'hello world    '
# print(len(result)) #15

'ISDIGIT,ISNUMERIC,ISDECIMAL'
#str.isdigit()
#str.isnumeric()   - это методы строк которые проверяют является ли  наша строка полностью чисел
#str.isdecimal()

# text = '25'
# print(text.isdigit)
# print(text.isdecimal)
# print(text.isnumeric)

# age = input('введите свой возраст:')
# print(age.isdigit())   #True


'ISALPHA'
#str.isalpha() - это метод строк который проверяет состоит ли наша строка только из символов

# text = 'bjsdhfvv hvhvvvvvv'
# print(text.isalpha())  #false, это так как пробел это не кирилца или латиница

# text = 'bjsdhfvvhvhvvvvvv'
# print(text.isalpha())#true, так вся строка состоит из латиницы



'ISALNUM'

#str.isalnum() - это метод которыйй проверяет на то что состоит ли наша строка из чисел и симвалов латинского или кирильского алфавита

# text ='ahchb25'
# print(text.isalnum())  #true, так как строка состоит из латиницы

# text_2='ahchb25  24*/'
# print(text_2.isalnum()) #false, так  как есть символы(пробелы,плюс,равно и.т.д) 


'ISLOWER,ISUPPER'
#str.islower-метод строк который проверяет на нижний регистр(с маленькой буквы)
#str.isupper-метод строк  котрый проверяет на верхниий регистр(с большой буквы)


text = 'makers'
print(text.islower()) #true
print(text.isupper()) #false

'ISTITLE'
#str.istile - проверяет этот метод строк начинается ли каждый слово в строке с верхнего регистра(с большой буквы)

# name = 'sultan talaibekov'
# name2 ='Sultan Talaibekov'
# print(name.istitle()) #false
# print(name2.istitle()) #true



'INDEX'
#str.index(values, start, end) - это метод строк который возрашает индекст заданного значение(values)

# text = 'djgkjkgdhgkjkjg'
# print(text.index('k')) #3

# text = 'makers bootkamp'
# print(text.index('a', 7)) #12 , ишет в слове  bootkamp


'COUNT'
#str.count(|values, start) - метод строк который считает сколько у нас значение (values,) есть в строке
# text = 'codingiseasy'
# print(text.count('i')) #2 начинает искать от начало до конца
# print(text.count('i' , 5))#1 начинает искать с 5 го до конца
# print(text.count('i', 5, 9))#1 начинает 5 индекса до 9 го

'FIND'
#str.find-это метод строк такой же как и метод строк str.index(смотрите выше) но он не выведет ошибку если значения (values)нету в строке он просто вернет индекст -1.

# text = 'makers bootkamp'
# print(text.find('z')) #распечатает-1

# text = 'makers bootkamp'
# print(text.index('z')) # распечатает (not found)


'SWAPCASE'
#str.swapcase- этот метод строк который меняет противополжнный регистр (a->A), (A->a),   (makers)->(MAKERS),(MAKERS)->(makers)

# text = 'codiniseasy'
# print(text.swapcase()) #CODINGIEASY

# text2 ='CODINGIEASY'
# print(text2.swapcase())#codingieasy


'CAPITALIZE'
#str.capitalize- это метод строк который меняет первую букву строки на верхний регистр , остальные нижний 

# text = 'hi my name is Anton'
# print(text.capitalize()) #'Hi my name is Anton'

'TITLE'
#str.title() - это метод строк который переводит начало каждого слово с строке в верхний регистр

# text = 'hi my name is ghustaph'
# print(text.title()) # 'Hi My Name Is Ghustaph'

'SPLIT'
# #str.split()- это метод строк который строку переводит в лист при помощи разделителя
# text = 'hi my name is Sultan'
# print(text.split())


'JOIN'
#'соединитель'.join(list)- это метод строк который соединяет элементы листа

# list_= ['12', '23', '54', '25']
# print(' '.join(list_))

#=============================================================================================















