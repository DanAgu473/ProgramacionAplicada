class Cuadrado:
    def __init__(self,val):
        self.val=val
    def getVal(self):
        return self.val*self.val

class Suma:
    def sum(self,a,b):
        return a+b

class Resta:
    def rest(self,a,b):
        return a-b
    
class Potencia:
    def potencia(self,a,b):
        return a**b

class Raiz:
     def raiz_cuadrada(self,a):
        return a**0.5
     
class factorial:
    def fact(self,a):
        if a==0 or a==1:
            return 1
        else:
            return a*self.fact(a-1)
        
class AreaC:
    def area_cuadrado(self,lado):
        return lado*lado
    
class AreaR:
    def area_rectangulo(self,base,altura):
        return base*altura
    
class AreaT:
    def area_triangulo(self,base,altura):
        return (base*altura)/2

class AreaCir:
    def area_circulo(self,radio):
        return 3.1416*radio*radio
