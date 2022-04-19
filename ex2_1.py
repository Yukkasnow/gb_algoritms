
while True:
    operator = input('Введите оперотор, если вы хотите выйти, введите 0(ноль)')  # +-*/
    if operator=='0':
        print('end')
        break
    number_1 = int(input('Введите первое число'))
    number_2 = int(input('Введите второе число'))
    if operator== '+':
        result=number_1+number_2
        print(f'Результат сложения {number_1} и {number_2}: {result}')
    elif operator=='-':
        result=number_1-number_2
        print(f'Результат вычитания {number_1} и {number_2}: {result}')
    elif operator=='*':
        result=number_1*number_2
        print(f'Результат умножения {number_1} и {number_2}: {result}')
    elif operator=='/' and number_2!=0:
        result=number_1/number_2
        print(f'Результат деления {number_1} на {number_2}: {result}')
    elif operator=='/' and number_2==0:
        print('Делить на ноль нельзя!')
    else:
        print('Вы ввели неверный знак операции')


