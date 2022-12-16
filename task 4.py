# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

S = 24


#коэффицент скорости оригами относительно друг друга
SergeyСoefficient = 1           
PetrСoefficient = SergeyСoefficient
KateСoefficient = (SergeyСoefficient + PetrСoefficient) * 2     

#общий коэфицент скорости оригами)))00)
TotalСoefficient =  KateСoefficient + PetrСoefficient + SergeyСoefficient  

#Общая Скорокость создания журавлика за условную единицу времни
СranesPerSecond = S / TotalСoefficient

#подсчет результата каждого 
Sergey = СranesPerSecond * SergeyСoefficient
Petr = СranesPerSecond * PetrСoefficient
Kate = СranesPerSecond * KateСoefficient

print('{}-> {} {} {}'.format(S,Sergey,Petr,Kate) )
