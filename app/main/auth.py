from flask import Blueprint

views = Blueprint('main',__name__)

@views.route('/')
def home():
    pass
