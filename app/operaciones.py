import sys
from colorama import init, Fore, Style
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

def crear_estructura_tarea(nombre: str, **kwargs: str):
    
    tarea = {
        "nombre": nombre,
        "completada": False,
        "prioridad": kwargs.get("prioridad", "Baja"),
        "fecha_límite": kwargs.get("fecha_límite", "No especificada")
    }
    
    tarea.update(kwargs)
    return tarea

def añadir_tarea(nombre: str, **kwargs: str):
    tarea = crear_estructura_tarea(nombre, **kwargs)
    return f"Tarea '{tarea['nombre']}' añadida con éxito."
    

def listar_tareas():
     return [crear_estructura_tarea("Tarea de ejemplo", prioridad="Media", fecha_límite="2024-12-31")]

def buscar_tarea(clave: str):
    nombre = input("Introduce el nombre de la tarea a listar (o presiona Enter para listar todas): ")
    if nombre:
            tareas = buscar_tarea(nombre)
            if not nombre in tareas:
                print(f"{Fore.RED}No se encontraron tareas con el nombre '{nombre}'.")
                return []

def mostrar_menu():

    print(f"\n{Fore.YELLOW}{Style.BRIGHT}------ GESTOR DE TAREAS CLI ------\n")

    print("1. Añadir Tarea")
    print("2. Listar Tareas")
    print("3. Buscar Tarea")
    print("4. Salir")

def iniciar_app():

    while True:

        mostrar_menu()

        opcion = input(f"\n{Fore.YELLOW}Selecciona una opción:\n")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            prioridad = input("Prioridad (Opcional - Presiona Enter para saltar): ")
       
            if prioridad:
                mensaje = añadir_tarea(nombre, prioridad=prioridad)
            else:
                mensaje = añadir_tarea(nombre)
            print(f"{Fore.GREEN}{mensaje}")
            clear_screen()        

        elif opcion == "2":
            tareas = listar_tareas()
            if not tareas:
                print(f"{Fore.RED}No hay tareas registradas.")
            else:
                print(f"\n{Fore.YELLOW}------ LISTA DE TAREAS ------")
                for i, t in enumerate(tareas, 1):
                    extra = ", ".join([f"{k}: {v}" for k, v in t.items() if k not in ["nombre", "completada"]])
                    detalles = f" ({extra})" if extra else ""
                    print(f"{i}. [{ '✓' if t['completada'] else ' ' }] {t['nombre']}{detalles}")
                    clear_screen()

        elif opcion == "3":
            clave = input("Introduce la palabra clave a buscar: ")
            resultados = buscar_tarea(clave)
            if not resultados:
                print(f"{Fore.RED}No se encontraron tareas.")
            else:
                print(f"\n{Fore.GREEN}--- RESULTADOS DE BÚSQUEDA ---")
                for t in resultados:
                    print(f"- {t['nombre']}")
                    clear_screen()

        elif opcion == "4":
            print(f"{Fore.BLUE}¡Hasta luego!")
            sys.exit()
            clear_screen()
        else:
            print(f"{Fore.RED}Opción no válida. Intenta de nuevo.")
