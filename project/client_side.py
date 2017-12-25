#!/usr/bin/env python
# -*- coding: utf-8 -*-
import test_url as tu
import time
import sql_database_fun as sf
import dec_bin as debi
import ip_checks as ic
import ip_socket_checks as isc

def create_new_user(c):
    check = True
    while check == True:
        print 'lets create new user'
        print 'enter user name'
        user_name = raw_input()
        print 'enter password'
        password = raw_input()
        if ((sf.check_password(user_name, password, c) == -1) or (sf.check_password(user_name, password, c) == 0)):  # מחזיר 1- אם הוא לא קיים
            check = False
        else:
            print "we already have this user name!!! choose other one"
    list = [user_name, password]
    sf.dynamic_data_entry_user(list, c, conn)  # adding new user
    sf.close_sql_connection(c, conn)
    print'hello ' + user_name + 'we are glad to have you here'


def login_user(user_name_log,password_log, c):
    if(sf.check_password(user_name_log, password_log, c)==2):
        return False
    else:
        print "the password or the user name are wrong"
        return True



def users_opetions():
    print 'what would you like to do?'
    print 'choose your action'
    print '1 - take a country (you can choose what you want to do with it)'
    print '2 - taking ip from to/total ips/taking ip by date/owner'
    print '3 - scanning one/some/all ports'
    print '4 - create/update database'
    #print 'what country would you like?'
    player_option = raw_input()
    player_option = str(player_option)

    return {
        '1': ['what country would you like to search for?',1,find_user_desired_country],
        '2': ['a',2],
        '3': ['a',3],
        '4': ['updating database',4,update_database],
        '5': ['a',5],
        '6': ['a',6],
    }.get(player_option, -1)

def update_database(user_string):#4 updating database
    print 'it works'
    time.sleep(0.5)
    print user_string[0]
    time.sleep(1)

    tu.create_database()
    return [] #no information has to be given back


#####
def find_user_desired_country(user_string):
    data = []
    while len(data) == 0:
        print user_string[0]
        user_country = raw_input()
        user_country = str(user_country)
        c1, conn1=sf.create_sql_connection('country_database.db')
        data = sf.find_counry_by_name(user_country, c1)
        if len(data)==0:
            print 'put a valid country'
    #print data
    return data

def users_opetions2():
    print 'what would you like to do?'
    print 'choose your action'
    print '1 - choose 1 ip)'
    print '2 - choose some ip'
    print '3 - all ips'
    print '4 - start ip to end ip'
    #print 'what country would you like?'
    print 'what would you like to do'
    player_option2 = raw_input()
    player_option2 = str(player_option2)
    return {
               '1': ['choose 1 ip', 1, ic.check_one_ip],
               '2': ['choose some ip', 2, ic.check_some_ip],
               '3': ['all ips',3, ic.check_all_ip],
               '4': ['start ip to end ip', 4, ic.check_from_to],
           }.get(player_option2, -1)

#####


'''
    print 'what would you like to do'
    player_option2 = raw_input()
    player_option2 = str(player_option2)
    return {
        '1': ['', 1, find_user_desired_country],
        '2': ['a', 2],
        '3': ['a', 3],
        '4': ['updating database', 4, update_database],
        '5': ['a', 5],
        '6': ['a', 6],
    }.get(player_option2, -1), data
'''

#main
#print debi.check_dec_bin(100)
c, conn = sf.create_sql_connection('user_database')
sf.create_table_user(c, conn)
print 'hello and welcome to our data base'
print 'are you a new user?'
print 'enter y/n'
yes = raw_input()
yes = str(yes)
while yes != 'n' or yes == 'y':
    print 'enter y/n'
    yes = raw_input()
    yes = str(yes)
if yes == 'y':
    create_new_user(c)
else:
    b = True
    while b == True:
        print 'enter user name to login'
        user_name = raw_input()
        print 'enter password'
        password = raw_input()
        # password = int(password)
        b = login_user(user_name, password, c)
continue_bol = True
while continue_bol == True:
    user_string_input = users_opetions()#asking user for his choice
    table_data = user_string_input[2](user_string_input) #doing what the user wants with taking the data from the dic and activating the fun from the dic data
    if len(table_data)==0:#table data contain the all data table from what the user has chosen
        print 'we finished your request'
    else:
        print '+'
        print 'what do you want to do with the data?'
        user_string_input2 = users_opetions2()
        ic.print_ips(table_data)
        if user_string_input2[1] == 1:
            check_bol = False
            while check_bol != True:
                print 'choose ip'
                user_ip = raw_input()
                user_ip = str(user_ip)
                check_bol = user_string_input2[2](table_data, user_ip)
                print check_bol
                if (check_bol == False):
                    print "we do'nt have "+ user_ip +" in the ip range!"
            print "scanning"
            print user_ip
            isc.single_bunner(user_ip)
        if user_string_input2[1] == 2:#some
            print '2'
        if user_string_input2[1] == 3:#all
            check_bol = False
            while check_bol != True:
                print 'choose ip'
                user_ip = raw_input()
                user_ip = str(user_ip)
                check_bol = user_string_input2[2](table_data, user_ip)
                if (check_bol == False):
                    print "we do'nt have " + user_ip + " in the ip range!"
            isc.check_all_ip(table_data, user_ip)
            print '3'
        if user_string_input2[1] == 4:
            print '4'


    print 'would you like to continue? y/n'
    user_choice = raw_input()
    user_choice = str(user_choice)
    if user_choice != 'y':
        continue_bol=False




