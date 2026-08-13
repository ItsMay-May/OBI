s = int(input())
a = int(input())
b = int(input())

cont = 0 

for i in range(a , b + 1):
    num = str(i)
    tam = len(num)
    list = []
    for j in range(tam):
        list.append(int(num[j]))
    
    if(sum(list)==s):
        cont+=1

print(cont)