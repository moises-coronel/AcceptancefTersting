Feature: Administrador de tareas

  Scenario: Agregar una nueva tarea
    Given que no hay tareas en la lista
    When agrego la tarea "Comprar leche"
    Then la tarea "Comprar leche" debe ser agregada

  Scenario: Listar tareas
    Given que la lista de tareas contiene:
      | Comprar leche |
      | Lavar ropa    |
    When solicito ver todas las tareas
    Then se deben mostrar las tareas:
      | Comprar leche |
      | Lavar ropa    |

  Scenario: Completar una tarea
    Given la lista de tareas contiene:
      | Comprar leche |
    When marco la tarea "Comprar leche" como completada
    Then la tarea "Comprar leche" debe aparecer como completada

  Scenario: Eliminar todas las tareas
    Given que la lista de tareas contiene 2 tareas
    When elimino todas las tareas
    Then la lista de tareas debe estar vacía

  Scenario: Buscar una tarea
    Given la lista de tareas contiene:
      | Comprar leche |
      | Lavar ropa    |
      | Planchar camisas |
    When busco por "camisas"
    Then se debe retornar la tarea "Planchar camisas"