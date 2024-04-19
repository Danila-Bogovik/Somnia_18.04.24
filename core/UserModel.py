from core.Database import Database

class User():
    def __init__(self, id, name, email, profile_pic):
        self.id = id
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.is_authenticated = True
        self.is_active = True
        self.remember = True
        
    def get_id(self):
        return str(self.id)

class UserModel(Database):
    def _userById(self, user_id) -> tuple:
        return self._fetchOneData(f"SELECT * FROM Users WHERE id = '{user_id}'")
    
    def _EmailAllowed(self, email) -> bool:
        return self._fetchOneData(f"SELECT * FROM AllowedUsers WHERE email = '{email}'")
    
    def _create(self, id, name, email, profile_pic) -> bool:
        return self._executeData("INSERT INTO Users (id, name, email, profile_pic) VALUES(?, ?, ?, ?)", (id, name, email, profile_pic))