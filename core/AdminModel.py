from core.Database import Database

class AdminModel(Database):
    def _allowEmail(self, email):
        return self._executeData(f"INSERT INTO AllowedUsers (email) VALUES('{email}')", ())