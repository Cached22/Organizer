from flask import Flask
from .api.routes import api_blueprint
from .database.db import initialize_db
from .utils.logging import setup_logging

def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables or default ones
    app.config.from_pyfile('config.py')
    app.config.from_envvar('SPACEORGANIZER_SETTINGS', silent=True)

    # Initialize logging
    setup_logging(app)

    # Initialize database
    initialize_db(app)

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

# If this file is executed, create and run the Flask application
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)