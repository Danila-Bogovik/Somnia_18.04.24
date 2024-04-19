from core.Database import AllowedEmails, db

class Admin():
    def allowUserEmail(self, users_email):
        email = AllowedEmails(email=users_email)
        db.session.add(email)
        db.session.commit()