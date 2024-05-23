from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db
# allows you to print errors to the console
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

# this route resolves to /api/users that accepts POST requests
@bp.route('/users', methods=['POST'])
def signup():
    # similar to the global g object, use the global request object to capture information sent through POST requests
    data = request.get_json()
    db = get_db()

    try:
        # attempt to create a new user
        # request.get_json() returns a Python dictionary that can be passed to a new User model instance using bracket notation
        newUser = User(
            username = data["username"],
            email = data["email"],
            password = data["password"]
        )

        # save in database
        db.add(newUser)
        db.commit()
    except:
        print(sys.exc_info()[0])
        # it may print an AssertionError - thrown when custom validations fail
        # or it may print an IntegrityError - thrown when something specific to MySQL (like UNIQUE contraint) fails
        # multiple except statements with the error type can be added to the statement for more specific error handling

        # if db.commit() fails, the connection remains in a pending state, which can crash the app
        # to resolve this, rollback the last commit
        # insert failed, so rollback
        db.rollback()

        # send error to front end
        return jsonify(message = 'Sign up failed'), 500

    # clear existing sessions and set two new seession properties
    # you can create sessions in Flask only if you have defined a secret key (ours is in app/__init__.py)
    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True

    return jsonify(id = newUser.id)

@bp.route('/users/logout', methods=['POST'])
def logout():
    # remove session variables
    session.clear()
    return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()

    try:
        user = db.query(User).filter(User.email == data['email']).one()
    except:
        print(sys.exc_info()[0])
        return jsonify(message = 'Incorrect credentials'), 400
    
    # here, data['password'] becomes the second parameter for verify_password because the first param is self
    if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect credentials')
    
    # user exists and credentials are correct
    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True

    return jsonify(id = user.id)