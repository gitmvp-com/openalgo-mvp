# OpenAlgo MVP - Algorithmic Trading Platform

![OpenAlgo MVP](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.12+-green.svg)
![Flask](https://img.shields.io/badge/flask-3.0.3-lightgrey.svg)
![License](https://img.shields.io/badge/license-AGPL%20V3.0-orange.svg)

OpenAlgo MVP is a simplified version of the comprehensive algorithmic trading platform that bridges traders with major brokers through a unified API. Built with Flask, Tailwind CSS, and DaisyUI.

## 🚀 Features

### Core Features
- ✅ **Authentication & User Management** - Secure login with Argon2 password hashing
- ✅ **Order Management API** - Place, modify, cancel orders with unified API
- ✅ **Real-time Dashboard** - WebSocket-powered live updates
- ✅ **API Key Management** - Generate and manage API keys for integrations
- ✅ **Broker Integration** - Extensible broker plugin system
- 📊 **Market Data API** - Real-time quotes, historical data, market depth
- 📈 **Portfolio Tracking** - Positions, holdings, order book, trade book
- 🔍 **Symbol Search** - Search trading instruments across exchanges

### Advanced Features
- 📡 **WebSocket Streaming** - Real-time market data with ZeroMQ message bus
- 🎯 **API Analyzer** - Test strategies without live execution (sandbox mode)
- 📊 **PnL Tracker** - Real-time profit/loss monitoring with TradingView charts
- 🤖 **ChartInk Integration** - Execute strategies from ChartInk signals
- 📈 **TradingView Integration** - Webhook support for TradingView alerts
- 💬 **Telegram Bot** - Trade notifications and command execution
- 🔐 **Security Features** - CORS, CSP, CSRF protection, rate limiting
- 📊 **Monitoring Tools** - Latency monitor, traffic monitor, performance analytics

## 📋 Prerequisites

- Python 3.12 or higher
- Node.js 18+ (for Tailwind CSS build)
- SQLite (included with Python)
- A broker account with API access

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gitmvp-com/openalgo-mvp.git
cd openalgo-mvp
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Set Up Frontend Dependencies

```bash
# Install Node.js dependencies
npm install

# Build Tailwind CSS
npm run build
```

### 4. Configure Environment

```bash
# Copy sample environment file
cp .sample.env .env

# Edit .env file with your configuration
# IMPORTANT: Generate new security keys!
```

**Generate Security Keys:**

```bash
# Generate APP_KEY
python -c "import secrets; print(secrets.token_hex(32))"

# Generate API_KEY_PEPPER
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Initialize Database

The database will be automatically initialized on first run.

### 6. Run the Application

```bash
# Development mode
python app.py

# Or use Flask directly
flask run
```

### 7. Access the Application

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 🐳 Docker Installation (Alternative)

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access at http://localhost:5000
```

## 📚 API Documentation

### Unified API Endpoints (`/api/v1/`)

#### Order Management
- `POST /api/v1/placeorder` - Place a new order
- `POST /api/v1/placesmartorder` - Place smart order with position sizing
- `POST /api/v1/modifyorder` - Modify existing order
- `POST /api/v1/cancelorder` - Cancel specific order
- `POST /api/v1/cancelallorder` - Cancel all pending orders
- `POST /api/v1/closeposition` - Close open position
- `POST /api/v1/basketorder` - Execute multiple orders

#### Account & Portfolio
- `POST /api/v1/funds` - Get account funds and margins
- `POST /api/v1/orderbook` - Retrieve order book
- `POST /api/v1/tradebook` - Get executed trades
- `POST /api/v1/positionbook` - View current positions
- `POST /api/v1/holdings` - Get demat holdings
- `POST /api/v1/openposition` - Check position details

#### Market Data
- `POST /api/v1/quotes` - Get real-time quotes
- `POST /api/v1/depth` - Get market depth
- `POST /api/v1/history` - Fetch historical OHLC data
- `POST /api/v1/search` - Search for symbols

#### Utilities
- `POST /api/v1/analyzer` - Test API requests (sandbox)
- `GET /api/v1/ping` - Test API connectivity

### Authentication

All API requests require an API key in the header:

```bash
curl -X POST http://127.0.0.1:5000/api/v1/funds \
  -H "Content-Type: application/json" \
  -d '{"apikey": "your-api-key"}'
```

## 🔐 Security Configuration

### Key Security Features

1. **Password Security**
   - Argon2 hashing (PHC winner)
   - Pepper-enhanced security

2. **API Key Security**
   - Encrypted storage with Fernet
   - Hashed validation
   - Time-based caching

3. **Session Security**
   - Secure cookies
   - Auto-expiry at 3:30 AM IST
   - CSRF protection

4. **Rate Limiting**
   - Login: 5/min, 25/hour
   - Orders: 10/second
   - API calls: 50/second

5. **Browser Security**
   - Content Security Policy (CSP)
   - CORS protection
   - Secure headers

## 🎨 UI Themes

OpenAlgo MVP includes three beautiful themes:

- **Light Theme** - Default clean interface
- **Dark Theme** - Reduced eye strain for night trading
- **Garden Theme** - Special theme for analyzer mode

Switch themes instantly from the navbar!

## 🧪 API Analyzer (Sandbox Mode)

The API Analyzer lets you test trading strategies risk-free:

1. Enable Analyzer Mode in Settings
2. All orders execute in sandbox environment
3. Track virtual positions and P&L
4. Test strategies without financial risk

Perfect for:
- Strategy development
- Parameter optimization
- API integration testing
- Learning algorithmic trading

## 📊 Monitoring Tools

### Latency Monitor
Track order execution performance across brokers:
- Real-time latency tracking
- Success rate analysis
- Broker comparison

### Traffic Monitor
Monitor API usage and system performance:
- Endpoint-specific analytics
- Error rate tracking
- Performance metrics

### PnL Tracker
Real-time profit/loss visualization:
- Intraday P&L curves
- Maximum drawdown tracking
- Interactive TradingView charts

## 🔌 Broker Support

OpenAlgo MVP supports a plugin-based broker architecture. Add brokers by:

1. Creating a broker plugin in `/broker/[broker_name]/`
2. Implementing required API methods
3. Adding broker to `VALID_BROKERS` in `.env`

Supported broker operations:
- Authentication
- Order placement/modification/cancellation
- Market data fetching
- Position management
- WebSocket streaming

## 🤖 Integrations

### ChartInk
Execute ChartInk scanner strategies:
1. Configure ChartInk webhook URL
2. Set up strategy parameters
3. Automatic trade execution on signals

### TradingView
Webhook-based strategy execution:
1. Create TradingView alert
2. Configure webhook to OpenAlgo
3. Auto-execute trades from alerts

### Telegram Bot
Trade from Telegram:
1. Enable bot in Settings
2. Connect with `/start` command
3. Execute trades via chat commands
4. Get real-time notifications

## 📁 Project Structure

```
openalgo-mvp/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── package.json          # Node.js dependencies
├── .sample.env           # Environment template
├── blueprints/           # Flask blueprints (routes)
│   ├── auth.py          # Authentication
│   ├── dashboard.py     # Main dashboard
│   ├── orders.py        # Order management
│   ├── apikey.py        # API key management
│   ├── analyzer.py      # Sandbox/analyzer
│   ├── chartink.py      # ChartInk integration
│   ├── telegram.py      # Telegram bot
│   └── ...              # Other blueprints
├── broker/              # Broker plugins
├── database/            # Database models
├── restx_api/           # RESTful API
├── static/              # Static assets
│   ├── css/            # Compiled CSS
│   └── js/             # JavaScript files
├── templates/           # HTML templates
├── utils/               # Utility functions
├── websocket_proxy/     # WebSocket server
└── db/                  # SQLite databases
```

## 🔧 Configuration

Key environment variables in `.env`:

```bash
# Security (REQUIRED - Generate new values!)
APP_KEY='your-app-key-here'
API_KEY_PEPPER='your-pepper-here'

# Broker Configuration
VALID_BROKERS='zerodha,angelone,upstox,...'
BROKER_API_KEY='your-broker-api-key'
BROKER_API_SECRET='your-broker-secret'

# Server Configuration
FLASK_HOST_IP='127.0.0.1'
FLASK_PORT='5000'
FLASK_ENV='development'

# WebSocket Configuration
WEBSOCKET_PORT='8765'
ZMQ_PORT='5555'

# Database URLs
DATABASE_URL='sqlite:///db/openalgo.db'
LATENCY_DATABASE_URL='sqlite:///db/latency.db'
LOGS_DATABASE_URL='sqlite:///db/logs.db'
SANDBOX_DATABASE_URL='sqlite:///db/sandbox.db'

# Security Features
CORS_ENABLED='TRUE'
CSP_ENABLED='TRUE'
CSRF_ENABLED='TRUE'

# Rate Limiting
LOGIN_RATE_LIMIT_MIN='5 per minute'
API_RATE_LIMIT='50 per second'
ORDER_RATE_LIMIT='10 per second'
```

## 🚨 Important Notes

### Security
1. **ALWAYS** generate new `APP_KEY` and `API_KEY_PEPPER` values
2. **NEVER** commit `.env` file to version control
3. Use HTTPS in production (set `HOST_SERVER` to https URL)
4. Keep broker credentials secure

### Database
- SQLite is used by default (suitable for single-user)
- For production, consider PostgreSQL/MySQL
- Regular backups recommended for `db/` folder

### Development
- Set `FLASK_DEBUG='True'` for development
- Set `FLASK_ENV='production'` for production
- Use `LOG_LEVEL='DEBUG'` for troubleshooting

## 📖 Usage Examples

### Place an Order via API

```python
import requests

url = "http://127.0.0.1:5000/api/v1/placeorder"
headers = {"Content-Type": "application/json"}
data = {
    "apikey": "your-api-key",
    "strategy": "MyStrategy",
    "exchange": "NSE",
    "symbol": "RELIANCE",
    "action": "BUY",
    "quantity": "10",
    "price": "2500",
    "product": "MIS",
    "ordertype": "LIMIT",
    "position_size": "10"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

### Get Account Funds

```python
url = "http://127.0.0.1:5000/api/v1/funds"
data = {"apikey": "your-api-key"}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

### WebSocket Market Data

```javascript
const ws = new WebSocket('ws://127.0.0.1:8765');

ws.onopen = () => {
    // Authenticate
    ws.send(JSON.stringify({
        action: 'authenticate',
        api_key: 'your-api-key'
    }));
    
    // Subscribe to symbols
    ws.send(JSON.stringify({
        action: 'subscribe',
        symbols: ['NSE:RELIANCE', 'NSE:TCS'],
        mode: 'ltp'
    }));
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Market data:', data);
};
```

## 🐛 Troubleshooting

### Application won't start
- Check Python version: `python --version` (need 3.12+)
- Verify dependencies: `pip install -r requirements.txt`
- Check `.env` configuration
- Ensure port 5000 is available

### CSS not loading
- Run: `npm install`
- Build CSS: `npm run build`
- Check `static/css/main.css` exists

### WebSocket connection fails
- Check `WEBSOCKET_PORT` in `.env`
- Verify port 8765 is not blocked
- Check firewall settings

### Broker authentication fails
- Verify `BROKER_API_KEY` and `BROKER_API_SECRET`
- Check broker credentials are active
- Review broker-specific documentation

## 🤝 Contributing

This is an MVP version based on the original OpenAlgo project. Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

Key points:
- ✅ Free to use, modify, and distribute
- ✅ Must disclose source code
- ✅ Must use same license for derivatives
- ✅ Network use = distribution (must share source)

See [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This software is for **educational purposes only**. 

- Do NOT risk money you cannot afford to lose
- USE THE SOFTWARE AT YOUR OWN RISK
- Authors assume NO RESPONSIBILITY for trading results
- Test thoroughly in sandbox mode before live trading
- Consult financial advisors before trading

## 🙏 Credits

This MVP is based on [OpenAlgo](https://github.com/marketcalls/openalgo) by Marketcalls.

### Third-Party Libraries

- **[Flask](https://flask.palletsprojects.com/)** - Web framework (BSD-3-Clause)
- **[DaisyUI](https://github.com/saadeghi/daisyui)** - UI components (MIT)
- **[Tailwind CSS](https://tailwindcss.com/)** - CSS framework (MIT)
- **[TradingView Lightweight Charts](https://github.com/tradingview/lightweight-charts)** - Charting library (Apache 2.0)
- **[Socket.IO](https://socket.io/)** - Real-time communication (MIT)
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - Database ORM (MIT)
- **[Argon2](https://github.com/P-H-C/phc-winner-argon2)** - Password hashing (Apache 2.0)

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the original [OpenAlgo documentation](https://docs.openalgo.in)
- Join the [OpenAlgo Discord](https://discord.com/invite/UPh7QPsNhP)

## 🗺️ Roadmap

Future enhancements for this MVP:
- [ ] Add more broker integrations
- [ ] Enhanced backtesting capabilities
- [ ] Advanced charting features
- [ ] Mobile app support
- [ ] Multi-user support with PostgreSQL
- [ ] Cloud deployment guides
- [ ] Video tutorials

---

**Built with ❤️ for the algo trading community**

Made with [GitMVP](https://gitmvp.com) - AI-powered MVP generator
