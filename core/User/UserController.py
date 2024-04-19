from core.User.UserModel import UserModel, User
   
class UserController(UserModel):
    def getUserById(self, user_id:int) -> User:
        
        if UserData:=self._userById(user_id):
            return User(*UserData)
        else:
            return None
        
    def isEmailAllowedToLogin(self, email) -> bool:
        if self._EmailAllowed(email):
            return True
        else:
            return False
    
    def createUser(self, id, name, email, google_profile_pic):
        return self._create(id, name, email, google_profile_pic)
    
