row = ''
table = ''
for char in range(32, 128):
    row += '{}:{}\t'.format(char, chr(char))
    if not (char - 31) % 10:
        table += '{}\n'.format(row)
        row = ''
table += '{}\n'.format(row)
print(table)

