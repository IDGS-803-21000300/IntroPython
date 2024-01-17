

n1 = int(input("Escribe un Numero  "))
n2 = int(input("Escribe otro Numero  "))

if n1 > n2 : 
    print("El {} es mayor que el {}".format(n1, n2))
else:
    print("El {} es mayor que el {}".format(n2, n1))

print("---------------- dame una edad ----------------")
edad = int (input("ingresa tu edad"))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes los 18")
else:
    print("Eres menos de edad")