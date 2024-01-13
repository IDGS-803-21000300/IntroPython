
'''
    Las Tuplas son Inmutables 

    Son como arreglos pero donde reciben muchos tipos de valores
'''

tupla = ("uno", "dos", "tres")
print(tupla)

tuplaVariosDatos = (12, True, 23.5, "El gato", 12+2j)
print(tuplaVariosDatos)

tuplasConTuplas = (1, 2, 3, 4(1, 2, 3, 4))
print(tuplasConTuplas)
print(tuplaVariosDatos[3])
print(tuplaVariosDatos[-2])
print(tuplaVariosDatos[0:2])

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaNueva = tupla + tuplaVariosDatos
print(tuplaNueva)