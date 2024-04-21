from flask_login import UserMixin
from core.Database import User, db

class User(User, UserMixin):
    def getUserById(self, user_id):
        return User.query.filter_by(id=str(user_id)).one_or_none()
    
    def editUserProfile(self, unique_id, display_name, about, telegram):
        user = self.getUserById(unique_id)
        user.name = display_name
        user.about = about
        user.telegram = telegram
        db.session.add(user)
        db.session.commit()
                    
    def createUser(self, unique_id, users_name, users_email, picture):
        user = User(id=unique_id, name=users_name, email=users_email, profile_pic=picture)
        db.session.add(user)
        db.session.commit()
        return True
        
    