#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bs4 as bs
import urllib
import sqlite3
import sql_database_fun as sf


def find_country(c, conn):#הפעולה מביאה את המדינות והקישורים אליהם

    html2 = urllib.urlopen('http://www.nirsoft.net/countryip/').read()
    soup2 = bs.BeautifulSoup(html2, 'lxml')
    #אני מזהה את הTABLE בעזרת ATTRIBUTE מסויים שיש לה
    table2 = soup2.find(lambda tag: tag.name == 'table' and tag.has_attr('width') and tag['width'] == "650")
    rows2 = table2.findAll(lambda tag: tag.name == 'tr')
    #print rows2
    for row2 in rows2:
        td2 = row2.find_all('a')
        bar2 = [i.text for i in td2]
        end_url2 = [i.get('href') for i in td2]
        for b in range(3):

            print_country_page_infromation(end_url2[b], bar2[b], c, conn)

    '''
    table = soup.find('table')
    #table_rows = table.find_all('tr')
    table_rows2 = table.find_all('td')
    condition = False
    print table_rows2

    for tr in table_rows2:
        td = tr.find_all('a')
        row = [i.text for i in td]
        print row
        
        if len(row) != 0:
            if row[0] == 'Afghanistan':
                condition = True
        if (condition == True):
            #print(row) 
            end_url = [i.get('href') for i in td]
            #print end_url
            print_country_page_infromation(end_url, row, list_country, c, conn)
    '''
def print_country_page_infromation(end_url, country_name, c, conn):#הפעולה מביאה את כל המידע שיש עלאה
    print country_name

    html = urllib.urlopen('http://www.nirsoft.net/countryip/' + end_url).read()
    soup = bs.BeautifulSoup(html, 'lxml')
    #אני מזהה את הTABLE בעזרת ATTRIBUTE מסויים שיש לה
    table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('border') and tag['border'] == "1")
    rows = table.findAll(lambda tag: tag.name == 'tr')
    rows.pop(0)
    for row in rows:

        td = row.find_all('td')
        bar = [i.text for i in td]
        '''
        count=True
        if len(bar[-1].split()) == 0:
            print 'printed bar here'

            for ip in bar:
                if '.' in ip and count == True:
                    check_ip_owner(ip)
                    count = False
        '''
        bar.insert(0, 'http://www.nirsoft.net/countryip/' + end_url)
        bar.insert(0, country_name)
        #print bar
        sf.dynamic_data_entry(bar, c, conn)




######
'''
def check_ip_owner(ip_owner):
    sring_owner= 'https://www.whois.com/whois/' + ip_owner
    print 'we will find you'
    html3 = urllib.urlopen(sring_owner).read()
    soup3 = bs.BeautifulSoup(html3, 'lxml')
    # אני מזהה את הTABLE בעזרת ATTRIBUTE מסויים שיש לה
    table3 = soup3.find(lambda tag: tag.name == 'pre' and tag.has_attr('id') and tag['id'] == "registryData")
    print len(table3)
    
    for s in table3:
        s = s + "$"
        if 'descr:' in s:
            if s[]
            print 1
            print s
    
    rows3 = table3.findAll(lambda tag: tag.name == 'descr')
    print rows3

'''


def create_database():
    c, conn = sf.create_sql_connection('country_database.db')
    sf.create_table(c, conn)
    find_country(c, conn)
    #maybe need to close connection close_sql_connection







