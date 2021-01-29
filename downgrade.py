#!/usr/bin/env python3
'''Run script with 2 params:
@password = ssh password found in site settings
@ip = ip address of uap'''
from paramiko import SSHClient
import sys

#python3 downgrade.py 192.168.1.2 askjdnkjeu23jaw

USERNAME = "admin"
PASSWORD = sys.argv[2]
IP = sys.argv[1]
client = SSHClient()
COMMAND = "upgrade https://dl.ui.com/unifi/firmware/U7PG2/4.3.20.11298/BZ.qca956x.v4.3.20.11298.200704.1347.bin"

client.connect(IP, username=USERNAME, password=PASSWORD)
stdin, stdout, stderr = client.exec_command(COMMAND)
reply = stdout.readlines()
print(reply)
client.close()
