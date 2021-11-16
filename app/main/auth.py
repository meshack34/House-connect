from flask import Blueprint

views = Blueprint('auth',__name__)

@views.route('/')
def home():
    pass
