#!/bin/bash

# Define variables
SERVICE_NAME="smart_sensor.service"
SOURCE_DIR="/home/pi/projects/tft_bonnet/services"
DEST_DIR="/etc/systemd/system"

# Check if the service file exists in the source directory
if [ ! -f "$SOURCE_DIR/$SERVICE_NAME" ]; then
  echo "Error: $SERVICE_NAME not found in $SOURCE_DIR."
  exit 1
fi

# Copy the service file to the systemd directory
echo "Copying $SERVICE_NAME to $DEST_DIR..."
sudo cp "$SOURCE_DIR/$SERVICE_NAME" "$DEST_DIR/"

# Set correct ownership and permissions
echo "Setting ownership and permissions for $SERVICE_NAME..."
sudo chown root:root "$DEST_DIR/$SERVICE_NAME"
sudo chmod 644 "$DEST_DIR/$SERVICE_NAME"

# Reload systemd manager configuration
echo "Reloading systemd manager configuration..."
sudo systemctl daemon-reload

# Enable the service to start on boot
echo "Enabling $SERVICE_NAME..."
sudo systemctl enable "$SERVICE_NAME"

# Restart the service to apply changes
echo "Restarting $SERVICE_NAME..."
sudo systemctl restart "$SERVICE_NAME"

# Check the status of the service
echo "Checking the status of $SERVICE_NAME..."
sudo systemctl status "$SERVICE_NAME"

# Print completion message
echo "Service $SERVICE_NAME has been copied, permissions set, scheduled, and started successfully."
