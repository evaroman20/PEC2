import sys
from colorama import init, Back, Fore, Style
from app.modelos import clear_screen, GESTOR_TAREAS

"""Inicia colorama"""
init(autoreset=True)


"""Muestra el menú principal de la aplicación CLI."""
def mostrar_menu():

    clear_screen()

    print("\033[0;93m▄███▀████\033[0;37m \033[0;93m████▀████\033[0;37m \033[0;93m▄███▀████\033[0;37m \033[0;93m██▀████▀███\033[0;37m \033[0;93m▄███▀███▄\033[0;37m \033[0;93m█████▀█████\033[0;37m      \033[0;93m████▀███▄\033[0;37m \033[0;93m████▀████\033[0;37m      \033[0;93m██▀████▀███\033[0;37m \033[0;93m████▀████\033[0;37m \033[0;93m█████▀█████\033[0;37m \033[0;93m████▀████\033[0;37m \033[0;93m████▀████\033[0;37m \033[0;93m▄███▀████\033[0m")
    print("\033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m▀▀▀▀\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m▀▀▀▀\033[0;37m \033[0;93m██\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m███\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m███\033[0;37m \033[0;93m█████\033[0;37m      \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m      \033[0;93m██\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m███\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m███\033[0;37m \033[0;93m█████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m▀▀▀▀\033[0m")
    print("\033[0;93m█\033[0;97m█\033[0;93m██▀████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m▀▀▀▀\033[0;37m  \033[0;93m▀▀▀▀███▄\033[0;37m \033[0;93m▀▀\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m▀▀▀\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m███\033[0;37m \033[0;93m█████\033[0;37m      \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m▀▀▀▀\033[0;37m      \033[0;93m▀▀\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m▀▀▀\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m███\033[0;37m \033[0;93m█████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m▀▀▀▀\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m  \033[0;93m▀▀▀▀███▄\033[0m")
    print("\033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██▀▀\033[0;37m    \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m    \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m     \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m███▀███▄▄\033[0;37m      \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██▀▀\033[0;37m            \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m     \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m███▀███▄▄\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██▀▀\033[0;37m    \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0;37m \033[0;93m█\033[0;97m█\033[0;93m██\033[0;37m \033[0;93m████\033[0m")
    print("\033[0;93m▀███▄████\033[0;37m \033[0;93m████▄████\033[0;37m \033[0;93m████▄███▀\033[0;37m    \033[0;93m████\033[0;37m     \033[0;93m▀███▄███▀\033[0;37m \033[0;93m█████\033[0;37m \033[0;93m█████\033[0;37m      \033[0;93m████▄███▀\033[0;37m \033[0;93m████▄████\033[0;37m         \033[0;93m████\033[0;37m     \033[0;93m████▀████\033[0;37m \033[0;93m█████\033[0;37m \033[0;93m█████\033[0;37m \033[0;93m████▄████\033[0;37m \033[0;93m████▀████\033[0;37m \033[0;93m████▄███▀\033[0m")
    print("")
    print("1. Añadir Tarea")
    print("2. Listar Tareas")
    print("3. Buscar Tarea")
    print("4. Salir")


"""Inicia la aplicación CLI y gestiona el flujo de interacción con el usuario."""
def iniciar_app():

    clear_screen()

    while True:

        mostrar_menu()
        opcion = input(f"\nSelecciona una opción:\n")

        if opcion == "1":

            clear_screen()

            nombre = input("Nombre de la tarea:\n")
            if not nombre.strip():
                print(f"\n{Fore.RED}El nombre de la tarea no puede estar vacío.\n")
                continue

            prioridad = input("PRIORIDAD (Opcional - Presiona Enter para saltar): ")
       
            if prioridad:
                mensaje = GESTOR_TAREAS.añadir_tarea(nombre, PRIORIDAD = (prioridad).capitalize())
            else:
                mensaje = GESTOR_TAREAS.añadir_tarea(nombre)
            print(f"\n{Fore.GREEN}{mensaje}\n")

            completada = input("¿Deseas marcar la tarea como completada? (S/N): ").strip().capitalize()
            
            if completada == 'S':
                GESTOR_TAREAS.BASE_DE_TAREAS[-1]['completada'] = True
                print(f"\n{Fore.GREEN}La tarea '{nombre}' ha sido marcada como completada.\n")
            else:
                print(f"\n{Fore.BLUE}La tarea '{nombre}' se ha añadido como pendiente.\n")

            clear_screen()
            
        elif opcion == "2":
            
            clear_screen()

            tareas = GESTOR_TAREAS.listar_tareas()
            
            if not tareas:
                print(f"\n{Fore.RED}No hay tareas registradas todavía.\n")
            else:
                print(f"\n{Fore.MAGENTA}{Back.BLACK}------ LISTA DE TAREAS ------\n")
                for i, t in enumerate(tareas, 1):
                    extra = ", ".join([f"{k}: {v}" for k, v in t.items() if k not in ["nombre", "completada"]])
                    detalles = f" ({extra})" if extra else ""
                    print(f"{i}. [{ '✅' if t['completada'] else '❌' }] {t['nombre']}{detalles}")

            clear_screen()

        elif opcion == "3":

            clear_screen()

            print(f"\n{Fore.MAGENTA}{Back.BLACK}------ BUSCAR TAREAS ------\n")
            
            clave = input("Introduce la palabra clave a buscar: ")
            
            if not clave.strip():
                print(f"\n{Fore.RED}La palabra clave no puede estar vacía.\n")
                continue

            resultados = GESTOR_TAREAS.buscar_tarea(clave)

            if not resultados:
                    print(f"\n{Fore.RED}No se encontraron tareas que coincidan con '{clave}'.\n")
            else:
                    print(f"\n{Fore.MAGENTA}{Back.BLACK}--- RESULTADOS DE BÚSQUEDA ---\n")
                    for t in resultados:
                        extra = ", ".join([f"{k}: {v}" for k, v in t.items() if k not in ["nombre", "completada"]])
                        detalles = f" ({extra})" if extra else ""
                        print(f"- {t['nombre']}{detalles}")

            clear_screen()
                
        elif opcion == "4":

            clear_screen()

            print(f"\n{Fore.MAGENTA}{Back.BLACK}¡Hasta luego!\n")
            sys.exit()
        else:

            clear_screen()

            print(f"\n{Fore.RED}Opción no válida. Intenta de nuevo.\n")
