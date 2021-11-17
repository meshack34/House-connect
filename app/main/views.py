from flask import Blueprint, render_template

from app.main import auth

views = Blueprint('views',__name__)
 
@auth.route('/')
def home():
    return render_template("home.html")

# @auth.route('/ABOUT US')
# def about():
#     return render_template('about.html')

# from .views import views
# from .auth import auth

