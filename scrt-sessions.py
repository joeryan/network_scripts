# scrt-sessions.py
# extract from folder structure all hosts with hostnames and IP addresses
# each configuration file in the directories are assumed to be named with the hostname
# Hostname field within each ini file is assumed to have IP address or DNS resolvable hostname
# write out a json file with each host, IP address in a list

import os, glob
import re
import json

files = []
locations = []
hosts = {}
hostregex = re.compile("S:\"Hostname")
root = input("enter directory to start walking for SCRT files: ")
if root == '' or root == '.':
  root = os.getcwd()

for (dirpath, dirnames, filenames) in os.walk(root):
    locations.extend(os.path.join(root, dirpath, dirname)for dirname in dirnames)
    break


for location in locations:
    os.chdir(location)
    for file in glob.glob("*.ini"):
        if file.endswith(".ini") and not file.startswith("__"):
            hostname = file.split(".")[0]
            with open(os.path.join(root, location, file), 'r') as infile:
                for line in infile.readlines():
                    if hostregex.match(line):
                        ip_addr = line.split('=')[-1].strip()
                        hosts[hostname] = dict([('hostname',hostname),('ipaddr',ip_addr)])
    os.chdir('../')

with open('hostlist.json', 'w') as outfile:
    json.dump(hosts, outfile)
