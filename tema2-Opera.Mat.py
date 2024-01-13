
num1 = 23
num = 3

print("La suma es :", int(num1 + num))
print("La resta es :", int(num1 - num))
print("La multiplicacion es :", int(num1 * num))
print("La division exacta es :", int(num1 // num))
print("La division es :", int(num1 / num))
print("La potencia es :", int(num1 ** num))

# Concatenacion en python

texto1 = "Hola"
texto2 = "Mundooooo"
textoFinal = texto1 + "  " + texto2
print(textoFinal)

##Asignar valores dentro de la cadena por medio de parametros

print("El saludo es : %s %s" %(texto1, texto2))
saludoFinal = "Saludo {} {}".format(texto1, texto2)
print(saludoFinal)

saludoFinal2 = "Saludo 2: {y} {x}".format(x = texto1, y = texto2)
print(saludoFinal2)