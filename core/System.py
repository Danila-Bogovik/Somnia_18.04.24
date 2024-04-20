from core.Database import AllowedEmails

class System():
    def isEmailAllowedToLogin(self, email) -> bool:
        if AllowedEmails.query.filter_by(email=email).one_or_none():
            return True
        else:
            return False
    