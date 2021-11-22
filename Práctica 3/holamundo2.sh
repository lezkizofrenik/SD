#!/usr/bin/env python
from bottle import Bottle, run, template, route, get, request, post
app = Bottle()

@app.route('/hello/<name>')
def index(name):
    return template('<b> Hello {{name}}</b>!', name =name)


@app.route('/cars') 
def getcars():
    cars= [ {'name': 'Audi', 'price': 34535}, {'name': 'Skoda', 'price': 2342234}]
    return dict(data=cars)


@app.route('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

usernames = ["username", "user"]
passwords = ["password", "pass"]
def check_login(username, password):
    if username in usernames and password in passwords:
        return True
    else:
        return False

@app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password) is True:
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

_names = ['a']
@app.route('/names/<oldname>', method='PUT')
def update_handler(oldname):
    try:
        data = json.load(utf8reader(request.body))
    except:
        raise ValueError

    newname = data['name']
    _names.remove({{oldname}})
    _names.add(newname)

    respose.headers['content-Type'] = 'application/json'
    return json.dumps({'name': newname})

run(app, host='localhost', port=8080)