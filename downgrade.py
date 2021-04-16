#!/usr/bin/env python3
'''Run script with 2 params:
@password = ssh password found in site settings
@ip = ip address of uap'''
import paramiko
import sys
import time

#python3 downgrade.py 192.168.1.2 askjdnkjeu23jaw

USERNAME = "admin"
PASSWORD = sys.argv[1]
#IP = sys.argv[1]

iplist = [ x.strip() for x in open ('iplist.txt').read().split('\n') if x ]

for ip in iplist:
	print("Connecting to " + ip + "...")
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	COMMAND = "mca-cli-op upgrade https://dl.ui.com/unifi/firmware/U7PG2/4.3.20.11298/BZ.qca956x.v4.3.20.11298.200704.1347.bin"
	client.connect(ip, username=USERNAME, password=PASSWORD)
	stdin, stdout, stderr = client.exec_command(COMMAND)
	reply = stdout.readlines()
	reply2 = stdout.readlines()
	print(reply)
	print(reply2)
	client.close()
	print("Waiting for connection to close - may take up to 1 minute")
	time.sleep(60)
