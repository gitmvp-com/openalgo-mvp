# OpenAlgo MVP - Installation Guide

## Quick Start

### Prerequisites

- Python 3.12 or higher
- Node.js 18+ (for Tailwind CSS)
- Git

### Installation Steps

#### 1. Clone Repository

```bash
git clone https://github.com/gitmvp-com/openalgo-mvp.git
cd openalgo-mvp
```

#### 2. Set Up Python Environment

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

#### 3. Set Up Frontend

```bash
# Install Node.js dependencies
npm install

# Build Tailwind CSS
npm run build
```

#### 4. Configure Environment

```bash
# Copy sample environment file
cp .sample.env .env

# Generate security keys
python -c "import secrets; print('APP_KEY=' + secrets.token_hex(32))"
python -c "import secrets; print('API_KEY_PEPPER=' + secrets.token_hex(32))"

# Edit .env and update:
# - APP_KEY (use generated value)
# - API_KEY_PEPPER (use generated value)
# - BROKER_API_KEY (your broker's API key)
# - BROKER_API_SECRET (your broker's API secret)
```

#### 5. Run Application

```bash
python app.py
```

Access at: http://127.0.0.1:5000

## Docker Installation

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access at http://localhost:5000
```

## Production Deployment

### Using Gunicorn

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Nginx (Reverse Proxy)

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

## Troubleshooting

### Database Issues

```bash
# Remove database and recreate
rm -rf db/
python app.py
```

### CSS Not Loading

```bash
# Rebuild CSS
npm run build
```

### Port Already in Use

```bash
# Change port in .env
FLASK_PORT=5001
```

## Next Steps

1. Register a new account
2. Get your API key from Settings
3. Configure broker credentials
4. Start making API requests!

For detailed API documentation, see [README.md](README.md).
