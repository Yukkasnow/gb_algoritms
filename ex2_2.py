num=input('Введите число')
even=0
odd=0
for n in num:
    if int(n)%2==0:
        even+=1
    else:
        odd+=1
print(f'в числе {num} {even} четных и {odd} нечетных чисел')