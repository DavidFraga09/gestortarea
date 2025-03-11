import unittest
from gestor_tareas import GestorTareas, Tarea

# Definir la clase de prueba GestorTareas
class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        """Configura un gestor de tareas con ejemplos antes de cada prueba"""
        self.gestor = GestorTareas()

        # Agregamos tres tareas de ejemplo con diferentes prioridades
        self.tarea1 = self.gestor.agregar_tarea("Revisar Documentos", "Revisar los documentos de la reunión", "media")
        self.tarea2 = self.gestor.agregar_tarea("Lavar el coche", "Realizar limpieza completa del coche", "alta")
        self.tarea3 = self.gestor.agregar_tarea("Preparar presentación", "Hacer presentación para el proyecto", "baja")

    # 1. Test the delete task functionality
    def test_eliminar_tarea_existente(self):
        """Successful deletion of an existing task"""
        self.assertTrue(self.gestor.eliminar_tarea(self.tarea1.id))
        self.assertIsNone(self.gestor.buscar_tarea_por_id(self.tarea1.id))

    def test_eliminar_tarea_inexistente(self):
        """Behavior when trying to delete a non-existent task"""
        self.assertFalse(self.gestor.eliminar_tarea(100))

    # 2. Test task search functionality by ID
    def test_buscar_tarea_existente(self):
        """Search for an existing task"""
        self.assertEqual(self.gestor.buscar_tarea_por_id(self.tarea2.id), self.tarea2)

    def test_buscar_tarea_inexistente(self):
        """Search for a non-existing task"""
        self.assertIsNone(self.gestor.buscar_tarea_por_id(100))

    # 3. Test the functionality of marking a task as completed
    def test_marcar_completada_existente(self):
        """Correctly marking an existing task"""
        self.assertTrue(self.gestor.marcar_completada(self.tarea3.id))
        self.assertTrue(self.tarea3.completada)

    def test_marcar_completada_inexistente(self):
        """Behavior when trying to mark a non-existent task"""
        self.assertFalse(self.gestor.marcar_completada(100))

    # 4. Test listing tasks
    def test_listar_todas_las_tareas(self):
        """Listing of all tasks"""
        self.assertEqual(len(self.gestor.listar_tareas()), 3)

    def test_listar_tareas_pendientes(self):
        """List filtered by pending tasks"""
        self.assertEqual(len(self.gestor.listar_tareas(completadas=False)), 3)
        self.gestor.marcar_completada(self.tarea1.id)
        self.assertEqual(len(self.gestor.listar_tareas(completadas=False)), 2)

    # 5. Test filtering tasks by priority
    def test_filtrar_por_prioridad(self):
        """The filtering of tasks for each priority level (high, normal, low, non-existent)"""
        self.assertEqual(len(self.gestor.filtrar_por_prioridad("alta")), 1)
        self.assertEqual(len(self.gestor.filtrar_por_prioridad("media")), 1)
        self.assertEqual(len(self.gestor.filtrar_por_prioridad("baja")), 1)
        self.assertEqual(len(self.gestor.filtrar_por_prioridad("inexistente")), 0)

    # 6. Test validation of invalid priorities
    def test_prioridad_invalida(self):
        """That an exception is thrown when using an impermissible priority"""
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("Tarea invalida", "Descripcion", "urgente")

    # 7. Test the custom comparison method (__eq__) of the Task class
    def test_tareas_con_mismo_id_iguales(self):
        """That two tasks with the same ID but different attributes are considered equal"""
        tarea1_clon = Tarea(self.tarea2.id, "Diferente titulo", "Otra descripcióon")
        self.assertEqual(self.tarea2, tarea1_clon)

    def test_tareas_con_diferente_id_diferentes(self):
        """That two tasks with different IDs are considered different"""
        tarea_nueva = Tarea(101, "Nueva tarea", "Descripcion nueva")
        self.assertNotEqual(self.tarea1, tarea_nueva)

    def test_tarea_no_es_igual_a_otro_tipo(self):
        """That task is not equal to an object of another type"""
        self.assertNotEqual(self.tarea2, "texto")

if __name__ == '__main__':
    unittest.main()
