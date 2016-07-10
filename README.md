# raspberry_sensors
Experimenting with IoT (Internet of Things) for Raspberry Pi

The purpose is to record various types of data, from sensors connected to a Raspberry Pi (v2 model B).
For the time being to the Pi there are connected:
- two Reed Switches - to be able to detect if 2 windows are opened or closed
- one temperature sensor (DS18B20) - to measure indoor temperature

All the sampled data is stored in a MySQL DB. From here the data can be plotted, interpreted and anylized.

Roadmap
- add an outdoor weather unit with temperature and humidity sensor (compute confort factor)
- add barometric pressure sensor (try weather prediction)
- add two more Reed Switches (differentiate between window fully opened and partially opened - flipped)
