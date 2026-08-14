# Multi-stage Dockerfile for AWESOME_OKAPI_V2

# ==================== BUILD STAGE ====================
FROM python:3.11-slim AS builder

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    curl \
    wget \
    netcat-openbsd \
    nmap \
    nikto \
    dnsutils \
    traceroute \
    iputils-ping \
    hashcat \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ==================== RUNTIME STAGE ====================
FROM python:3.11-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    netcat-openbsd \
    nmap \
    nikto \
    dnsutils \
    traceroute \
    iputils-ping \
    hashcat \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN useradd -m -u 1000 awesome && \
    mkdir -p /app && \
    chown -R awesome:awesome /app

# Copy from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application
WORKDIR /app
COPY awesome_okapi_v2.py .
COPY entrypoint.sh .

# Create directories
RUN mkdir -p .awesome_okapi_v2 awesome_okapi_v2_reports && \
    chown -R awesome:awesome /app

# Set permissions
RUN chmod +x entrypoint.sh

# Expose ports
EXPOSE 5000 8080 8000-9000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Switch to app user
USER awesome

# Entry point
ENTRYPOINT ["/app/entrypoint.sh"]

# Default command
CMD ["python", "awesome_okapi_v2.py"]