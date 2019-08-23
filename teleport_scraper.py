# Import necessary libraries
import requests
import re
import urllib.parse as up
import json
import pandas as pd
import numpy as np
from pprint import pprint


df = pd.read_excel('university_1.xlsx')

# For loop to get name of city and country from static api
full_name = []
for i in df['first_administrative_area_level']:
    convert = up.quote(i)
    url = url = 'https://api.teleport.org/api/cities/?search=' + convert
    embed = 'city:search-results/city:item/city:urban_area/ua:scores'
    params = {'embed': embed}
    page = requests.get(url, params=params)
    content = json.loads(page.text)
    result = content['_embedded']['city:search-results']
    if len(result) == 0:
        full_name.append(np.nan)
    else:
        for i in result[:1]:
            full_name.append(i['matching_full_name'])

df['full_name'] = full_name

# Initialize empty lists to contain details of api calls
housing = []
cost_of_living = []
startups = []
venture_capital = []
travel_connectivity = []
commute = []
business_freedom = []
safety = []
healthcare = []
education = []
environment_quality = []
economy = []
taxation = []
internet_access = []
leisure_culture = []
tolerance = []
outdoors = []

# Breakdown of each of the results added to initialized list
for i in df['first_administrative_area_level']:
    convert = up.quote(i)
    url = url = 'https://api.teleport.org/api/cities/?search=' + convert
    embed = 'city:search-results/city:item/city:urban_area/ua:scores'
    params = {'embed': embed}
    page = requests.get(url, params=params)
    content = json.loads(page.text)
    result = content['_embedded']['city:search-results']
    if len(result) != 0:
        for i in result[:1]:
            check = i['_embedded']['city:item']['_embedded']['city:urban_area']
            search_tree = check['_embedded']['ua:scores']['categories']
            if '_embedded' in check:
                housing.append(search_tree[0]['score_out_of_10'])
                cost_of_living.append(search_tree[1]['score_out_of_10'])
                startups.append(search_tree[2]['score_out_of_10'])
                venture_capital.append(search_tree[3]['score_out_of_10'])
                travel_connectivity.append(search_tree[4]['score_out_of_10'])
                commute.append(search_tree[5]['score_out_of_10'])
                business_freedom.append(search_tree[6]['score_out_of_10'])
                safety.append(search_tree[7]['score_out_of_10'])
                healthcare.append(search_tree[8]['score_out_of_10'])
                education.append(search_tree[9]['score_out_of_10'])
                # environment_quality(search_tree[10]['score_out_of_10'])
                economy.append(search_tree[11]['score_out_of_10'])
                taxation.append(search_tree[12]['score_out_of_10'])
                internet_access.append(search_tree[13]['score_out_of_10'])
                leisure_culture.append(search_tree[14]['score_out_of_10'])
                tolerance.append(search_tree[15]['score_out_of_10'])
                outdoors.append(search_tree[16]['score_out_of_10'])
            else:
                housing.append(np.nan)
                cost_of_living.append(np.nan)
                startups.append(np.nan)
                venture_capital.append(np.nan)
                travel_connectivity.append(np.nan)
                commute.append(np.nan)
                business_freedom.append(np.nan)
                safety.append(np.nan)
                healthcare.append(np.nan)
                education.append(np.nan)
                # environment_quality.append(np.nan)
                economy.append(np.nan)
                taxation.append(np.nan)
                internet_access.append(np.nan)
                leisure_culture.append(np.nan)
                tolerance.append(np.nan)
                outdoors.append(np.nan)
    else:
        housing.append(np.nan)
        cost_of_living.append(np.nan)
        startups.append(np.nan)
        venture_capital.append(np.nan)
        travel_connectivity.append(np.nan)
        commute.append(np.nan)
        business_freedom.append(np.nan)
        safety.append(np.nan)
        healthcare.append(np.nan)
        education.append(np.nan)
        # environment_quality.append(np.nan)
        economy.append(np.nan)
        taxation.append(np.nan)
        internet_access.append(np.nan)
        leisure_culture.append(np.nan)
        tolerance.append(np.nan)
        outdoors.append(np.nan)

df['Housing'] = housing
df['Cost_of_Living'] = cost_of_living
df['Startups'] = startups
df['Travel_Connectivity'] = travel_connectivity
df['Commute'] = commute
df['Business_Freedom'] = business_freedom
df['Safety'] = safety
df['Healthcare'] = healthcare
df['Education'] = education
df['Economy'] = economy
df['Taxation'] = taxation
df['Internet_Access'] = internet_access
df['Leisure_Culture'] = leisure_culture
df['Tolerance'] = tolerance
df['Outdoors'] = outdoors

df.to_excel('university_1.xlsx')
