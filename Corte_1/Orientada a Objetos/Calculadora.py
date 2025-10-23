import Clase_Calculadora

print("Seleccione la operación a realizar:")
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

while(True):
    switcher=int(input("Ingrese la opción deseada (1/2/3/4/5/6): \n"))
    if switcher==1:
        a=int(input("Ingrese el primer número: \n"))
        b=int(input("Ingrese el segundo número: \n"))
        suma=Clase_Calculadora.Suma()
        print("El resultado de la suma es: ",suma.sum(a,b))
    elif switcher==2:
        a=int(input("Ingrese el primer número: \n"))
        b=int(input("Ingrese el segundo número: \n"))
        resta=Clase_Calculadora.Resta()
        print("El resultado de la resta es: ",resta.rest(a,b))
    elif switcher==3:
        val=int(input("Ingrese el número a elevar al cuadrado: \n"))
        cuadrado=Clase_Calculadora.Cuadrado(val)
        print("El resultado del cuadrado es: ",cuadrado.getVal())
    elif switcher==4:
        a=int(input("Ingrese la base: \n"))
        b=int(input("Ingrese el exponente: \n"))
        potencia=Clase_Calculadora.Potencia()
        print("El resultado de la potencia es: ",potencia.potencia(a,b))
    elif switcher==5:
        a=int(input("Ingrese el número para calcular su raíz cuadrada: \n"))
        raiz=Clase_Calculadora.Raiz()
        print("El resultado de la raíz cuadrada es: ",raiz.raiz_cuadrada(a))
    elif switcher==6:
        a=int(input("Ingrese el número para calcular su factorial: \n"))
        factorial=Clase_Calculadora.factorial()
        print("El resultado del factorial es: ",factorial.fact(a))
    elif switcher==7:
        lado=int(input("Ingrese el lado del cuadrado: \n"))
        area_cuadrado=Clase_Calculadora.AreaC()
        print("El área del cuadrado es: ",area_cuadrado.area_cuadrado(lado))
    elif switcher==8:
        base=int(input("Ingrese la base del rectángulo: \n"))
        altura=int(input("Ingrese la altura del rectángulo: \n"))
        area_rectangulo=Clase_Calculadora.AreaR()
        print("El área del rectángulo es: ",area_rectangulo.area_rectangulo(base,altura))
    elif switcher==9:
        base=int(input("Ingrese la base del triángulo: \n"))
        altura=int(input("Ingrese la altura del triángulo: \n"))
        area_triangulo=Clase_Calculadora.AreaT()
        print("El área del triángulo es: ",area_triangulo.area_triangulo(base,altura))
    elif switcher==10:
        radio=int(input("Ingrese el radio del círculo: \n"))
        area_circulo=Clase_Calculadora.AreaCir()
        print("El área del círculo es: ",area_circulo.area_circulo(radio))
    else:
        print("Opción no válida")
    repetir=int(input("Desea realizar otra operación \nDigite 1 para Si u otro número para No \n"))
    if repetir!=1:
        break
