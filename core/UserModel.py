from core.Database import Database
   
class UserModel(Database):
    def _userById(self, user_id) -> tuple:
        request = f"SELECT * FROM Users WHERE id = {user_id}"
        return self._fetchOneData(request)
    
    def _create(self, id, name, email, profile_pic):
        request = "INSERT INTO Users (id, name, email, profile_pic) VALUES(?, ?, ?, ?)"
        parameters = (id, name, email, profile_pic)
        return self._executeData(request, parameters)