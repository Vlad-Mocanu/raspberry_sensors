# raspberry_sensors
Experimenting with IoT (Internet of Things) for Raspberry Pi

## Description 

The purpose is to record various types of data, from sensors connected to a Raspberry Pi (v2 model B).
For the time being to the Pi there are connected:
- two Reed Switches - to be able to detect if 2 windows are opened or closed
- one temperature sensor (DS18B20) - to measure indoor temperature
- one outdoor weather unit with temperature, barometric pressure and humidity sensor (BME280)

All the sampled data is stored in a MySQL DB. From here the data can be plotted, interpreted and anylized.
The front-end application for Android is https://github.com/Vlad-Mocanu/RaspbiAtHome.

## Requirements

The development was done on a Raspberry Pi v2 model B, running Raspbian.

To install the package and its dependencies, you can run:
```
git clone https://github.com/Vlad-Mocanu/raspberry_sensors/
pip install raspberry_sensors/
````

## Usage

After you navigate to raspberry_sensors/raspberry_sensors, in order to run, you can use:
```
python record_all_sensors.py
```
    
The default configuration file is raspberry_sensors/raspberry_sensors/sensors_config.json. This file can be edited to adjust the program to your needs. In order to use another configuration file, other than the default one you can run it like this:
```
python record_all_sensors.py --config_file <path_to_config_file>
```

For more info you can consult the wiki of this repository.
