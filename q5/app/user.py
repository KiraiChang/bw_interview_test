from flask_restful import Resource, request

userList = []

class User(Resource):

    def get(self, account):
        user = next(filter(lambda x: x['account'] == account, userList), None)
        return {'user': user}, 200 if user else 404
    
    def post(self, account):
        data = request.get_json();
        password = data['password']
        name = data['name']
        if next(filter(lambda x: x['account'] == account, userList), None):
            return { 'message': "Account '{}' already exists.".format(account)}, 400
        user = {'account': account, 'name': name, 'password': password}
        userList.append(user)
        return user, 201

    def put(self, account):
        data = request.get_json();
        password = data['password']
        name = data['name']
        user = next(filter(lambda x: x['account'] == account, userList), None)
        if user is None:
            user = {'account': account, 'name': name, 'password': password}
            userList.append(user)
        else:
            user['name'] = name
            user['password'] = password

        return user, 201

class Users(Resource):
    def get(self):
        return {'users': userList}