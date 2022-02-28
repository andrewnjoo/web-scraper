from bs4 import BeautifulSoup
import requests
import csv
import re

html_text = requests.get(
    'https://ashidakim.com/zenkoans/').text
soup = BeautifulSoup(html_text, 'lxml')
links = list(filter(lambda x: x['href'].startswith(
    'http://www.ashidakim.com/zenkoans/'), soup.find_all('a')))

for i, link in enumerate(links):
    links[i] = link['href']

# # human sorting helper function


def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    float regex comes from https://stackoverflow.com/a/12643073/190597
    '''
    return [atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text)]


links.sort(key=natural_keys)
print(links)

with open("output.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for link in links:
        writer.writerow([link])
