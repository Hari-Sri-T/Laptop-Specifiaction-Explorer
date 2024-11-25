from flask import Flask
from .models import init_db
from .views import views
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Use a strong, unique secret key

    # MySQL Configuration
    app.config['MYSQL_HOST'] = 'localhost'  #enter your mysql details
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ' '
    app.config['MYSQL_DB'] = '  '
    
    # Session Configuration
    app.config['SESSION_PERMANENT'] = False  # Sessions last only during browser session
    app.config['SESSION_TYPE'] = 'filesystem'  # Store session data on the file system

    # Initialize the database
    init_db(app)

    # Register Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
