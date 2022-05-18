import sys
 #lesson 1 ex5
# lettter1=ord(input('Введите первую букву').upper())
# lettter2=ord(input('Введите вторую букву').upper())
# index_1=lettter1-64
# index_2=lettter2-64
# btw_letters=index_2-index_1
# print(f'Первая буква находится на {index_1} месте \n'
#       f'Вторая буква находится на {index_2} месте\n'
#       f'Между ними {btw_letters} букв')
#print(sys.getsizeof(lettter1), sys.getsizeof(lettter2), sys.getsizeof(index_1), sys.getsizeof(index_2), sys.getsizeof(btw_letters))
#даная программа занимает 140 байт

#lesson 2 ex6
# import random
#
# answer=random.randint(0,100)
# user_try=0
# max_count=10
#
# while user_try!=max_count:
#     user_try+=1
#     user_answer=int(input('Введите число от 0 до 100 '))
#     if user_answer==answer:
#         print('Поздравляю, вы угадали')
#         break
#     elif user_answer<answer:
#         print('Вы не угадали, число меньше загаданного')
#     elif user_answer>answer:
#         print('Вы не угадали, число больше загаданного')
# if user_try==max_count:
#     print(f'Вы проиграли, правильный ответ {answer}')
#данная программа использует 84 байта памяти

mass=[1,2,8,8,6,7,7,9,3,3,4,8,5,1,8,6,8]
print(mass)
total=0
for m in mass:
    count=mass.count(m)
    if count>total:
        total=count
        max_number=m
print(f'{max_number} встречается {total} раз')
print(sys.getsizeof(mass),sys.getsizeof(total),sys.getsizeof(count),sys.getsizeof(max_number))
#данная программа занимает 300 байт памяти, пространственная сложность О(n)

