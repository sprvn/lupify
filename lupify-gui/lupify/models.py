from lupify import db, app
from ldap3 import Server, Connection
from json import loads, dumps
from uuid import uuid4

from flask_login import UserMixin

class User(UserMixin):

    def __init__( self, username, id = 0 ):
        if id == 0:
            self.id = uuid4()
        else:
            self.id = id
        self.username = username

    def __repr__(self):
        return '<User %r %s>' % (self.username, self.id)

    def save(self):
        db.users.insert(loads(self.to_json()))
        return True

    def to_json(self):
        data = {}
        for key, value in self.__dict__.items():
            data[key] = str(value)

        return dumps(data)


    @staticmethod
    def try_login(username, password):
        s = Server(app.config['LDAP_HOST'], port = 636, use_ssl = True)
        c = Connection(s, app.config['LDAP_BIND_USER'], app.config['LDAP_BIND_PASS'])
        try:
            c.bind()
        except:
            return False

        try:
            c.search(
                     app.config['LDAP_BASE_DN'], 
                     '(&(uid=%s)(memberof=%s))' % (username, 
                                                   app.config['LDAP_GROUP_DN']))
            if len(c.entries) == 1: 
                user_dn = loads((c.entries[0]).entry_to_json())['dn']
        except:
            return False

        c.unbind()

        if 'user_dn' in locals() and user_dn:
            c = Connection(s, user_dn, password)
            try:
                if c.bind():
                    c.unbind()
                    db.users.delete_one({"username": username})
                    return True
                return False
            except:
                return False

    @staticmethod
    def get_user(userid):
        user = db.users.find_one({"id": userid})
        if user:
            return User(user['username'], user['id'])
        else:
            return None
