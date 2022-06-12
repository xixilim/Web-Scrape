# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:02:01 2017

Author: Chenlin Cheng (ccheng04)
File: Homework 2
"""

import requests
from bs4 import BeautifulSoup as bsoup
    
my_wm_username = 'ccheng04'
search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content
            

"""parse html"""
parsed_html = bsoup(response, 'lxml')

"""get target rows"""
table = parsed_html.find('tbody') #find the table by using tbody
table_rows = table.find_all('tr') #access to each row of the table

#create a new list to store text in the table
my_result_list = []

#iterate through each row and find target elements (header included)
for i in table_rows:
    element = i.find_all('td')
    #find text in each line and save it to empty list
    element = [x.text.strip() for x in element]
    my_result_list.append(element)

"""print results into lists"""
print (my_wm_username)
print(len(my_result_list))
print(my_result_list)
