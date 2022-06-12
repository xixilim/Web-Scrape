# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:06:43 2017

Author: Chenlin Cheng (ccheng04)
File: CTBA_Homework 3
"""

import requests

my_wm_username = 'ccheng04'
search_url = 'https://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
 
#access root in json file
root = response.json()

"""Number of shots categorized exactly as “Jump Shot”"""
numJumpShotsAttempt = 0 #initialize number as 0
for i in response.json(): #iterate through each target 'row' and check if the information is included
    if i['ACTION_TYPE'] == 'Jump Shot':
        numJumpShotsAttempt += 1

"""The number of those shots classified as a “Made Shot”"""
numJumpShotsMade = 0 #initialize number as 0
for j in response.json():
    if j['ACTION_TYPE'] == 'Jump Shot' and j['EVENT_TYPE'] == 'Made Shot':
        numJumpShotsMade += 1

"""The percentage of the attempted “Jump Shots” which were classified as “Made Shot” """
#find the percentage by calculation
percJumpShotMade = numJumpShotsMade / numJumpShotsAttempt
#change numbers to percentage format.
percJumpShotMade = "{:.3%}".format(percJumpShotMade)

print(my_wm_username)
print(numJumpShotsAttempt)
print(numJumpShotsMade)
print(percJumpShotMade)