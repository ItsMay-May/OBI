vitorias = 0

 #se vence >5 = grupo 1
 #se vence 3 or 4 = grupo 2
 #se vence 1 or 2 = grupo 3
 # se nao vence nada, ta fora!
p1 = input()
p2 = input()
p3 = input()
p4 = input()
p5 = input()
p6 = input()


if p1.upper == "V":
    vitorias = vitorias + 1
elif p2.upper == "V":
    vitorias = vitorias + 1
elif p3.upper == "V":
    vitorias = vitorias + 1
elif p4.upper == "V":
    vitorias = vitorias + 1
elif p5.upper == "V":
    vitorias = vitorias +1
elif p6.upper == "V":
    vitorias = vitorias +1
 
print (vitorias)

  
