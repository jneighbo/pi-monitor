## pi-monitor :pie:

### Project Description

`pi-monitor` is a lightweight network monitor that utilizes the 8x8 LED display on a Raspberry Pi Sense HAT to visualize network activity. The application is designed for Raspberry Pi Model B (versions 2 and 3 tested; version 4 is expected to work as well). It provides a rolling graph of network utilization on the display. The project requires a router or switch capable of SNMP (Simple Network Management Protocol). I am currently using a Netgear GS108E switch and monitoring the port that connects to my router to track internet traffic. Testing with pfSense is planned, and I am open to assisting with other device setups.

### About the application
This application is written in Python and requires the easysnmp and SenseHat modules.

![pi-monitor in use](https://github.com/jneighbo/pi-monitor/assets/33995623/e4bda6a9-0068-4355-80b7-5acfbc920427)

### How to Install and Run
You will need a Raspberry PI model B (2 tested, 3 tested,4 should work) with the SenseHat Pi Hat v1 or v2. It should work on a Libre le potato (B model compatible SBC)
You will need to install Python and required modules


``` $ sudo apt-get install libsnmp-dev snmp-mibs-downloader ```

``` $ pip3 install sense_hat easysnmp numpy ```

``` $ python monitor.py ```


Known issues
v1 of the SenseHat generates an error: WARNING:root:Failed to initialise TCS34725 colour sensor. (sensor not present)

You can ignore this error as it doesn't affect the LED grid

Some TPLink devices support SNMP, but give invalid data.

