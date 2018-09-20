"""se define la clase"""

class operaciones:  #operaciones (identacion)

    def __init__(self,num, num2):
        self.num=num;
        self.num2=num2;

    def suma(self):
        print("5.-la suma del ",self.num,"mas",self.num2, "es igual a:",self.num+self.num2)

    def diferencia(self):
        print("7.-la diferencia del ", self.num, "con", self.num2, "es igual a:", self.num - self.num2)

    def verificar_cero(self):
        if self.num == 0:
            print("1.- el ",self.num,"si es igual a cero")
        else:
            print("1.-el ",self.num,"no es igual a cero")

    def sucesor(self):
        print("2.-el sucesor del ", self.num, "es", self.num+1)

    def antecesor(self):
        print("6.-el antecesor del ", self.num, "es", self.num-1)

    def igual(self):
        print("4.-el ", self.num, "es igual al", self.num)

    def escero(self):
        print("3.-el ", self.num, "es igual 0")

    def menor(self):
        if self.num < self.num2:
            print("8.- el numero menor es:", self.num)
        else:
            print("8.-el numero menor es: ",self.num2)
