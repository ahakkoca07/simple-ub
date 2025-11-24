FROM python:3.11-slim

# Install system dependencies
# RUN apt-get update && apt-get install -y \
#   speedtest-cli neofetch \
#    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "main.py"]
