import random

# 10-10-1 20-10-2 30-10-3
cont = ''
light = 0
for i in range(120):
    # cont += f'{i*10}-10-1 '
    if i % 2 == 0:
        cont += f'{i*10}-10-1 '
    else:
        cont += f'{i * 10}-10-0 '
print(cont)