Author: Christian Holmström <br>
ID:ch223wu

# Temperature and Humidity Sensor IOT
 <p align="center">

 
## Overview
This project is about measuring temperature and humidity and displaying their current values, as well as monitoring how these values change over time. 
It is designed for beginners and can be completed within an estimated time frame of 2-3 hours, following this tutorial.

## Objective
The purpose of this project is to enable real-time monitoring of temperature and humidity, as well as logging the sensor data for analysis over time. 
This system provides valuable insights into the environment being monitored. 
For instance, it can be utilized to track temperature and humidity levels on a balcony during the summer or to observe the impact of a running PC on room temperature in an office setting.

## Material
For this project, we will be working with the Raspberry Pi Pico WH microcontroller. 
The Raspberry Pi Pico WH offers numerous digital and analog input and output pins, along with a 2.4GHz wireless interface. For detailed information about the Pico WH, please refer to the datasheet.

To measure temperature and humidity, we have selected the DHT11 Humidity & Temperature Sensor, which provides a digital output. 
It has a measurement range of 0-50°C (32-122°F) for temperature and 20-90% RH (Relative Humidity) for humidity, which is suitable for this project.

In addition, we will need a breadboard and a few jumper wires to connect all the components together. 
To power the Raspberry Pi Pico WH, we will use a micro-USB cable, which will also allow us to connect it to our PC for programming and data transfer.

|    | Material | Price (SEK) |
|----|----------|-------------|
| <img src='https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/pico_109.webp?raw=true' width=150> | Raspberry Pi Pico WH | 109 |
| <img src='https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/dht11_49.jpg?raw=true' width=150> | DHT11 | 49 |
| <img src='https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/breadboard_69.jpg?raw=true' width=150> | Breadboard           | 69  |
| <img src='https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/jumper_29.jpg?raw=true' width=150> | Jumper cables M-to-M | 29  |
| <img src='https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/microusb_19.webp?raw=true' width=150> | micro-USB cable | 19 |

## Computer setup
For the IDE, we will be using Visual Studio Code. It provides a robust and user-friendly coding environment. 
Additionally, we will utilize the PyMakr extension, which enables code uploading to the Raspberry Pi Pico WH. 
To use the PyMakr extension, it is necessary to install Node.js.

### Step-by-step
1.Install Python if you don't already have it installed on your computer. You can download the latest version of Python from the official Python website (https://www.python.org) and follow the installation instructions provided.

2.Download and install Node.js. Visit the official Node.js website (https://nodejs.org) and download the current version (not LTS) of Node.js that is compatible with your operating system. Follow the installation instructions to complete the setup.

3.Download and install the Visual Studio Code IDE (VSCode) from the official website (https://code.visualstudio.com). Choose the appropriate version for your operating system and follow the installation instructions.

4.Open Visual Studio Code and navigate to the Extensions Marketplace. Search for the "PyMakr" extension and install it. This extension enables communication and code uploading to the Raspberry Pi Pico from within Visual Studio Code.

5.Update the firmware on the Raspberry Pi Pico:
a. Download the MicroPython firmware in .uf2 format. Make sure to get the latest stable version from the Releases section and not the Nightly builds. You can find the firmware on the official Raspberry Pi Pico GitHub repository (https://github.com/raspberrypi/pico-micropython-examples/releases).
b. Connect the micro-USB cable to the Raspberry Pi Pico.
c. While holding down the BOOTSEL button on the board, connect the other end of the micro-USB cable to your computer. Once it's plugged in, you can release the BOOTSEL button.
d. A new drive named "RPI-RP2" or similar should appear in your file system. This is the Raspberry Pi Pico's storage.
e. Move the downloaded .uf2 firmware file into this storage. It will automatically trigger the firmware update process.
f. Wait for the board to disconnect and reconnect automatically.


By following these steps, you will have Python, Node.js, Visual Studio Code, the PyMakr extension, and the latest MicroPython firmware set up for your Raspberry Pi Pico. You are now ready to start coding and uploading programs to your microcontroller.

## Putting everything together
This diagram showcases the process of connecting the DHT11 sensor to the Raspberry Pi Pico WH using a breadboard. In this diagram i used a dht22 because the program i used diden't have dht11 as a sensor.


<img src = 'https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/Sensor_Diagram.png?raw=true'>

## Platform
The chosen platform for this project is Adafruit. 
It provides a user-friendly and free platform that is well-suited for beginners. 
Adafruit offers simple visualizations to present your data effectively.

To get started, we need to set up an account on Adafruit IO. 
This account will allow us to utilize the platform's features for data logging and visualization. 
Once registered, we can create two separate feeds—one for temperature and another for humidity. 
The process of setting up feeds is detailed in the instructions available on the Adafruit website.

By following the provided instructions, we can easily create feeds on Adafruit IO for temperature and humidity. 
These feeds will serve as repositories for storing and organizing the sensor data collected by the Raspberry Pi Pico WH. 
We can then utilize Adafruit's visualization tools to present the data in a clear and understandable manner.

## Code
We organize our code using a standard structure that should be followed when creating projects. 

<img src="https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/Code_Structure.png?raw=true" width="200">


I have divided my code into four files to organize and separate different parts of my project:

Boot: Handles WiFi connection with configuration settings and connection code.

[Click here to view the boot.py file](https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/picow-micropthon/boot.py)


Secrets: Stores sensitive information such as WiFi network name and password separately to protect them.

[Click here to view the secrets.py file](https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/picow-micropthon/secrets.py)


MQTT: Contains MQTT-related functions and settings for communication with the MQTT broker.

[Click here to view the mqtt.py file](https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/picow-micropthon/mqtt.py)

Main: This is where the main code for my project resides, including importing the other files, sensor readings, data transmission, and other project-specific functions.

[Click here to view the main.py file](https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/picow-micropthon/main.py)


## Transmitting data

We use WiFi and MQTT protocols to transmit temperature and humidity data from the Raspberry Pi Pico WH to Adafruit. 
Data is sent every 20 seconds for real-time monitoring and long-term analysis purposes.

## Presenting data
Now that we have successfully set up our Raspberry Pi Pico to send weather data to our feeds on Adafruit, we can visualize this data using the Adafruit platform.
We have created a dashboard on Adafruit that utilizes the two feeds we previously set up.


<img src='https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/AdaFruit_Temp_Hum.png?raw=true' width = 800 height = 400>


## Final thoughts and design

The project is very simple, but sense i have never used IOT and sensors i decieded to stick with a temperature and humidty project. 
I do feel more incluined to do something more advanced in the future now that i know the basic.

<img src = 'https://github.com/BraveParrot-8/Temperature_Humidity_Sensor_IOT/blob/main/img/Final_Project.jpg?raw=true' width =900 height = 600>



