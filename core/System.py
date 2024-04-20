import datetime
import dateparser
from core.Database import AllowedEmails, User, UsersMeets, db

class System():
    def isEmailAllowedToLogin(self, email) -> bool:
        if AllowedEmails.query.filter_by(email=email).one_or_none():
            return True
        else:
            return False
        
    def addUserMeet(self, UserClass:User, title, description, date, time, duration):
        date = datetime.date.fromisoformat(date)
        time = datetime.time.fromisoformat(time)
        duration = datetime.time.fromisoformat(duration)
        user_meet = UsersMeets(created_by=UserClass.id, title=title, description=description, date=date, time=time, duration=duration)
        db.session.add(user_meet)
        db.session.commit()
        
        