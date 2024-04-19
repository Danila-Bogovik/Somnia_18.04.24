from core.UserModel import UserModel

class User():
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        
class UserController(UserModel):
    def getUserById(self, user_id:int):
        return self._userById(user_id)
    
    def createUser(self, id, name, email, profile_pic):
        return self._create(id, name, email, profile_pic)