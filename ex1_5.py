lettter1=ord(input('Введите первую букву').upper())
lettter2=ord(input('Введите вторую букву').upper())
index_1=lettter1-64
index_2=lettter2-64
btw_letters=index_2-index_1
print(f'Первая буква находится на {index_1} месте \n'
      f'Вторая буква находится на {index_2} месте\n'
      f'Между ними {btw_letters} букв')