#!/bin/bash
# Entrypoint script for AWESOME_OKAPI_V2 Docker container

set -e

echo " Starting AWESOME_OKAPI_V2..."

# Set up environment
export PYTHONUNBUFFERED=1
export CONFIG_DIR="${CONFIG_DIR:-/app/.awesome_okapi_v2}"
export DATABASE_FILE="${DATABASE_FILE:-/app/.awesome_okapi_v2/awesome_okapi_v2.db}"
export LOG_FILE="${LOG_FILE:-/app/.awesome_okapi_v2/awesome_okapi_v2.log}"

# Create necessary directories
mkdir -p "$CONFIG_DIR"
mkdir -p /app/awesome_okapi_v2_reports

# Check if running as root
if [ "$(id -u)" -eq 0 ]; then
    echo "⚠️ Running as root. Use --user awesome for better security."
fi

# Run the application
exec python /app/awesome_okapi_v2.py "$@"