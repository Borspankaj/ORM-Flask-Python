from flask import Flask
from resources.user import UserResource
from resources.home import HomeResource
from exts import db 
from flask_restful import Api

def create_app() :
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////user.db'
    register_extensions(app)
    return app

def register_extensions(app) :

    db.init_app(app)
    api = Api(app)
    api.add_resource(HomeResource,'/')
    api.add_resource(UserResource, '/api/user', '/api/user/<string:username>')
    with app.app_context():
        db.create_all()
    
    

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

