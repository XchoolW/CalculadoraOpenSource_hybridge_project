from sumar import Suma
from resta import Resta 
from multiplicacion import Multiplicacion
from dividir import Dividir
from suma_avanzada import SumaAvanzada

opciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Suma avanzada", "Salir"]

def solicitar_numeros():
    try:
        n1 = int(input("Pasame el primer numero: "))
        n2 = int(input("Pasame el segundo numero: "))
    except ValueError:
        print("No es un numero valido")

    return n1, n2


running = True

print("Bienvenido a la Calculador Git \n")

while running:
    
    # Mostrar menu
    print("Elige una opcion: ")
    contador = 1
    for i in opciones:
        print(f"{str(contador)}.{i}", end="   ")
        contador += 1
    print() 

    try:
        seleccion = int(input("Eleccion --> "))
    except ValueError:
        print("No es una opcion validad")
        pass

    if seleccion == 1:
        n1, n2 = solicitar_numeros()
        
        suma = Suma(n1, n2)
        print(f"El resultado es {suma.sumar()}\n\n")

    elif seleccion == 2:
        n1, n2 = solicitar_numeros()

        resta = Resta(n1, n2)
        print(f"El resultado es {resta.resta()}\n\n")

    elif seleccion == 3:
        n1, n2 = solicitar_numeros()

        multi = Multiplicacion(n1, n2)
        print(f"El resultado es {multi.multiplica()}\n\n")

    elif seleccion == 4:
        n1, n2 = solicitar_numeros()
        
        div = Dividir(n1, n2)
        print(f"El resultado es {div.dividir()}\n\n")
    
    elif seleccion == 5:
        try:
            ntimes = int(input("Cuantas veces deseas hacer la suma: "))
        except ValueError:
            print("Ese no es un numero valido")
            pass

        sumav = SumaAvanzada(ntimes)
        print(f"El resultado es {sumav.sumar()}\n\n")
    
    else:
        print("Gracias por usar")
        break
