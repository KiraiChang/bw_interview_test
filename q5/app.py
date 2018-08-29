import os
from flask import Flask
from flask_restful import Api
from app.user import Users
from app.user import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user/<string:account>')
api.add_resource(Users, '/users/')

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'SuperSecretKey'

    # run
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000)))