mass_1=[10,25,30,45,50]
mass_2=[]
for i in mass_1:
    if i%2==0:
        mass_2.append(mass_1.index(i))
print(mass_2)