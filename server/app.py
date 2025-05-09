from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from utils.extensions import oauth, mail
from routes import register_blueprints
from dotenv import load_dotenv
import logging
import os

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

    # Initialize extensions
    JWTManager(app)
    mail.init_app(app)
    oauth.init_app(app)

    # Register blueprints
    register_blueprints(app)

    return app

if __name__ == '__main__':
    app = create_app()
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'

    logger.info(f"Starting Flask app on {host}:{port} (debug={debug})")
    app.run(host=host, port=port, debug=debug)
