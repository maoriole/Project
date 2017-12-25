#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import time
#import datetime
#import random
from sqlite3 import Cursor


def create_sql_connection(databasename):
    #conn = sqlite3.connect('country_database.db')
    conn = sqlite3.connect(databasename)
    c = conn.cursor()
    return c, conn

def close_sql_connection(c, conn):
    c.close
    conn.close()

def create_table(c, conn):
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(country_name TEXT, url TEXT, from_ip TEXT, to_ip TEXT, total_ip TEXT, assign_date TEXT, owner TEXT)")#REAL


#def dynamic_data_entry(country_name,url,from_ip,to_ip,total_ip,assign_date,owner):
def dynamic_data_entry(list, c, conn):#הוא מקבל את הDictionarie וגם את המפתח של המדינה שלו
    b = True
    while b == True:
        if len(list) < 7:
            list.append("")
        else:
            b = False
    c.execute("INSERT INTO stuffToPlot (country_name ,url, from_ip, to_ip, total_ip, assign_date, owner) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (list[0],list[1],list[2],list[3],list[4],list[5],list[6]))
              # (country_name,url,from_ip,to_ip,total_ip,assign_date,owner))

    conn.commit()


def create_table_user(c, conn):
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(user_name TEXT, password REAL)")#REAL


def dynamic_data_entry_user(list, c, conn):
    c.execute("INSERT INTO stuffToPlot (user_name ,password) VALUES (?, ?)",
        (list[0], list[1]))
    conn.commit()

def check_password(user_name, password, c):
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(data)
    for row in data:
        if user_name==row[0] and password==row[1]:
            print 2
            return 2
        else:
            if user_name == row[0]:
                print 1
                return 1
            else:
                if password == row[1]:
                    print 0
                    return 0
                else:
                    print -1
                    return -1

def find_counry_by_name(country, c):
    c.execute('SELECT * FROM stuffToPlot WHERE country_name = ?', (country,))
    data = c.fetchall()
    for row in data:
        print row
    return data


    '''
    c.execute("SELECT * FROM stuffToPlot WHERE country_name = ?", country);
    data = c.fetchall()
    '''
