import random

answer=random.randint(0,100)
user_try=0
max_count=10

while user_try!=max_count:
    user_try+=1
    user_answer=int(input('Введите число от 0 до 100 '))
    if user_answer==answer:
        print('Поздравляю, вы угадали')
        break
    elif user_answer<answer:
        print('Вы не угадали, число меньше загаданного')
    elif user_answer>answer:
        print('Вы не угадали, число больше загаданного')
if user_try==max_count:
    print(f'Вы проиграли, правильный ответ {answer}')


