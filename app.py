#!/usr/bin/env python
"""
OpenAlgo MVP - Main Application Entry Point

A simplified algorithmic trading platform that bridges traders with brokers.
Built with Flask, SQLAlchemy, and Socket.IO for real-time updates.
"""

import os
import sys
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Verify critical environment variables
required_vars = ['APP_KEY', 'API_KEY_PEPPER']
missing_vars = [var for var in required_vars if not os.getenv(var) or os.getenv(var).startswith('CHANGE_ME')]

if missing_vars:
    print("\n" + "="*70)
    print("⚠️  CRITICAL: Missing or default security configuration!")
    print("="*70)
    for var in missing_vars:
        print(f"   • {var} is not set or using default value")
    print("\n📝 Please update your .env file with new values:")
    print("   1. Copy .sample.env to .env")
    print("   2. Generate new keys with:")
    print("      python -c \"import secrets; print(secrets.token_hex(32))\"")
    print("   3. Update APP_KEY and API_KEY_PEPPER in .env")
    print("="*70 + "\n")
    sys.exit(1)

print("\n" + "="*70)
print("🚀 Starting OpenAlgo MVP...")
print("="*70)

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Basic configuration
    app.secret_key = os.getenv('APP_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db/openalgo.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Session configuration
    HOST_SERVER = os.getenv('HOST_SERVER', 'http://127.0.0.1:5000')
    USE_HTTPS = HOST_SERVER.startswith('https://')
    
    app.config.update(
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
        SESSION_COOKIE_SECURE=USE_HTTPS,
        SESSION_COOKIE_NAME=os.getenv('SESSION_COOKIE_NAME', 'session')
    )
    
    # CSRF Protection
    csrf_enabled = os.getenv('CSRF_ENABLED', 'TRUE').upper() == 'TRUE'
    app.config['WTF_CSRF_ENABLED'] = csrf_enabled
    
    if csrf_enabled:
        csrf = CSRFProtect(app)
        app.csrf = csrf
    
    # Initialize database
    from database import init_db
    init_db(app)
    
    # Register blueprints
    from blueprints.auth import auth_bp
    from blueprints.dashboard import dashboard_bp
    from blueprints.api import api_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    # Home route
    @app.route('/')
    def index():
        if session.get('logged_in'):
            return redirect(url_for('dashboard.index'))
        return redirect(url_for('auth.login'))
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def server_error(e):
        return render_template('errors/500.html'), 500
    
    print("✅ Application initialized successfully")
    return app

if __name__ == '__main__':
    app = create_app()
    
    # Get configuration from environment
    host = os.getenv('FLASK_HOST_IP', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    
    print(f"\n📍 Server running at: http://{host}:{port}")
    print(f"🔧 Debug mode: {debug}")
    print(f"🗄️  Database: {os.getenv('DATABASE_URL', 'sqlite:///db/openalgo.db')}")
    print("="*70 + "\n")
    
    app.run(host=host, port=port, debug=debug)
