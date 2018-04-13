## Collection of network python scripts
A collection of python network utility scripts.  Some 
of these script may require the netmiko package.
### 8821-speed.py
Cisco 8821 series speed dial list XML file generator.
Accepts a csv file of names and numbers and outputs an 
XML file for use on the 8821 phones.

This file can be loaded on a webserver for the phone to 
download a preprogrammed speed dial list.  Althogh this
can be created by users in Call Manager self-service 
portal, Larger organizations may manage this themselves.

### scrt-sessions.py
Script to walk a directory containing host ini files from
SCRT and extract hostnames and IP addresses into a json
file.  Input is a directory to start in, where each ini
file is named with the hostname.

The script is useful if historical connections have been 
made in SCRT and organized into files/folders.  This 
historical knowledge can be easily extracted into json
for use in other pythton scripts or automation tools.

