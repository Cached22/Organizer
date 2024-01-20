from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy ORM instance
db = SQLAlchemy()

def init_db(app):
    """
    Initialize the database with the given Flask app.
    """
    with app.app_context():
        db.init_app(app)
        # This line can be used to create tables based on the models if they don't exist
        # db.create_all() 

# Import the models to ensure they are registered with SQLAlchemy before creating the tables
from .models import User, Item

# You can add additional imports for other models as you create them
# from .models import AnotherModel
