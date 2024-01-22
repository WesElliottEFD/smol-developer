#!/bin/bash

# Deployment script for DevFusion app

# Exit on any error
set -e

# Define the base directory for the project
BASE_DIR="$(dirname "$0")/.."

# Navigate to the base directory
cd "$BASE_DIR"

# Ensure we are on the main branch and up to date
git checkout main
git pull origin main

# Update name references in the codebase
echo "Updating name references from Smol-Developer to DevFusion..."
python3 src/utils/name_updater.py

# Integrate UI components from BloopAI
echo "Integrating UI components from BloopAI..."
python3 src/utils/integrateUIComponents.py

# Upgrade to GPT-4 Turbo
echo "Upgrading AI model to GPT-4 Turbo..."
python3 src/utils/upgradeToGPT4Turbo.py

# Build the frontend
echo "Building the frontend..."
cd src/frontend
npm install
npm run build
cd "$BASE_DIR"

# Run tests to ensure everything is working as expected
echo "Running tests..."
python3 src/tests/integration_tests.py
python3 src/tests/backend/model_tests.py
python3 src/tests/backend/api_tests.py
python3 src/tests/frontend/component_tests.js
python3 src/tests/name_consistency_tests.py

# Deploy to the server
echo "Deploying the application..."
# Add deployment commands here, e.g., scp, rsync, or cloud provider CLI commands

# Monitor deployment
echo "Monitoring deployment..."
bash scripts/post_deploy_monitoring.sh

# Collect user feedback
echo "Setting up feedback collection..."
python3 scripts/feedback_collector.py

echo "Deployment of DevFusion app completed successfully."

# End of deploy.sh script