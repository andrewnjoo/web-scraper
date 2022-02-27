from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://weworkremotely.com/categories/remote-front-end-programming-jobs').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='feature')
for job in jobs:
    company = job.find('span', class_='company')
    title = job.find('span', class_='title')
    location = job.find('span', class_='region company')
    if 'North America' in location.text or 'USA' in location.text:
        print(company.text, title.text)
