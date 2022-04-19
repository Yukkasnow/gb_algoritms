number_range=input('Введите поседовательность цифр ')
find_number=input('Ввведите цифру количество которой вы хотете посчитать ')
i=0
for num in number_range:
    if num==find_number:
        i+=1
print(f'{find_number} встречается {i} раз')