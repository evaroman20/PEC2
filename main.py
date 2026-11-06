from app.operaciones import añadir_tarea, listar_tareas, buscar_tarea, mostrar_menu, iniciar_app
from colorama import init, Fore, Style

init(autoreset=True)

if __name__ == "__main__":
    iniciar_app()
    mostrar_menu()
    buscar_tarea("Python")
    listar_tareas()
    añadir_tarea("Comprar pan", prioridad="Alta")



