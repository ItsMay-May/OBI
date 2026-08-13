t  = int(input())
n = int(input())

cities = []

for i in range (n):
    dist = int(input())
    cities.append(dist)
cities.sort()

menor_vis = (cities[1] - cities[0])/2 + cities[0]

for i in range(1, n-1):
    if(i==n-1):
        vis = (t - cities[i]) + (cities[i] - cities[i -1 ])/2
    else:
        vis  = (cities[i+ 1] - cities[i- 1]) /2
    if vis < menor_vis:
        menor_vis = vis
print(f"{menor_vis:.2f}")
            
        



