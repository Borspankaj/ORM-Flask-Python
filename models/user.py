from exts import db

class User(db.Model) :

    username = db.Column(db.String(80) , primary_key =True)
    password = db.Column(db.String(25) , unique = True , nullable = False)

    def __repr__(self) -> str:
        return '<User %r>' % self.username
    
