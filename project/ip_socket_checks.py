import socket
import sys
import os
from netaddr import *
import math
import ip_checks as ic

def grab_banner(ip_address, port):
    try:
        s = socket.socket()
        s.connect((ip_address, port))
        banner = s.recv(1024)
        print
        ip_address + ':' + banner
    except:
        print str(port) + ":" + "is closed"
        return


def all_ports(ips):
    portList = [21, 22, 25, 80, 110, 443]
    for x in range(0, 255):
        for port in portList:
            ip_address = ips + str(x)
            print ip_address
            # ip_address = '192.168.0.' + str(x)
            grab_banner(ip_address, port)


def single_bunner(ip_address):
    portList = [21, 22, 25, 80, 110, 443]
    for port in portList:
        grab_banner(ip_address, port)
        # twenty_bunner()




def check_all_ip(data, player_ip_choice):#
    if ic.ipFormatChk(player_ip_choice) != True:
        return False
    print 'check_one_ip'
    '''
    total_ips = int(data[0][4])
    zeros = math.log(total_ips, 2)
    zeros = int(zeros)
    bits = 32 - zeros
    bits = str(bits)
    for ip in IPNetwork(data[0][2] + "/" + bits):
        print ip
        if ip == player_ip_choice:
            print ip
    '''
    for row in data:
        total_ips = int(row[4])#getting the amount of ip in the table
        zeros = math.log(total_ips, 2)#calculating the root of 2 of this number to know how many bit we need to subtract
        zeros = int(zeros)
        bits = 32 - zeros#subtracting from 32 bits (bits in ip)
        bits = str(bits)
        print "row" + row[2][-1]
        if row[-1] == " ":
            print "space"
            start_ip = row[2][:-1]#extra space in the table
        else:
            print "no space"
            start_ip = row[2]
        #start_ip = row[2][:-1]#extra space in the table
        for ip in IPNetwork(start_ip+"/"+bits):#going over the ip range that we got with netaddr lib
            single_bunner(ip)

# ip_address_main = raw_input('give me ip address: ')
# single_bunner('10.0.28.130')
# single_bunner(ip_address_main)
#ips = raw_input("give me ip range: ")
#all_ports(ips)









