#Actividad 3
#Operacion entre conjuntos
#Lozano Mena Leonardo Daniel

from operacion import *



while True:

    print("ACTIVIDAD NUMEROS POSITIVOS CON CERO: ")
    print("Selecciona una opción: ")
    print("\t1 - Inicio")
    print("\t2 - Salida")
    # solicituamos una opción al usuario

    opcionMenu = input("\ninserte opcion>> ")
    if opcionMenu=="1":
        numero = int(input("introduzca el numero: "))
        numero2 = int(input("introduzca otro numero, NOTA: sera empleado para la suma y diferencia: "))
        prototipo = operaciones(numero, numero2)
        prototipo.verificar_cero()
        prototipo.sucesor()
        prototipo.escero()
        prototipo.igual()
        prototipo.suma()
        prototipo.antecesor()
        prototipo.diferencia()
        prototipo.menor()
        input("Pulsa una tecla para continuar")

    elif opcionMenu=="2":
        break
    else:
        print("")
        input("No has seleccionado ninguna opción correcta...\npulsa una tecla para continuar")

