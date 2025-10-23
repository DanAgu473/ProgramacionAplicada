while (True):
    num= int(input("Ingrese un numero \n"))
    sobrante= num % 2
    if sobrante==0:
        print(num," es par")
    else:
        print(num," es impar")    