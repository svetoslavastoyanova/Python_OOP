from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user in self.user_records:
            del self.rented_books[user]
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        if user_id in self.user_records and new_username != user:
            pass
