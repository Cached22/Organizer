from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    items = relationship('Item', back_populates='owner')

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    width = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    depth = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship('User', back_populates='items')

class Layout(Base):
    __tablename__ = 'layouts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    layout_data = Column(String, nullable=False)  # JSON or other serialized format
    user = relationship('User', backref='layouts')