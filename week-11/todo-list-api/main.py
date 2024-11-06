from todo_service import TodoService
from api_client import APIClient

def main():
    base_url = "https://jsonplaceholder.typicode.com"
    api_client = APIClient(base_url)
    todo_service = TodoService(api_client)

    # Obtener detalles de una tarea
    todo = todo_service.get_todo_details(1)
    print(f"Tarea: {todo['title']} - Completada: {todo['completed']}")

    # Agregar una nueva tarea
    new_todo = todo_service.add_todo("Aprender pytest")
    print(f"Nueva tarea creada: {new_todo}")

    # Completar una tarea
    updated_todo = todo_service.complete_todo(1)
    print(f"Tarea actualizada: {updated_todo}")

    # Eliminar una tarea
    result = todo_service.remove_todo(1)
    print(f"Tarea eliminada: {result}")

if __name__ == "__main__":
    main()