# importing libraries
from bs4 import BeautifulSoup
import re
import csv
import requests
import pandas as pd
from datetime import date

url = "https://www.worldometers.info/coronavirus/#c-africa"

try:
    page = requests.get(url)
except:
    print("An error occured.")

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)
results = soup.find(id='main_table_countries_today')
content = results.find_all('td')

countries = []
total_cases = []
total_deaths = []
total_recovered = []
active_cases = []

i = 1
for data in content:
    if i%13 == 1:
        countries.append(data.text.strip())
    if i%13 == 2:
        total_cases.append(data.text.strip())
    if i%13 == 4:
        total_deaths.append(data.text.strip())
    if i%13 == 6:
        total_recovered.append(data.text.strip())
    if i%13 == 7:
        active_cases.append(data.text.strip())
    i += 1

column_names = [
    "Country", 
    "Total Cases", 
    "Total Deaths",  
    "Total Recovered", 
    "Active Cases"
]

covid19_table = {
    "country": countries,
    "total_cases": total_cases,
    "total_deaths": total_deaths,
    "total_recovered": total_recovered,
    "active_cases": active_cases
}

df = pd.DataFrame(covid19_table)
df.to_csv("daily.csv",index=False)

print (df)
