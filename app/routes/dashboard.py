# like home.py, this file is also a module and every variable or function belongs to this module can be imported elsewhere
from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db
from app.utils.auth import login_required

# the url_prefix argument will prefix every route in the blueprint with our specified string
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
# use our custom login decorator
@login_required
def dash():
    db = get_db()
    posts = (db.query(Post)
    .filter(Post.user_id == session.get('user_id'))
    .order_by(Post.created_at.desc())
    .all()
    )
    return render_template('dashboard.html', posts=posts, loggedIn=session.get('loggedIn'))

@bp.route('/edit/<id>')
@login_required
def edit(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render edit page
    return render_template('edit-post.html', post=post, loggedIn=session.get('loggedIn'))