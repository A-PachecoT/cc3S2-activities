from typing import List, Optional
from src.models.user import User

class UserRepository:
    def __init__(self):
        self.users: List[User] = []
        self.next_id = 1

    def create(self, user: User) -> User:
        user.id = self.next_id
        self.next_id += 1
        self.users.append(user)
        return user

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: int) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def update(self, user_id: int, user_data: User) -> Optional[User]:
        existing_user = self.get_by_id(user_id)
        if existing_user:
            user_data.id = user_id
            self.users = [user_data if user.id == user_id else user for user in self.users]
            return user_data
        return None

    def delete(self, user_id: int) -> bool:
        initial_length = len(self.users)
        self.users = [user for user in self.users if user.id != user_id]
        return len(self.users) < initial_length 