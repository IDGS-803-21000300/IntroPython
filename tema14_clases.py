
class OperasBas:
    
    #DECLARACION DE PROPIEDADES

    num1 = 0
    num2= 0
    num3 = 0

    #DECLARACIOM DEL CONSTRUCTOR

    def __init__(self, a, b) :
        self.num1 = a
        self.num2 = b

    #DECLARACION DE METODOS DE CLASE
        
    def suma(self) : 
        self.res = self.num1 + self.num2
        print("la suma es: {}".format(self.res))

def main():
    obj = OperasBas(3, 4)
    obj.suma()

if __name__ == "__main__" :
    main()