# pi-monitor
## Project Description
This is a tiny network monitor that uses the 8x8 LED display on a Raspberry PI SenseHat.  It shows a rolling graph of network utilization on the display.  I requires a router or switch that is capable of SNMP.  I am using a Netgear GS108E and monitoring port leading to my router to see traffic.  I will be testing on pFsense soon and will be happy to help get other devices working.  Some TPLink devices support SNMP, but give invalid data.

### About the application
This application is written in Python and requires the easysmpe, and SenseHat modules.

I hope to add more error checking in future versions

### How to Install and Run
- You will need a Raspberry PI with the SenseHat Pi Hat
- You will need to install Python and required modules

`$ pip install pip3 install sense_hat easysnmp numpy`
`$ python monitor.py`
  

Thanks to kevin@harle.org for help with code review and general advice.
