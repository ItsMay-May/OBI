a = int(input())
s = int(input())
d = int(input())

i = 0
dist = 0

while (True):
    i+=1
    dist += s
    if dist >= a:
        print(i)
        break
    dist-=d


#sss = (a-que)
#print(sss)

 
#b = (a/que)
#print (b)