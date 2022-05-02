#Для анализа был взят алгоритм из 3 домашнего задания, номер 1
import time
# start=time.time()
# result1=[]
# result2=[]
# numbers=range(2,10)
# for n in numbers:
#     result1=[]
#     for i in range(2, 1000000):
#         if i%n==0:
#             result1.append(i)
#     print(f'{len(result1)} чисел деляться на {n}')
#
# print(time.time()-start)
#сложность алгоритма О(n),
# при 100к чисел в последовательности алгоритм выполняется за 0,18с,
# при длине ряда в миллион чисел за 1,6с

start=time.time()
div_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
max_number=100000
for num in range(2, max_number):

    if num % 2 == 0:
        div_dict[2] += 1

    if num % 3 == 0:
        div_dict[3] += 1

    if num % 4 == 0:
        div_dict[4] += 1

    if num % 5 == 0:
        div_dict[5] += 1

    if num % 6 == 0:
        div_dict[6] += 1

    if num % 7 == 0:
        div_dict[7] += 1

    if num % 8 == 0:
        div_dict[8] += 1

    if num % 9 == 0:
        div_dict[9] += 1

print(div_dict)
print(time.time()-start)
#данный алгоритм также сложности О(n) и выполняется чуть быстре на 10к чисел за 0,1с, на миллионе за 1,1с,
# возможно это связано с принтом и тем, что в первом алгоритме 2 цикла for