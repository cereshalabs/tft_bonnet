# **tft_bonnet**

## **Overview**
`tft_bonnet` is a Python-based project for a **Smart Thermostat**. The goal is to create a mobile thermometer that displays the current temperature and humidity on a built-in screen and sends this data to an Azure IoT Hub.

This project is designed for use with Raspberry Pi and an ST7789VW-based display.

---

## **Features**
- Real-time display of temperature and humidity on a 240x240 TFT screen.
- Button controls for interacting with the device.
- Sends data to an Azure IoT Hub for remote monitoring and IoT integration.
- Service integration for automatic startup and monitoring.

---

## **Project Structure**
```plaintext
tft_bonnet/
├── docs/                 # Placeholder for future project documentation
│   └── Documentation.md  # Instructions and additional details
├── services/             # Systemd and deployment scripts
│   ├── deploy_custom_service.sh  # Script to deploy the service
│   └── smart_sensor.service       # Systemd service file for automation
├── src/                  # Main source code
│   ├── blinkatest.py                 # Script to test the display
│   ├── rgb_display_pillow_bonnet_buttons.py  # Button and display control script
│   └── smart_sensor.py               # Main application for the smart thermostat
├── tests/                # Test scripts
│   ├── blinkatest.py
│   ├── rgb_display_pillow_bonnet_buttons.py
│   └── test_sensor.py
├── .gitignore            # Git ignore rules
├── LICENSE               # Project license
├── README.md             # This README file
