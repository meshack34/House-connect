from flask import Blueprint, render_template

from app.main import auth

views = Blueprint('views',__name__)
 
@auth.route('/')
def home():
    return render_template("home.html")

# from .views import views
# from .auth import auth

