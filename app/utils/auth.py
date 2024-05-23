from flask import session, redirect
from functools import wraps

# decorators are functions that wrap other functions - similar to callbacks in JavaScript
# here, login_required expects an argument of another function

# def login_required(func):
#     @wraps(func)
#     def wrapped_function(*args, **kwargs):
#         print('wrapper')
#         return func(*args, **kwargs)
        
#     return wrapped_function

# when it's called, it looks like this

# @login_required
# def callback():
#     print('hello')

# callback() # prints 'wrapper' then 'hello'

# a wrapper is intended to return a new function, but by returning a new function, we change the internal name of the original function
# printing callback.__name__ prints wrapped_function instead of callback

# @wraps(func) decorator will preserve the original name when creating the wrapped function

# *args and **kwargs are keywords that ensure that no matter how many arguments are given (if any), the wrapped_function() captures them all

def login_required(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        # if logged in, call original function with original arguments
        if session.get('loggedIn') == True:
            return func(*args, **kwargs)
        return redirect('/login')
        
    return wrapped_function