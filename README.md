# **tft_bonnet**

## **Overview**
`tft_bonnet` is a showcase project that highlights my expertise in **Data Engineering**, **DevOps**, **Mechanical Engineering**, and **Electrical Engineering**. 

The goal of this project is to demonstrate my ability to design and implement a fully functional **Smart Thermostat**, capable of:
- Measuring and displaying real-time temperature and humidity.
- Integrating with Azure IoT Hub for data analysis and visualization.
- Automating deployments and services through DevOps principles.

---

## **Why This Project?**

This project is a blend of:
- **DevOps**: Automating deployments with Systemd services and CI/CD pipelines.
- **Data Engineering**: Integrating with Azure IoT Hub to enable data collection and real-time monitoring.
- **Mechanical Engineering**: Leveraging sensor technology for practical environmental monitoring.
- **Electrical Engineering**: Interfacing hardware like sensors and displays with Raspberry Pi.

---

## **Features**
- Real-time display of temperature and humidity on a 240x240 TFT screen.
- Button controls for interacting with the device.
- Sends data to a cloud IoT Hub for remote monitoring and IoT integration.
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
