from core.Database import AllowedEmails, User, db

class System():
    def getUserById(self, user_id):
        return User.query.filter_by(id=str(user_id)).one_or_none()
    
    def isEmailAllowedToLogin(self, email):
        if AllowedEmails.query.filter_by(email=email).one_or_none():
            return True
        else:
            return False
        
    def findPartnerForUser(self, user_id):
        user = self.getUserById(user_id)
        partner = User.query.filter(User.searching_partner == True, User.id != user_id).one_or_none()
        if partner:
            partner.searching_partner = False
            user.partner_id = partner.id
            partner.partner_id = user.id
            db.session.add(user)
            db.session.add(partner)
            db.session.commit()
            return partner
        else:
            user.searching_partner = True
            db.session.add(user)
            db.session.commit()
            return None
            
    def cencelSearhingForUser(self, user_id):
        user = self.getUserById(user_id)
        user.searching_partner = False
        db.session.add(user)
        db.session.commit()
        
    def skipPartnerForUser(self, user_id):
        user = self.getUserById(user_id)
        partner = self.getUserById(user.partner_id)
        user.partner_id = None
        partner.partner_id = None
        db.session.add(user)
        db.session.add(partner)
        db.session.commit()