
texto = "Universidad Tecnologica de Leon"

print(texto.lower())#Minusculas
print(texto.upper())#Mayusculas
print(texto.title())
print(texto.find("de"))#Es como contain
print(texto.count("e"))#Cuenta el caracter como parametro

textoNuevo = texto.replace("e", "4")
print(textoNuevo)