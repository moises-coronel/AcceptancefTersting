from behave import given, when, then

tasks = []

@given('que no hay tareas en la lista')
def step_impl(context):
  global tasks
  tasks = []

@when('agrego la tarea "{text}"')
def step_impl(context, text):
  global tasks
  tasks.append(text)

@then('la tarea "{text}" debe ser agregada')
def step_impl(context, text):
  assert text in tasks

@given('que la lista de tareas contiene')
def step_impl(context):
  global tasks
  tasks = [row['task'] for row in context.table]

@when('solicito ver todas las tareas')
def step_impl(context):
  global tasks
  context.printed_tasks = tasks.copy()

@then('se deben mostrar las tareas')
def step_impl(context):
  assert context.printed_tasks == [row['task'] for row in context.table]

@when('marco la tarea "{text}" como completada')
def step_impl(context, text):
  global tasks
  index = tasks.index(text)
  tasks[index] = f"{text} (Completada)"

@then('la tarea "{text}" debe aparecer como completada')
def step_impl(context, text):
  assert f"{text} (Completada)" in tasks

@when('elimino todas las tareas')
def step_impl(context):
  global tasks
  tasks.clear()

@then('la lista de tareas debe estar vacía')
def step_impl(context):
  assert len(tasks) == 0

@when('busco por "{text}"')
def step_impl(context, text):
  global tasks
  context.search_result = [task for task in tasks if text in task]

@then('se debe retornar la tarea "{text}"')
def step_impl(context, text):
  assert context.search_result == [text]