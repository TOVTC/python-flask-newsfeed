# like home.py, this file is also a module and every variable or function belongs to this module can be imported elsewhere
from flask import Blueprint, render_template

# the url_prefix argument will prefix every route in the blueprint with our specified string
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    return render_template('dashboard.html')