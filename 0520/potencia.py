n = int(input())
ter = 0
for i in range(n):
    T = int(input())
    x = T //10
    y = T %10
    ter += x ** y

print(ter)    