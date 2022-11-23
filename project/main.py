from flask import Blueprint
#from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Homepage'

@main.route('/profile')
def profile():
    return 'User Profile'