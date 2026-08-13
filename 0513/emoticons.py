texto = input()

sorrisos = texto.count(":-)")
triste = texto.count(":-(")
 
if sorrisos == triste:
    print("neutro")
elif triste > sorrisos:
    print("chateado")
else:
    print("divertido")    
