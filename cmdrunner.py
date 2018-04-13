"""runner.py
# Usage: python runner.py hosts.json commands.txt
# runs commands listed in commands.txt on all hosts listed in hosts.txt
# user is pormpted for name of file to save output in, or a default of <date>_<time>_hosts.json
# hosts.json should be one line dictionary for each host in the netmiko format
# {'<hostname>': {'ip'="0.0.0.0", 'device-type': "cisco-ios"}, }
#
# dependencies: json, netmiko
"""

# import future and get_input utility for Python 2.7/3 syntax compatability
from __future__ import absolute_import, division, print_function
from utilities import get_input

import netmiko
import json
import getpass
import sys

## TODO add code to read command line args for hosts.json and commands.txt, or display usage
hostfile = "2hosts.json"
commands = "commands.txt"
outfile = "20170125_1620_2hosts.json"

user = get_input("enter username: ")
password = getpass.getpass("Enter password: ")

has_password = (password is not None)
print("username: {username}; Password: {haspass}".format(username = user, haspass = str(has_password)))

hosts = """
10.0.0.1
10.1.1.1
""".strip().splitlines()
		
print(hosts)

device_type = "cisco_ios"

for host in hosts:
	connection = netmiko.ConnectHandler(ip=host, device_type=device_type, username = user, password=password)
	
	print("Host {host}: {cmdout}".format(host=host, cmdout=connection.send_command('show clock')))
	connection.disconnect
	
	