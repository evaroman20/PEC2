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
        if opcion in ["1", "2", "3", "4"]:
            pass
        else:
            print(f"\n{Fore.RED}Debe escribir una opción válida. Inténtelo de nuevo.\n")
            input("Presiona Enter para continuar...")
            continue

        if opcion == "1":

            clear_screen()

            while True:

                nombre = input(f"{Fore.YELLOW}Nombre de la tarea:\n{Style.RESET_ALL}")
                if not nombre.strip():
                    print(f"\n{Fore.RED}El nombre de la tarea no puede estar vacío.\n")
                else:
                     break
                
            prioridad = input(f"{Fore.YELLOW}Prioridad (Opcional - Presiona Enter para saltar): {Style.RESET_ALL}")
        
            if prioridad:
                mensaje = GESTOR_TAREAS.añadir_tarea(nombre, prioridad = (prioridad).capitalize())
            else:
                mensaje = GESTOR_TAREAS.añadir_tarea(nombre)
                print(f"\n{Fore.GREEN}{mensaje}\n")

            completada = input(f"{Fore.YELLOW}¿Deseas marcar la tarea como completada? (S/N): {Style.RESET_ALL}").strip().capitalize()
                
            if completada == 'S':
                GESTOR_TAREAS.BASE_DE_TAREAS[-1]['completada'] = True
                print(f"\n{Fore.GREEN}La tarea '{nombre}' ha sido marcada como completada.\n")
            else:
                print(f"\n{Fore.RED}La tarea '{nombre}' se ha añadido como pendiente.\n")
            
                input(f"Presiona Enter para continuar...")
            
        elif opcion == "2":
            
            clear_screen()

            tareas = GESTOR_TAREAS.listar_tareas()
            
            if not tareas:
                print(f"\n{Fore.RED}No hay tareas registradas todavía.\n")
            else:
                print(f"\n{Fore.YELLOW}{Back.BLACK}------ LISTA DE TAREAS ------\n")
                for i, t in enumerate(tareas, 1):
                    extra = ", ".join([f"{k}: {v}" for k, v in t.items() if k not in ["nombre", "completada"]])
                    detalles = f" ({extra})" if extra else ""
                    print(f"{i}. [{ '✅' if t['completada'] else '❌' }] {t['nombre']}{detalles}")

            input(f"\nPresiona Enter para continuar...")

        elif opcion == "3":

            clear_screen()

            print(f"\n{Fore.YELLOW}{Back.BLACK}------ BUSCAR TAREAS ------\n")

            while True:

                clave = input(f"{Fore.YELLOW}Introduce la palabra clave a buscar: {Style.RESET_ALL}")
            
                if not clave.strip():
                    print(f"\n{Fore.RED}La palabra clave no puede estar vacía.\n")
                else:
                    break

            resultados = GESTOR_TAREAS.buscar_tarea(clave)

            if not resultados:
                    print(f"\n{Fore.RED}No se encontraron tareas que coincidan con '{clave}'.\n")
            else:
                    print(f"\n{Fore.YELLOW}{Back.BLACK}--- RESULTADOS DE BÚSQUEDA ---\n")
                    for t in resultados:
                        extra = ", ".join([f"{k}: {v}" for k, v in t.items() if k not in ["nombre", "completada"]])
                        detalles = f" ({extra})" if extra else ""
                        print(f"- {t['nombre']}{detalles}")
            
            input(f"\nPresiona Enter para continuar...")
                
        elif opcion == "4":

            clear_screen()

            print(f"\n{Fore.YELLOW}{Back.BLACK}¡Hasta luego!\n")
            sys.exit()