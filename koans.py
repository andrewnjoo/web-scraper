from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get(
    'https://ashidakim.com/zenkoans/').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
links = soup.find_all('a')
# print(links)
# counter = 0
with open("output.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for link in links:
        href = link['href']
        if(href.startswith('http://www.ashidakim.com/zenkoans/')):
            # counter += 1
            writer.writerow([href])
            print(href)

# print(counter)
