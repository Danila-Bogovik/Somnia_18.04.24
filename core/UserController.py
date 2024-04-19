from core.UserModel import UserModel, User
   
class UserController(UserModel):
    def getUserById(self, user_id:int) -> User:
        
        if UserData:=self._userById(user_id):
            return User(UserData[0], UserData[1], UserData[2], UserData[3])
        else:
            return None
        
    def isEmailAllowedToLogin(self, email) -> bool:
        if self._EmailAllowed(email):
            return True
        else:
            return False
    
    def createUser(self, id, name, email, profile_pic):
        return self._create(id, name, email, profile_pic)
    
