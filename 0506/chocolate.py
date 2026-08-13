#total = int(input())
#for i in range(total):
    #chocolates.append(int(input()))                   

chocolates = [8, 5, 10, 2, 5, 10, 4]

chocolates.sort()
pos = 2
while(pos<len(chocolates)):
    pos += 2
    chocolates.pop()


acum = 0;
for i in range(len(chocolates)):
    acum += chocolates 


print(chocolates)
