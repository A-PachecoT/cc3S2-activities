from typing import List, Optional
from src.models.user import User
from src.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: User) -> User:
        return self.repository.create(user)

    def get_all_users(self) -> List[User]:
        return self.repository.get_all()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(user_id)

    def update_user(self, user_id: int, user: User) -> Optional[User]:
        return self.repository.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id) 