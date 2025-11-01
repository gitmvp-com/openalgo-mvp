FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js for Tailwind CSS
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt package.json package-lock.json* ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js dependencies
RUN npm install

# Copy application files
COPY . .

# Build Tailwind CSS
RUN npm run build

# Create necessary directories
RUN mkdir -p db log logs keys strategies

# Expose ports
EXPOSE 5000 8765

# Run the application
CMD ["python", "app.py"]
