from User import User

class UserRepository:
    def __init__(self, db: str, user: str, password: str):
        self.__db = db
        self.user = user
        self.password = password
        
    def save_to_db(self, user: User):
        print(f'Saving to database {user.get_user_details()}')
    
    def delete_from_db(self, user: User):
        print(f'Deleting from database {user.get_user_details()}')
        