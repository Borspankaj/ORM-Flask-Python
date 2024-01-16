from flask_restful import Resource, reqparse
from exts import db
from models.user import User

class UserResource(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            return {'username': user.username, 'password': user.password}
        else:
            return {'message': 'User not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username cannot be blank')
        parser.add_argument('password', type=str, required=True, help='Password cannot be blank')
        args = parser.parse_args()

        new_user = User(username=args['username'], password=args['password'])
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201

    def put(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, required=True, help='Password cannot be blank')
        args = parser.parse_args()

        user = User.query.filter_by(username=username).first()
        if user:
            user.password = args['password']
            db.session.commit()
            return {'message': 'User updated successfully'}
        else:
            return {'message': 'User not found'}, 404

    def delete(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}
        else:
            return {'message': 'User not found'}, 404
