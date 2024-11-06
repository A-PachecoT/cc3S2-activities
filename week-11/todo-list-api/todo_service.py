from api_client import APIClient

class TodoService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_todo_details(self, todo_id):
        todo = self.api_client.get_todo(todo_id)
        # Lógica de negocio adicional
        todo['title'] = todo['title'].title()
        return todo

    def add_todo(self, title, completed=False):
        data = {
            'title': title,
            'completed': completed
        }
        return self.api_client.create_todo(data)

    def complete_todo(self, todo_id):
        todo = self.api_client.get_todo(todo_id)
        if not todo['completed']:
            todo['completed'] = True
            return self.api_client.update_todo(todo_id, todo)
        return todo

    def remove_todo(self, todo_id):
        return self.api_client.delete_todo(todo_id) 