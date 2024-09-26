## pi-monitor :pie:

### Project Description
`pi-monitor` is a lightweight network monitor that utilizes the 8x8 LED display on a Raspberry Pi Sense HAT to visualize network activity. The application is designed for Raspberry Pi Model B (versions 2 and 3 tested; version 4 is expected to work as well). It provides a rolling graph of network utilization on the display. The project requires a router or switch capable of SNMP (Simple Network Management Protocol). I am currently using a Netgear GS108E switch and monitoring the port that connects to my router to track internet traffic. Testing with pfSense is planned, and I am open to assisting with other device setups.

### About the Application
This application is written in Python and depends on the `easysnmp` and `SenseHat` modules.

![pi-monitor in use](https://github.com/jneighbo/pi-monitor/assets/33995623/e4bda6a9-0068-4355-80b7-5acfbc920427)

### Installation and Setup

#### Requirements:
- A Raspberry Pi Model B (versions 2 and 3 tested, 4 expected to work)
- Raspberry Pi Sense HAT (version 1 or 2)
- A compatible SBC like Libre Computer's Le Potato (optional)

#### Steps to Install:
1. Install Python 3 and the required dependencies on your Raspberry Pi:
   ```bash
   sudo apt-get install libsnmp-dev snmp-mibs-downloader
