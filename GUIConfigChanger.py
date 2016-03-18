# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from Tkinter import * 
import os,subprocess

def applyConfig():
    ipAddressVar = ipAddress.get()
    subnetMaskVar = subnetMask.get()
    gatewayVar = gateway.get()
    interfaceNameVar = interfaceName.get()
    
    
    cmd = ['ifconfig', interfaceNameVar , ipAddressVar ,'netmask' ,subnetMaskVar ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    cmd = ['route', 'add', 'default','gw' , gatewayVar ,interfaceNameVar ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return
    
    
root = Tk() #create GUI 

MainTitle = Label(root , text="Configure Your NIC" , fg="red").grid(row =0  ,column = 1)
root.title("Configuration")
root.geometry("300x150")

ipAddress = StringVar()
subnetMask = StringVar()
gateway = StringVar()
interfaceName = StringVar()

#ip address 
ipaddLabel = Label(root , text="IP Address").grid(row=2,column=0)
ipstr = Entry(root , textvariable=ipAddress ).grid(row=2,column=1)
ipstr.insert(0,"192.168.1.122") #default value

#subnet mask
SubnetLabel = Label(root , text="Subnet Mask Address").grid(row=3,column=0)
subnetstr = Entry(root , textvariable=subnetMask ).grid(row=3,column=1)
subnetstr.insert(0,"255.255.255.0") #default value

#gateway address
gatewayLabel = Label(root , text="Gateway Address").grid(row=4,column=0)
gatewaystr = Entry(root , textvariable=gateway ).grid(row=4,column=1)
gatewaystr.insert(0,"192.168.1.1") #default value

#interface Name
interfaceLabel = Label(root , text="Interface Name").grid(row=6,column=0)
interfacestr = Entry(root , textvariable=interfaceName ).grid(row=6,column=1)
interfacestr.insert(0,"eth0") #default value

#Apply Configuration Btn 
applyBtn = Button(root, text="Apply", command =applyConfig).grid(row=8,column=1)

#powered By ASU Engineering
PoweredBy = Label(root , text="Powered By @AsuEng" , fg="red").grid(row=9,column=1)

root.mainloop() #mainLoop

