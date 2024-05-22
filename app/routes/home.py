# in the app/routes directory, routes is considered a package because it contains __init__.py
# home.py is considered a module that belongs to the routes package
from flask import Blueprint, render_template

# Blueprint() allows us to consolidate routes onto a single bp object that the parent app can register at a later time
# this is similar to using router in Express.js
bp = Blueprint('home', __name__, url_prefix='/')

# the @bp.route decorator turns the following functions into routes attached to the bp object
# render_template() will return a template instead of a string
@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')

# single() captures the id parameter in the route
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')