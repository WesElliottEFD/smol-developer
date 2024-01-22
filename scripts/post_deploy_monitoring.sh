#!/bin/bash

# post_deploy_monitoring.sh
# Script to monitor the DevFusion application after deployment.

LOG_FILE="/var/log/devfusion_post_deploy.log"
DEPLOYMENT_STATUS_ENDPOINT="http://localhost/api/deployment_status"
FEEDBACK_ENDPOINT="http://localhost/api/feedback"
MONITOR_INTERVAL=60 # Monitor every 60 seconds

echo "Post-deployment monitoring started for DevFusion." | tee -a $LOG_FILE

# Function to check the deployment status
check_deployment_status() {
  echo "Checking deployment status..." | tee -a $LOG_FILE
  response=$(curl -s $DEPLOYMENT_STATUS_ENDPOINT)
  echo "Deployment status: $response" | tee -a $LOG_FILE
}

# Function to collect user feedback
collect_user_feedback() {
  echo "Collecting user feedback..." | tee -a $LOG_FILE
  feedback=$(curl -s $FEEDBACK_ENDPOINT)
  echo "User feedback: $feedback" | tee -a $LOG_FILE
  python3 scripts/feedback_collector.py "$feedback"
}

# Main monitoring loop
while true; do
  current_time=$(date)
  echo "[$current_time] Monitoring cycle initiated." | tee -a $LOG_FILE

  check_deployment_status
  collect_user_feedback

  echo "Waiting for $MONITOR_INTERVAL seconds before next check..." | tee -a $LOG_FILE
  sleep $MONITOR_INTERVAL
done