from core.Database import Database

class User():
    def __init__(self, id, google_name, display_name, email, google_profile_pic, custom_profile_pic, about):
        self.id = id
        self.google_name = google_name
        self.display_name = display_name
        self.email = email
        self.google_profile_pic = google_profile_pic
        self.custom_profile_pic = custom_profile_pic
        self.about = about
        self.is_authenticated = True
        self.is_active = True
        self.remember = True
        
    def get_id(self):
        return str(self.id)

class UserModel(Database):
    def _userById(self, user_id) -> tuple:
        return self._fetchOneData(f"SELECT id, google_name, display_name, email, google_profile_pic, custom_profile_pic, about FROM Users WHERE id = '{user_id}'")
    
    def _EmailAllowed(self, email) -> bool:
        return self._fetchOneData(f"SELECT email FROM AllowedUsers WHERE email = '{email}'")
    
    def _create(self, id, name, email, profile_pic) -> bool:
        return self._executeData("INSERT INTO Users (id, google_name, display_name, email, google_profile_pic) VALUES(?, ?, ?, ?, ?)", (id, name, name, email, profile_pic))