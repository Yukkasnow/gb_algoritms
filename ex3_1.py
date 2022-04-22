result1=[]
result2=[]
numbers=range(2,10)
for n in numbers:
    result1=[]
    for i in range(2, 100):
        if i%n==0:
            result1.append(i)
    print(f'{len(result1)} чисел деляться на {n}\nвот эти числа {result1}')

