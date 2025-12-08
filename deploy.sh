#!/usr/bin/env bash
set -e

# This script runs on the EC2 host. It assumes docker & docker-compose (v1 or v2) are installed.
# Usage: chmod +x deploy.sh && ./deploy.sh

APP_DIR="${HOME}/student-api-deploy"
mkdir -p "${APP_DIR}"
# Copy everything from current working dir (scp will place files in ~/<target_dir>)
# If using action scp to upload to $APP_DIR, comment the next line
# cp -r . "${APP_DIR}/"

cd "${APP_DIR}"

# Ensure environment file exists (should be created or uploaded via secrets)
if [ ! -f ".env" ]; then
  echo "WARNING: .env not found in ${APP_DIR}. Please create a .env with MYSQL_ variables or configure docker-compose.prod.yml appropriately."
fi

# Pull latest images (if using remote registry) or build locally
docker compose -f docker-compose.prod.yml up -d --build

# Optional: prune unused images
docker image prune -f || true

echo "Deployment finished."
