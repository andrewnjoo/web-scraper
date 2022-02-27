import csv
import re

# human sorting / natural sorting helper function


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


arr = []
with open('output.csv', newline='') as csvfile:
    writer = csv.reader(csvfile, delimiter=' ')
    for row in writer:
        arr.append(row[0])

# print(arr)
print(len(arr))

arr.sort(key=natural_keys)
# print(arr)

with open("output-ordered.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for link in arr:
        writer.writerow([link])
