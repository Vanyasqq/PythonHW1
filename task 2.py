# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


def ParsingTheNumber():
    num = str(input('число:'))
    r= range(len(num))
    num = int(num)
    sum = 0
    for i in r:
        conclusion = num % 10
        num = num// 10
        print(conclusion, end=' ')
        sum = sum + conclusion
    print('=',sum)

ParsingTheNumber()

