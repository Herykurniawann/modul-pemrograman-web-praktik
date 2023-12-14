from app import app
from app.controllers import user_controller

@app.route('/')

def index():
    return 'Hello, World!'


@app.route('/users')
def users():
    return user_controller.index()