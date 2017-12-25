#!/usr/bin/env python
# -*- coding: utf-8 -*-
from netaddr import *
import pprint
import socket,struct
import math
from IPy import IP

def print_ips(data):#
    print 'check_one_ip'
    count = 0
    for row in data:
        #print row[2] + ' - ' + row[3]
        #str(len(row[2]))
        count+=1
        print str(count) + ' - ' + row[2] + ' - ' + row[3]
    return 1




def ipFormatChk(ip_str):#validates the ip
    if len(ip_str.split()) == 1:
        ipList = ip_str.split('.')
        if len(ipList) == 4:
            for i, item in enumerate(ipList):
                try:
                    ipList[i] = int(item)
                except:
                    return False
                if not isinstance(ipList[i], int):
                    return False
            if max(ipList) < 256:
                return True
            else:
                return False
        else:
            return False
    else:
        return False



def check_one_ip(data, player_ip_choice):#
    if ipFormatChk(player_ip_choice) != True:
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
        for ip in IPNetwork(start_ip+"/"+bits):#going over the ip range that we got with netaddr lib
            print ip
            if str(ip) == str(player_ip_choice):#comparing between them (it didnt work without the str())
                print "we found it"
                return True


    return False


def check_some_ip(data, player_ip_choice):#
    print 'check_some_ip'
    return 1


def check_all_ip(data, player_ip_choice):#
    print 'check_all_ip'
    return 1


def check_from_to(data, player_ip_choice,):#
    print 'check_one_ip'
    for row in data:
        math.log(row[4], 2)
        for ip in IPNetwork(player_ip_choice,):
            if ip == player_ip_choice:
                print row[2]
    return 1



def makeMask(n):
    "return a mask of n bits as a long integer"
    return (2L<<n-1) - 1

def dottedQuadToNum(ip):
    "convert decimal dotted quad string to long integer"
    return struct.unpack('L',socket.inet_aton(ip))[0]

def networkMask(ip,bits):
    "Convert a network address to a long integer"
    return dottedQuadToNum(ip) & makeMask(bits)

def addressInNetwork(ip,net):
   "Is an address in a network"
   return ip & net == net


#print math.log(16384,2)

#58.147.145.150
#58.147.129.200
'''

address = dottedQuadToNum("192.168.1.1")
networka = networkMask("10.0.0.0",24)
networkb = networkMask("192.168.0.0",24)
print (address,networka,networkb)
print addressInNetwork(address,networka)
print addressInNetwork(address,networkb)


'''