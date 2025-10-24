import math

while(True):
    grados=float(input("Ingrese sus grados (sexagesimales): \n"))
    rad=grados/180.0*math.pi
    seno= math.sin(rad)
    print("El seno de: ", grados, "° en radianes",rad, "es: " ,seno )


    result= math.sin(math.radians(grados))
    result

    repetir=int(input("Desea revisar otro número \nDigite 1 para Si u otro número para No \n"))
    if repetir!=1:
            break