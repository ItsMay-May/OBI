lista_n = []
num_lista=[]
a = input().split(" ")
n= int(a[0])
f = int(a[1])

for i in range(n):
    data=(input())
    lista_n.append(str(data))
    
    

for num in lista_n: 
        x = f
        while (x >= 0):
            num = num.replace ( str(x) ,"*")
            x = x - 1
        num_lista.append(num)    

for num in num_lista:
     print(num)
