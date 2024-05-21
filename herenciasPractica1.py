class Operaciones:
    def __init__(self):
        self.num1= int(input("Ingrese un numero:"))
        self.num2= int(input("Ingrese un numero:"))
        self.resultado= 0
    def imprimir(self):
        print("Calculadora:" ) 
class Suma(Operaciones):
    def __init__(self):
      super().__init__ ()
      print("Suma:", self.num1 + self.num2)
      #self.resultado= self.num1 + self.num2
      #print("Resultado:", self.resultado)
class Resta(Operaciones):
    def __init__(self):
      super().__init__ ()
      print("Resta:", self.num1 - self.num2)
      #self.resultado = self.num1 - self.num2
class Multiplicacion(Operaciones):
    def __init__(self):
      super().__init__ ()
      print("Multiplicacion:",self.num1 * self.num2)
      #self.resultado = self.num1 * self.num2


calculadora = Suma()
calculadora = Resta()
calculadora = Multiplicacion()     