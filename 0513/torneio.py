
resultado = 0

for i in range(6):
    win = input()   
    if win == 'V':
        resultado += 1


if resultado >= 5:
    print(1)
elif resultado >=3:
    print(2)
elif resultado >= 1:
    print(3)
else:
    print(-1) 

 