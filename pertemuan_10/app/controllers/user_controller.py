from app.models.users import User
from app import response,app

def index():
    try :
        users = User.query.all()
        data = multiTransform(users)

        return response.success_response(data,"success")
    
    except Exception as e:
        return response.bad_request_response([],str(e))

def transform(user):
    data = {
        "id" : user.id,
        "username": user.username,
        "email": user.email,
    }

    return data

def multiTransform(user):
    data = []
    for i in user:
        data.append(transform(i))
    return data

    