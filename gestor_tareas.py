class Tarea:
    def __init__(self, id, titulo, descripcion='', completada=False, prioridad='media'):
        # Asignar los valores básicos de una tarea
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada

        # Definir las prioridades válidas para la validación
        prioridades_validas = ['baja', 'media', 'alta']

        # Verificamos que la prioridad proporcionada sea válida
        if prioridad not in prioridades_validas:
            raise ValueError(f'La prioridad no es válida. Debe ser una de: {prioridades_validas}')

        # Asignamos la prioridad si pasó la validación
        self.prioridad = prioridad

    def __eq__(self, other):
        if not isinstance(other, Tarea):
            return False
        return self.id == other.id


class GestorTareas:
    def __init__(self):
        self.tareas = []  # Lista para almacenar tareas
        self.contador_id = 0  # Contador para IDs únicos

    def agregar_tarea(self, titulo, descripcion="", prioridad="media"):
        """Agrega una nueva tarea a la lista."""
        self.contador_id += 1
        nueva_tarea = Tarea(self.contador_id, titulo, descripcion, False, prioridad)
        self.tareas.append(nueva_tarea)
        return nueva_tarea

    def eliminar_tarea(self, id):
        """Elimina una tarea por su ID si existe."""
        for tarea in self.tareas:
            if tarea.id == id:
                self.tareas.remove(tarea)
                return True
        return False

    def buscar_tarea_por_id(self, id):
        """Busca y devuelve una tarea por su ID, o None si no existe."""
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea
        return None

    def marcar_completada(self, id):
        """Marca una tarea como completada si existe."""
        tarea = self.buscar_tarea_por_id(id)
        if tarea:
            tarea.completada = True
            return True
        return False

    def listar_tareas(self, completadas=None):
        """Devuelve la lista de tareas, filtrada según el parámetro completadas."""
        if completadas is None:
            return self.tareas
        else:
            return [tarea for tarea in self.tareas if tarea.completada == completadas]

    def filtrar_por_prioridad(self, prioridad):
        """Devuelve una lista de tareas filtradas por prioridad."""
        return [tarea for tarea in self.tareas if tarea.prioridad == prioridad]