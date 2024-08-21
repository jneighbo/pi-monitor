## pi-monitor :pie:
## Project Description
This is a tiny network monitor that uses the 8x8 LED display on a Raspberry Pi SenseHat to show network activity.  You need a Raspberry Pi model B.  It shows a rolling graph of network utilization on the display.  It requires a router or switch that is capable of SNMP.  I am using a Netgear GS108E and monitoring the port leading to my router to see traffic from the Internet.  I will be testing on pFsense soon and will be happy to help get other devices working.  
### About the application
This application is written in Python and requires the easysnmp and SenseHat modules.

![pi-monitor in use](https://github.com/jneighbo/pi-monitor/assets/33995623/e4bda6a9-0068-4355-80b7-5acfbc920427)




### How to Install and Run
- You will need a Raspberry PI model B (2 tested, 3 tested,4 should work) with the SenseHat Pi Hat v1 or v2.  It should work on a Libre le potato (B model compatible SBC)
- You will need to install Python and required modules

`$ sudo apt-get install libsnmp-dev snmp-mibs-downloader` 

`$ pip3 install sense_hat easysnmp numpy`

`$ python monitor.py`

### Known issues
v1 or the SenseHat generates an error:
`WARNING:root:Failed to initialise TCS34725 colour sensor. (sensor not present)`

You can ignore this error as it doesn't affect the LED grid

Some TPLink devices support SNMP, but give invalid data.

Thanks to Kevin Hartle his support.


