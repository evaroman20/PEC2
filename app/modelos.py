import os


"""Limpia la pantalla de la terminal según el sistema operativo."""
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_estructura_tarea(nombre: str, **kwargs: str) -> dict:
    tarea = {
        "nombre": nombre,
        "completada": False,
        "prioridad": kwargs.get("prioridad", "No especificada"),
        "fecha_límite": kwargs.get("fecha_límite", "No especificada")
    }
    tarea.update(kwargs)
    return tarea

"""Clase encargada de almacenar y operar sobre la lista de tareas."""
class GestorTareas:
    
    def __init__(self):
        self.BASE_DE_TAREAS = []


    """Añade una tarea a la lista de tareas y devuelve un mensaje de éxito."""
    def añadir_tarea(self, nombre: str, **kwargs: str) -> str:
        tarea = crear_estructura_tarea(nombre, **kwargs)
        self.BASE_DE_TAREAS.append(tarea)
        return f"\nTarea '{tarea['nombre']}' añadida con éxito.\n"

    """Crea una lista de todas las tareas registradas y devuelve una lista de estructuras de tareas."""
    def listar_tareas(self):
         return self.BASE_DE_TAREAS

    """Filtra tareas por una palabra clave y devuelve una lista de estructuras de tareas."""
    def buscar_tarea(self, clave: str):
        coincidencias = [tarea for tarea in self.BASE_DE_TAREAS if clave.lower() in tarea['nombre'].lower()]
        return coincidencias

GESTOR_TAREAS = GestorTareas()
