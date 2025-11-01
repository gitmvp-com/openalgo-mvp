"""
API Blueprint
RESTful API endpoints for trading operations
"""

from flask import Blueprint, request, jsonify
from database import db, User, Order, ApiLog
from datetime import datetime
import secrets

api_bp = Blueprint('api', __name__)

def verify_api_key():
    """Verify API key from request"""
    data = request.get_json()
    if not data or 'apikey' not in data:
        return None, {'status': 'error', 'message': 'API key required'}
    
    user = User.query.filter_by(api_key=data['apikey']).first()
    if not user or not user.is_active:
        return None, {'status': 'error', 'message': 'Invalid or inactive API key'}
    
    return user, None

def log_api_request(user_id, endpoint, method, status_code, request_data=None, response_data=None):
    """Log API request to database"""
    log = ApiLog(
        user_id=user_id,
        endpoint=endpoint,
        method=method,
        status_code=status_code,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent'),
        request_data=str(request_data),
        response_data=str(response_data)
    )
    db.session.add(log)
    db.session.commit()

@api_bp.route('/placeorder', methods=['POST'])
def place_order():
    """Place a new order"""
    user, error = verify_api_key()
    if error:
        return jsonify(error), 401
    
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['symbol', 'exchange', 'action', 'quantity', 'ordertype']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        response = {'status': 'error', 'message': f'Missing required fields: {", ".join(missing_fields)}'}
        log_api_request(user.id, '/api/v1/placeorder', 'POST', 400, data, response)
        return jsonify(response), 400
    
    # Create order
    order = Order(
        user_id=user.id,
        order_id=f"ORD{secrets.token_hex(8).upper()}",
        symbol=data['symbol'],
        exchange=data['exchange'],
        action=data['action'].upper(),
        quantity=int(data['quantity']),
        price=float(data.get('price', 0)),
        order_type=data['ordertype'].upper(),
        product=data.get('product', 'MIS').upper(),
        status='PENDING'
    )
    
    db.session.add(order)
    db.session.commit()
    
    response = {
        'status': 'success',
        'message': 'Order placed successfully',
        'orderid': order.order_id
    }
    
    log_api_request(user.id, '/api/v1/placeorder', 'POST', 200, data, response)
    return jsonify(response), 200

@api_bp.route('/orderbook', methods=['POST'])
def get_orderbook():
    """Get user's order book"""
    user, error = verify_api_key()
    if error:
        return jsonify(error), 401
    
    orders = Order.query.filter_by(user_id=user.id).order_by(Order.created_at.desc()).all()
    
    order_list = [{
        'orderid': order.order_id,
        'symbol': order.symbol,
        'exchange': order.exchange,
        'action': order.action,
        'quantity': order.quantity,
        'price': order.price,
        'ordertype': order.order_type,
        'product': order.product,
        'status': order.status,
        'timestamp': order.created_at.isoformat()
    } for order in orders]
    
    response = {
        'status': 'success',
        'data': order_list
    }
    
    log_api_request(user.id, '/api/v1/orderbook', 'POST', 200, None, response)
    return jsonify(response), 200

@api_bp.route('/cancelorder', methods=['POST'])
def cancel_order():
    """Cancel an order"""
    user, error = verify_api_key()
    if error:
        return jsonify(error), 401
    
    data = request.get_json()
    
    if 'orderid' not in data:
        return jsonify({'status': 'error', 'message': 'Order ID required'}), 400
    
    order = Order.query.filter_by(order_id=data['orderid'], user_id=user.id).first()
    
    if not order:
        return jsonify({'status': 'error', 'message': 'Order not found'}), 404
    
    if order.status == 'COMPLETE':
        return jsonify({'status': 'error', 'message': 'Cannot cancel completed order'}), 400
    
    order.status = 'CANCELLED'
    order.updated_at = datetime.utcnow()
    db.session.commit()
    
    response = {
        'status': 'success',
        'message': 'Order cancelled successfully',
        'orderid': order.order_id
    }
    
    log_api_request(user.id, '/api/v1/cancelorder', 'POST', 200, data, response)
    return jsonify(response), 200

@api_bp.route('/funds', methods=['POST'])
def get_funds():
    """Get account funds (mock data for MVP)"""
    user, error = verify_api_key()
    if error:
        return jsonify(error), 401
    
    # Mock funds data
    response = {
        'status': 'success',
        'data': {
            'available_cash': 100000.00,
            'used_margin': 25000.00,
            'available_margin': 75000.00,
            'total_collateral': 100000.00
        }
    }
    
    log_api_request(user.id, '/api/v1/funds', 'POST', 200, None, response)
    return jsonify(response), 200

@api_bp.route('/ping', methods=['GET'])
def ping():
    """API health check"""
    return jsonify({
        'status': 'success',
        'message': 'OpenAlgo MVP API is running',
        'timestamp': datetime.utcnow().isoformat()
    }), 200
