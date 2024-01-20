from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

# Initialize SQLAlchemy with no settings
db = SQLAlchemy()

def init_db(app):
    """
    Initialize the database with the Flask app and create tables.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///space_organizer.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

def get_db_session():
    """
    Returns a session for the database connection.
    """
    engine = create_engine(os.environ.get('DATABASE_URL', 'sqlite:///space_organizer.db'))
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return db_session

# Import models here to ensure they are known to SQLAlchemy
from .models import User, Item

# Create tables if they don't exist
def create_tables():
    engine = create_engine(os.environ.get('DATABASE_URL', 'sqlite:///space_organizer.db'))
    if not engine.dialect.has_table(engine, 'user'):
        User.metadata.create_all(bind=engine)
    if not engine.dialect.has_table(engine, 'item'):
        Item.metadata.create_all(bind=engine)