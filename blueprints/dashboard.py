"""
Dashboard Blueprint
Main dashboard and portfolio views
"""

from flask import Blueprint, render_template, session, redirect, url_for
from database import db, User, Order
from functools import wraps

dashboard_bp = Blueprint('dashboard', __name__)

def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@dashboard_bp.route('/dashboard')
@login_required
def index():
    """Main dashboard"""
    user = User.query.get(session['user_id'])
    recent_orders = Order.query.filter_by(user_id=user.id).order_by(Order.created_at.desc()).limit(10).all()
    
    # Calculate statistics
    total_orders = Order.query.filter_by(user_id=user.id).count()
    pending_orders = Order.query.filter_by(user_id=user.id, status='PENDING').count()
    completed_orders = Order.query.filter_by(user_id=user.id, status='COMPLETE').count()
    
    stats = {
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
        'api_key': user.api_key
    }
    
    return render_template('dashboard/index.html', user=user, recent_orders=recent_orders, stats=stats)

@dashboard_bp.route('/orders')
@login_required
def orders():
    """Order book view"""
    user = User.query.get(session['user_id'])
    all_orders = Order.query.filter_by(user_id=user.id).order_by(Order.created_at.desc()).all()
    
    return render_template('dashboard/orders.html', orders=all_orders)

@dashboard_bp.route('/settings')
@login_required
def settings():
    """User settings"""
    user = User.query.get(session['user_id'])
    return render_template('dashboard/settings.html', user=user)
