import socket
import sys
import struct
import time
import binascii
import serial
import array as arr
import serial.tools.list_ports
i = 0
l = 0

okunan = arr.array('l',[0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,   
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0])
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print("\r")
    print(p)
with open("UDP_VCP_SerComm.bin", "w") as f:
    while 1:
        while 1:
            def setupSerial(UDPPort):
                ser = serial.Serial(port='COM6',baudrate=115200,bytesize=8,parity='N',stopbits=1,xonxoff=0,rtscts=0)
                return ser
            UDPPort = "COM6"
            ser = setupSerial(UDPPort)
            okunan = ser.read(342)
            i = i + 1
            denemeler = ("\n%d.packet:\t" %(i))
            print(denemeler)
            f.writelines(denemeler)
            for l in range (342):
                s = ("0x%02X" % (okunan[l]))
                f.writelines(s)
                f.write(" ")
                print(s,end="  ")
            ser.close() 
            break
    f.close()


 