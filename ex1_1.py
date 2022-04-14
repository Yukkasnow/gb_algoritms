number=int(input('Введите трехзначное число'))
a=(number-number%100)//100 #сотни
b=(number//10)%10 #десятки
c=number%10 # единицы
summ=a+b+c
composition=a*b*c
print(f'сумма чисел {summ}, Произведение чисел {composition}')