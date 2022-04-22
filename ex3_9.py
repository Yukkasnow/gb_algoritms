matrix=[[5,8,10,12],
        [10,12,18,25],
        [16,20,23,6]]
stroka=len(matrix)
stolb=len(matrix[0])
max_el=0
for n in range(stolb):

    min_el=None
    for m in range(stroka):
        elmnt=matrix[m][n]
        if min_el==None:
            min_el=elmnt
        elif elmnt<min_el:
            min_el=elmnt

    if min_el>max_el:
        max_el=min_el
print(max_el)