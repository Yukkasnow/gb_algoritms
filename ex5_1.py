companies=[]
number=1
while number<=4:
    companies.append(input(f' Введите название {number} компании и прибыль за каждый квартал через пробел').split( ))
    number+=1
print(companies)
summ=0
comp_inpt=0
for company in companies:
    quater_1 = int(company[1])
    quater_2 = int(company[2])
    quater_3 = int(company[3])
    quater_4 = int(company[4])
    summ=quater_1+quater_2+quater_3+quater_4+summ
ave_input=summ/4
print(f' средняя прибыль за год всех компаний: {ave_input}')

for company in companies:
    inp=0
    comp_inpt=0
    for inp in company[1:5]:
        inp=int(inp)
        comp_inpt=comp_inpt+inp
    ave_inp=comp_inpt/4
    print(ave_inp)
    if ave_inp<ave_input:
        print(f'У {company[0]} прибыль ниже среднего')
    else:
        print(f'у {company[0]} прибыль выше среднего')

