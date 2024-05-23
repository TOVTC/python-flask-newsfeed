# in the app/routes directory, routes is considered a package because it contains __init__.py
# home.py is considered a module that belongs to the routes package
from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db

# Blueprint() allows us to consolidate routes onto a single bp object that the parent app can register at a later time
# this is similar to using router in Express.js
bp = Blueprint('home', __name__, url_prefix='/')

# the @bp.route decorator turns the following functions into routes attached to the bp object
# render_template() will return a template instead of a string
@bp.route('/')
def index():
    # the get_db() function returns a session connection that's tied to this route's context
    # the query() method is used on the connection object to query the Post model
    # get all posts
    db = get_db()
    # you can choose to do a single line query like this
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    # or do a multi-line query using parentheses like this
    # posts = (
    #     db
    #       .query(Post)
    #       .order_by(Post.created_at.desc())
    #       .all()
    #     )

    # pass the retrieved posts in as an argument to the template and pass the loggedIn session property
    return render_template('homepage.html', posts=posts, loggedIn=session.get('loggedIn'))

@bp.route('/login')
def login():
    # not logged in yet
    if session.get('loggedIn') is None:
        return render_template('login.html')
    return redirect('/dashboard')

# single() captures the id parameter in the route
@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render single post template
    return render_template('single-post.html', post=post, loggedIn=session.get('loggedIn'))