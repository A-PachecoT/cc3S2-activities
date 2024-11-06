import requests

import requests

class APIClient:
    def __init__(self, base_url, session=None):
        self.base_url = base_url
        # Inyección de dependencias: permitimos inyectar una sesión personalizada
        self.session = session or requests.Session()

    def get_todo(self, todo_id):
        try:
            response = self.session.get(f"{self.base_url}/todos/{todo_id}")
            response.raise_for_status() # Manejo de errores HTTP
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # Manejo de errores HTTP
            raise Exception(f"HTTP error occurred: {http_err}") from http_err
        except Exception as err:
            # Manejo de otros errores
            raise Exception(f"An error occurred: {err}") from err

    def create_todo(self, data):
        try:
            response = self.session.post(f"{self.base_url}/todos", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}") from http_err
        except Exception as err:
            raise Exception(f"An error occurred: {err}") from err

    def update_todo(self, todo_id, data):
        try:
            response = self.session.put(f"{self.base_url}/todos/{todo_id}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}") from http_err
        except Exception as err:
            raise Exception(f"An error occurred: {err}") from err

    def delete_todo(self, todo_id):
        try:
            response = self.session.delete(f"{self.base_url}/todos/{todo_id}")
            response.raise_for_status()
            return response.status_code == 200
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}") from http_err
        except Exception as err:
            raise Exception(f"An error occurred: {err}") from err