from bs4 import BeautifulSoup
import requests
html_text = requests.get(
    'https://ashidakim.com/zenkoans/').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
links = soup.find_all('a')
# print(links)
counter = 0
for link in links:
    href = link['href']
    if(href.startswith('http://www.ashidakim.com/zenkoans/')):
        counter += 1
        print(href)

print(counter)
