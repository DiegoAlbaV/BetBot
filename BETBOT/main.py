import subprocess
def opcion_1():    
    print("\nMOSTRANDO PROBABILIDADES.")
    from probabilidades import funcion_en_otro_archivo
    funcion_en_otro_archivo()

def opcion_2():
    print("\nODDS CALC.")
    from op2 import funcion2
    funcion2()

def opcion_3():    
    print("\nFootyStats.")
    from op3 import funcion3
    funcion3()

def salir():
    print("Saliendo del menú. ¡Hasta luego!")

def switch(opcion):
    opciones = {
        '1': opcion_1,
        '2': opcion_2,
        '3': opcion_3,
        '4': salir
    }

    # Obtén la función correspondiente según la opción
    funcion = opciones.get(opcion, lambda: print("Opción no válida. Inténtalo de nuevo."))

    # Ejecuta la función
    funcion()

def mostrar_menu():
    print("BETBOT MENU")
    print("1. PROBABILIDADES")
    print("2. ODDS")
    print("3. FOOTYSTATS")
    print("4. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion_elegida = input("Ingresa el número de la opción que deseas (1-4): ")

        switch(opcion_elegida)

        if opcion_elegida == '4':
            break
