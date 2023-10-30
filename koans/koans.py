from bs4 import BeautifulSoup
import requests
import csv
import sys
from helpers import atof, natural_keys

# Get data from webpage

html_text = requests.get(
    'https://ashidakim.com/zenkoans/').text
soup = BeautifulSoup(html_text, 'lxml')
links = list(filter(lambda x: x['href'].startswith(
    'https://ashidakim.com/zenkoans/'), soup.find_all('a')))

# print(soup)

for i, link in enumerate(links):
    links[i] = link['href']

links.sort(key=natural_keys)
# print(links)

# Write to links.csv

# with open("links.csv", "w", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for link in links:
#         writer.writerow([link])


def addRow(num):
    temp = []
    html_text_1 = requests.get(links[num]).text
    soup = BeautifulSoup(html_text_1, 'lxml')
    para = soup.find_all("font")
    for p in para[1:-1]:
        x = p.text.replace('\n\n', ' ').replace(
            '\n', ' ').replace('\xa0', '').replace("\\'", "")
        temp.append(x)

    with open("text.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in temp:
            writer.writerow([row])


for idx, row in enumerate(links):
    addRow(idx)
