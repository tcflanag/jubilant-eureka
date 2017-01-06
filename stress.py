import socket
from struct import *
import time
import serial
import datetime


r1,g1,b1,i1 = (0xff,0,0,127)
r2,g2,b2,i2 = (1,0,0,127)
r3,g3,b3,i3 = (1,55,0,4)
r4,g4,b4,i4 = (55,55,1,4)
UDP_IP = "192.168.1.255" #"192.168.1.112"
UDP_PORT = 0x1936
s = serial.Serial('COM8',baudrate=115200)

for skew in range(0,180):
    MESSAGE = pack("8sHHBBBBH","Art-Net\0",0,0,0,0,0,0,0)
    for i in range (skew,skew+180):
        #MESSAGE += pack("B",0)*(530-len(MESSAGE))
        if (i/30)%2:
            MESSAGE += pack("BBB",255,0,0)
        else:
            MESSAGE += pack("BBB",0,255,0)                
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP            
MESSAGE = " "
x = 0
time.sleep(5)
while 1:
    x+=1
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    if s.in_waiting:
        print 
        while s.in_waiting:   
            print str(datetime.datetime.now()),s.readline(),
        x=0
        print('\a')
        time.sleep(5)
    if x%1000 == 0: 
        print("    %dk packets sent  \r"%(x/1000)),
        
        
    
    