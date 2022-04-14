import random

def compare(a,b):
    if a>b:
        raise 'Левая граница больше правой'
    else:
        return

cel_gran1=int(input('Введите левую границу случайного целого числа'))
cel_gran2=int(input('Введите правую границу случайного целого числа'))
vesh_gran1=float(input('Введите левую границу случайного вещественного числа'))
vesh_gran2=float(input('Введите правую границу случайного вещественного числа'))
simb_gran1=input('Введите левую границу случайного символа')
simb_gran2=input('Введите правую границу случайного символа')

compare(cel_gran1,cel_gran2)
rand_cel=random.randint(cel_gran1,cel_gran2)
print(f'Ваше случайное целое число {rand_cel}' )

compare(vesh_gran1,vesh_gran2)
rand_vesh=random.uniform(vesh_gran1,vesh_gran2)
print(f'Ваше случайное вещественное число {rand_vesh:.2f}')

simb_gran1=ord(simb_gran1)
simb_gran2=ord(simb_gran2)
compare(simb_gran1,simb_gran2)
rand_symb=chr(random.randint(simb_gran1,simb_gran2))
print(f'Ваше случайный символ {rand_symb}')