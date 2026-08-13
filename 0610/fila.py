n = int(input())
h = (input().split())

i = n - 1
maior = int(h[i])
i -= 1
cont_cola = 0
while (i>=0):   
    elem = int(h[i])
    if (elem > maior):
       cont_cola += 1
print(cont_cola)        