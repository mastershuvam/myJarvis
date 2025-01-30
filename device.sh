# filepath: /Users/shuvamghosh/Desktop/MyJervis/device.sh
#!/bin/bash

echo "Disconnecting old connections..."
adb disconnect
echo "Setting up connected device"
adb tcpip 5555
echo "Waiting for device to initialize"
sleep 3
ipfull=$(adb shell ip addr show wlan0 | grep "inet " | awk '{print $2}')
ip=${ipfull%%/*}
echo "Connecting to device with IP $ip..."
adb connect $ip

# Set the IP address of your Android device
DEVICE_IP=192.0.0.4

# Set the port number for ADB
ADB_PORT=5555

# Set the path to the ADB executable
ADB_PATH="adb"

# Restart the ADB server
$ADB_PATH kill-server
$ADB_PATH start-server

# Connect to the Android device over Wi-Fi
$ADB_PATH connect $DEVICE_IP:$ADB_PORT

