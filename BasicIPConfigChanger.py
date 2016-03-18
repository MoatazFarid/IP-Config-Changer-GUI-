import os,subprocess

cmd = ['sudo', 'ifconfig', 'eth0', '192.168.1.21','netmask' ,'255.255.255.0']

proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
cmd = ['sudo', 'route', 'add', 'default','gw' ,'192.168.1.1','eth0']

proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)