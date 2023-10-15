# pi-monitor :pie:
## Project Description
This is a tiny network monitor that uses the 8x8 LED display on a Raspberry PI SenseHat.  You need a Raspberry Pi model B.  It shows a rolling graph of network utilization on the display.  It requires a router or switch that is capable of SNMP.  I am using a Netgear GS108E and monitoring the port leading to my router to see traffic.  I will be testing on pFsense soon and will be happy to help get other devices working.  Some TPLink devices support SNMP, but give invalid data.

### About the application
This application is written in Python and requires the easysmpe, and SenseHat modules.

I hope to add more error checking in future versions

### How to Install and Run
- You will need a Raspberry PI model B (2 test, 3,4 should work) with the SenseHat Pi Hat v1 or v2
- You will need to install Python and required modules

`$ pip3 install sense_hat easysnmp numpy`

`$ python monitor.py`

### Known issues
v1 or the SenseHat generates an error:
`WARNING:root:Failed to initialise TCS34725 colour sensor. (sensor not present)`
You can ignore this error as it doesn't affect the LED grid


Thanks to Kevin Hartle for help with code review and general advice.

Test commit/push after machine reinstall(s)
