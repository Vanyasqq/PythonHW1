# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

LongChocolate = int(input('Длина шоколадки (в дольках):'))
WidhChocolate = int(input('Ширина шоколадки (в дольках):'))

TheFault = int(input('сколько хотите отломить?:'))

if (TheFault % LongChocolate == 0) or (TheFault % WidhChocolate == 0):
    print('у вас получится')
else:
    print('за один разлом не выйдет')

