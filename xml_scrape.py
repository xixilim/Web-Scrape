# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:28:32 2021

Author: Chenlin Cheng (ccheng04)
File: CTBA_Homework 1
"""

import requests
from lxml import objectify

wm_user = 'ccheng04'
print(wm_user)

"""NOAA National Centers for Environmental information, Climate at a Glance"""
"""Create a string variable for each of the parameters above to store string values in the
form that the URL requires them."""

parameter = 'tavg'
state = '44'
month = '08'
year = '2016'
#Create a urlTemplate to insert custom elements
urlTemplate = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/%s-%s-%s%s/data.xml'
url = urlTemplate % (state, parameter, year, month)

response = requests.get(url).content
#access root of xml file
root = objectify.fromstring(response)

"""Retrieve the XML data with your program (or view it initially in a browser) and
notice how you can identify the portion of the XML file that is associated with a 5-
month window, April-August 2016 """
#use for loop to find the target <data>
for i in range(len(root['data'])):
    #define the target <data>, and extract information we want
   if int(root['data'][i]['period']) == 5:
      print(root['data'][i]['value'])
      print(root['data'][i]['mean'])
      print(root['data'][i]['departure'])
      print(root['data'][i]['lowRank'])
      print(root['data'][i]['highRank'])
        
