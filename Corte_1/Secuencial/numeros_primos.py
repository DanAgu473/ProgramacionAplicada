while(True):
    num= int(input("Ingrese un valor: \n"))
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
    print("Es primo")
    repetir=int(input("Desea revisar otro número \nDigite 1 para Si u otro número para No \n"))
    if repetir!=1:
        break