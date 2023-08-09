# Función para editar una tarea
# lista para almacenar las tareas
tasks = []

# función para agregar una nueva tarea
def add_task(task):
  tasks.append(task)

# función para listar todas las tareas
def list_tasks():
  for index, task in enumerate(tasks):
    print(f"{index+1}. {task}")

# función para marcar una tarea como completada
def complete_task(index):
  tasks[index] = f"{tasks[index]} (completada)"

# función para borrar toda la lista
def clear_tasks():
  tasks.clear()

# Función para buscar una tarea
def find_task(search_term):
    results = []
    for task in tasks:
        if search_term in task:
            results.append(task)

    return results

#probando
add_task("Comprar comida")
add_task("Lavar ropa")
add_task("Pagar servicios")
print("encontrar task")
find_task("2")
# listar tareas
list_tasks()

# marcar una tarea como completada
complete_task(1)

# listar de nuevo
list_tasks()

# borrar lista
clear_tasks()

# lista vacía
list_tasks()