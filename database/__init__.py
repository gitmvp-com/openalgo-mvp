"""
Database initialization and models
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db = SQLAlchemy()

def init_db(app):
    """Initialize database with app context"""
    db.init_app(app)
    
    with app.app_context():
        # Create db directory if it doesn't exist
        db_path = os.path.dirname(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
        if db_path and not os.path.exists(db_path):
            os.makedirs(db_path)
        
        # Create all tables
        db.create_all()
        print("✅ Database tables created")

class User(db.Model):
    """User model for authentication"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    api_key = db.Column(db.String(64), unique=True)
    broker = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Order(db.Model):
    """Order model for tracking placed orders"""
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_id = db.Column(db.String(50), unique=True)
    symbol = db.Column(db.String(50), nullable=False)
    exchange = db.Column(db.String(20), nullable=False)
    action = db.Column(db.String(10), nullable=False)  # BUY/SELL
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)
    order_type = db.Column(db.String(20), nullable=False)  # MARKET/LIMIT/SL
    product = db.Column(db.String(20))  # MIS/CNC/NRML
    status = db.Column(db.String(20), default='PENDING')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    
    def __repr__(self):
        return f'<Order {self.order_id} {self.symbol}>'

class ApiLog(db.Model):
    """API request logging"""
    __tablename__ = 'api_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    endpoint = db.Column(db.String(100), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    status_code = db.Column(db.Integer)
    ip_address = db.Column(db.String(50))
    user_agent = db.Column(db.String(255))
    request_data = db.Column(db.Text)
    response_data = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('api_logs', lazy=True))
    
    def __repr__(self):
        return f'<ApiLog {self.endpoint} {self.status_code}>'
