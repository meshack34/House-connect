from flask import Blueprint, app

views = Blueprint('views',__name__)


from .views import views
from .auth import auth

app.register_blueprint(views,)
app.register_blueprint(views)