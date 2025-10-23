import Clase_Calculadora

print("Seleccione la operación a realizar:")
print("1.Sumar")
print("2.Restar")
print("3.Cuadrado")
print("4.Potencia")
print("5.Raíz Cuadrada")
print("6.Factorial")

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
    repetir=int(input("Desea realizar otra operación \nDigite 1 para Si u otro número para No \n"))
    if repetir!=1:
        break
