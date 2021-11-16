from flask  import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='3aa896203b9aca2912c711d5994b2f1c'

    return app