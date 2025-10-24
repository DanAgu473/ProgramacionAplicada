class Calculadora:
    def __init__(self, val=0):
        self.val = val

    def sum(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            return "Error: Solo se permiten números"
        self.val = a + b
        return self.val

    def rest(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            return "Error: Solo se permiten números"
        self.val = a - b
        return self.val
    
    def mult(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            return "Error: Solo se permiten números"
        self.val = a * b
        return self.val
    
    def divi(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            return "Error: Solo se permiten números"
        if b == 0:
            return "Error: División por cero"   
        self.val = a / b
        return self.val
    
    def cuadrado(self, a):
        if not isinstance(a, (int, float)):
            return "Error: Solo se permiten números"
        self.val = a * a
        return self.val
    
    def potencia(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            return "Error: Solo se permiten números"
        if b == 0:
            return 1
        self.val = a ** b
        return self.val

    def raiz_cuadrada(self, a):
        if not isinstance(a, (int, float)):
            return "Error: Solo se permiten números"
        if a < 0:
            return "Error: Raíz cuadrada de número negativo"
        self.val = a ** 0.5
        return self.val
     
    def fact(self, a):
        if not isinstance(a, int):
            return "Error: Solo se permiten números enteros"
        if a < 0:
            return "Error: Factorial de número negativo"
        if a == 0 or a == 1:
            return 1
        else:
            self.val = a * self.fact(a - 1)
            return self.val
        

class Calculadora_de_Areas(Calculadora):

    def __init__(self):
        super().__init__()
        self.pi = 3.141592653589793

    def getVal(self):
        return self.val * self.val

    def area_cuadrado(self, lado):
        if not isinstance(lado, (int, float)):
            return "Error: Solo se permiten números"
        if lado <= 0:
            return "Error: El lado no puede ser negativo ó cero"
        self.val = lado * lado
        return self.val
    
    def area_rectangulo(self, base, altura):
        if not (isinstance(base, (int, float)) and isinstance(altura, (int, float))):
            return "Error: Solo se permiten números"
        if base <= 0 or altura <= 0:
            return "Error: La base y la altura no pueden ser negativos ó cero"
        self.val = base * altura
        return self.val
    
    def area_triangulo(self, base, altura):
        if not (isinstance(base, (int, float)) and isinstance(altura, (int, float))):
            return "Error: Solo se permiten números"
        if base <= 0 or altura <= 0:
            return "Error: La base y la altura no pueden ser negativos ó cero"
        self.val = (base * altura) / 2
        return self.val

    def area_circulo(self, radio):
        if not isinstance(radio, (int, float)):
            return "Error: Solo se permiten números"
        if radio <= 0:
            return "Error: El radio no puede ser negativo ó cero"
        self.val = self.pi * radio * radio
        return self.val


class Menu:

    @staticmethod
    def Interfaz():
        print("Seleccione la operación a realizar:")
        print("0.Cerrar calculadora")
        print("1.Sumar")
        print("2.Restar")
        print("3.Cuadrado")
        print("4.Potencia")
        print("5.Raíz Cuadrada")
        print("6.Factorial")
        print("7.Area del Cuadrado")
        print("8.Area del Rectángulo")
        print("9.Area del Triángulo Rectangulo")
        print("10.Area del Círculo")


def mainCalc():
    Menu.Interfaz()
    calc = Calculadora()
    area = Calculadora_de_Areas()

    while True:
        try:
            switcher = int(input("Ingrese la opción deseada: \n"))
        except ValueError:
            print("Opción no válida\n")
            continue

        if switcher == 0:
            print("Cerrando calculadora...")
            break

        elif switcher == 1:
            try:
                a = float(input("Ingrese el primer número: \n"))
                b = float(input("Ingrese el segundo número: \n"))
                print("El resultado de la suma es: ", calc.sum(a, b))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        elif switcher == 2:
            try:
                a = float(input("Ingrese el primer número: \n"))
                b = float(input("Ingrese el segundo número: \n"))
                print("El resultado de la resta es: ", calc.rest(a, b))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        elif switcher == 3:
            try:
                a = float(input("Ingrese el número a elevar al cuadrado: \n"))
                print("El resultado del cuadrado es: ", calc.cuadrado(a))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        elif switcher == 4:
            try:
                a = float(input("Ingrese la base: \n"))
                b = float(input("Ingrese el exponente: \n"))
                print("El resultado de la potencia es: ", calc.potencia(a, b))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        elif switcher == 5:
            try:
                a = float(input("Ingrese el número para calcular su raíz cuadrada: \n"))
                print("El resultado de la raíz cuadrada es: ", calc.raiz_cuadrada(a))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        elif switcher == 6:
            try:
                a = int(input("Ingrese el número para calcular su factorial: \n"))
                print("El resultado del factorial es: ", calc.fact(a))
            except ValueError:
                print("Error: Debe ingresar solo números enteros.\n")

        elif switcher == 7:
            try:
                lado = float(input("Ingrese el lado del cuadrado: \n"))
                print("El área del cuadrado es: ", area.area_cuadrado(lado))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        elif switcher == 8:
            try:
                base = float(input("Ingrese la base del rectángulo: \n"))
                altura = float(input("Ingrese la altura del rectángulo: \n"))
                print("El área del rectángulo es: ", area.area_rectangulo(base, altura))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        elif switcher == 9:
            try:
                base = float(input("Ingrese la base del triángulo: \n"))
                altura = float(input("Ingrese la altura del triángulo: \n"))
                print("El área del triángulo es: ", area.area_triangulo(base, altura))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        elif switcher == 10:
            try:
                radio = float(input("Ingrese el radio del círculo: \n"))
                print("El área del círculo es: ", area.area_circulo(radio))
            except ValueError:
                print("Error: Debe ingresar solo números.\n")

        else:
            print("Opción no válida")


if __name__ == "__main__":
    mainCalc()