from core.Database import AllowedEmails, User, db

class Admin():
    def allowUserEmail(self, users_email):
        if AllowedEmails.query.filter_by(email=users_email).one_or_none():
            return
        email = AllowedEmails(email=users_email)
        db.session.add(email)
        db.session.commit()
        
    def setAdminToUser(self, users_email):
        user = User.query.filter_by(email=users_email).one_or_none()
        if user:
            user.admin = True
            db.session.add(user)
            db.session.commit()
            
    def deliteUserEmail(self, email):
        user = User.query.filter_by(email=email).one_or_none()
        email = AllowedEmails.query.filter_by(email=email).one_or_none()
        if email and user:
            db.session.delete(user)
            db.session.delete(email)
            db.session.commit()
     
    def getAllowedUsersEmail(self):
        return User.query.filter_by().all()
    
    