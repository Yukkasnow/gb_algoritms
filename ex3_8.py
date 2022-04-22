str_1=input('Введите элементы первой строки через пробел').split()
str_2=input('Введите элементы второй строки через пробел').split()
str_3=input('Введите элементы третьей строки через пробел').split()
str_4=input('Введите элементы четвертой строки через пробел').split()
str_5=input('Введите элементы пятой строки через пробел').split()

def summ(strr):
    summ=0
    for i in strr:
        i=int(i)
        summ+=i
    strr.append(summ)
    return strr

print(f'{summ(str_1)}\n{summ(str_2)}\n{summ(str_3)}\n{summ(str_4)}\n{summ(str_5)}')