import random #libreria para buscar palabras en aleatorio
"""se define la clase"""
class juego:

    def buscar_palabra(self):

       palabras = ['sombra', 'animal', 'django', 'oveja', 'aprender', 'ejercicios',
          'caballo', 'perro', 'vaca', 'computadora', 'python', 'abeja', 'diente ',
          'conejo','mantel', 'mesa', 'basura', 'escritorio', 'ubuntu', 'gorro',
          'parque', 'amuleto', 'cama', 'cuarto', 'descargar', 'curso diario ',
          'vaso', 'cuadro', 'foto', 'revista', 'esdrujula',
          'parlantes', 'radio', 'tutorial', 'banana', 'naranja', 'manzana ',
          'celular', 'casco', 'ventana', 'silla', 'pileta', 'juegos' ,'televisor ',
          'heladera', 'modulos', 'cocina', 'timbre', 'lavarropas', 'estufa', 'enchufe ',
          'futbol', 'pelota', 'pizarron', 'cargador', 'factura', 'papel', 'impresora ',
          'telefono', 'remedio', 'planta', 'vegetal', 'aves', 'luna', 'electricidad ',
          'copa', 'fernet', 'google', 'lenguaje', 'internet', 'esposa ',
          'jarra', 'microondas' ,'manual', 'sarten' ,'cortina', 'musica', 'pato']


       palabraAadivinar = random.choice(palabras)
       return palabraAadivinar #Retorna la palabra a adivinar

    def adivinar(self,palabra):
      # self.palabra=palabra
       tupalabra = " "
       intentos = 6
       print("La palaba es: ")
       while intentos > 0:
           fallas = 0
           for letra in palabra:
              if letra in tupalabra:
                   print(letra, end="")
              else:
                   print("x", end="")
                   fallas += 1
           if fallas == 0:
              print("\nEN HORABUENA ADIVINASTE LA PALABRA!!!")
              break

           tuletra = input("\nIngrese una letra: ")
           tupalabra += tuletra

           if tuletra not in palabra:
             intentos -= 1
             print("intente de nuevo")
             print("tienes", +intentos, "vidas")
           if intentos == 0:
              print("\nNO HAS ADIVINADO LA PALABRA!!!")
       else:
               print("Gracias por jugar ")
