while (True):
    num= int(input("Ingrese un numero \n"))
    sobrante= num % 2
    if sobrante==0:
        print(num," es par")
    else:
        print(num," es impar") 
    repetir=int(input("Desea revisar otro número \nDigite 1 para Si u otro número para No \n"))
    if repetir!=1:
        break