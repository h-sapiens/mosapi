About:  

Mosapi is a simple, lightweight microservice that can be run on a linux server, or linux IOT device. Its purpose is to provide simple interface to control the device through a REST API.

Current features: 
- Endpoint to reboot.
- Endpoint to shutdown.
- Endpoint to ping another device in the same LAN.
- Endpoint to exit the program.

The features are developed with security in mind, as it doesn't let you send commands directly from url or forms, if so, they should be validated. 

If you want to contribute please do so accordingly with security in mind and as the license states. 

Requires:
- python3
- web.py v0.62 at system level (sudo for linux)  

  - Linux: 
```
sudo python3 -m pip install web.py==0.62
```

To run Mosapi just:
```
python3 mosapi.py
```
or for winfows with python3:
```
python mosapi.py
```

Use Cases:  
- Ping:  
  - By device name calling GET`/your/path/to/ping/{device_name}`.
  - Any device in the LAN by addressing the last slot of the ip addres (e.g.  `x.x.x.*this`)  calling GET`/your/path/to/ping/ip/{last_slot}`.

Setup: 
- Rename file `./config.base.json` to `./config.json` and setup your configuration.
- Optional (Linux): Create user to run script.
  - Add user enough permissions:
    - Reboot, shutdown : version 1.0
    - Create user `sudo useradd username`
    - Add reboot permissions to `sudo visudo` `/etc/sudoers.d/reboot_privilege` with  `UserName ALL=(root) NOPASSWD: /sbin/reboot, /sbin/shutdown` at the EOF.
- Optional (Linux): Make it start at boot:.
  - Add command to crontab.
    - For specific user (Examples): 
        - On terminal `crontab -e -u username`
        - Add `@reboot cd /path/to/Mosapi/ && /usr/bin/python3 mosapi.py` at the EOF.          
        - Alternatively:
          - making the file executable with `chmod +x script.py` 
          - Add `@reboot cd /path/to/Mosapi && ./mosapi.py`  at the EOF.
        - We are adding a `cd` first so the server can be ignited.

