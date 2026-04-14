from User import User
from UserRepository import UserRepository
        
user = User('Anmol', 24, 'anmol@gmail.com')
UserRepo = UserRepository('MySQL', 'Aanad', '******')
UserRepo.save_to_db(user)
UserRepo.delete_from_db(user)