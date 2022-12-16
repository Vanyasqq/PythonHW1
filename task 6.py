# Задача 6
# Вы пользуетесь общественным транспортом?
#  Вероятно, вы расплачивались за проезд и получали билет с номером.
#  Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no


# проверка корректности номера билета
def TicketValid(x):
    if len(x) % 2 == 0:
        return True
    return False


NumberTicket = input('номер билета:')
NumLen = len(NumberTicket)

if TicketValid(NumberTicket) == False:
    print("не корректный номер билета")  
#на случай если в билете меньше или больше 6ти цифр))
else:
    sum1 = 0
    sum2 = 0
    
    for i in range(0, NumLen//2):
        sum1 = sum1 + int(NumberTicket[i])
    for i in range(NumLen//2, NumLen):
        sum2 = sum2 + int(NumberTicket[i])
    if sum1 == sum2:
        print("блиет счтастливый")
    else:
        print('билет не счастливый')








