# sentence = input('Vvedite predlojeniye: ')

# if sentence[-1] == '?':
#     print('Voprositel\'noe predlojeniye!')
# else:
#     print('Normal one!')

# print('Voprositel\'noe predlojeniye!' if sentence[-1] == '?' or sentence[-2:] == '?!' else 'Normal one!')
'-----------------------------------------------------------------------------------'

# Ternery operators(Тернарный оператор) - это конструкция, которая аналогична по-своему действию  конструкции if\else, но при этом записывается в одну строчку

# number = 21
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)

# <выражение если в условии True> if <условие> else <выражение если в условии False>

# num = int(input('Vvedite chislo: '))

# res = num -100 if num <100 else num * 2
# print(res)

ls = [55, 65, 75, 89, 100, 15, 6]
print(ls)
choice = input('Vvedite max/min: ')

res = max(ls) if choice.lower().strip() == 'max' else min(ls)
print(res)









































# Ternary operators (Тернарный опретор ) - это констурция которая аналогична по своему действию конструкции if/else но при этом записывется в одну строку 




# number = 18
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)


# <выражение если в условии True > if <условие > else <выражение в условии False>

# num = int(input('Vvedite chislo: '))
# res  = num - 100 if num < 100 else num *2
# print(res)


ls = [55, 65, 75, 89, 100, 15, 6]
print(ls)
choice = input('Vvedite max/min: ')

res = max (ls) if choice.lower().strip() == 'max' else min(ls)
print(res)