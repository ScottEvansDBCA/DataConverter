'''This program will download JSON from https://jsonplaceholder.typicode.com/postss
The results will then be saved into a .csv format.'''

import httplib2
import json
import csv
h = httplib2.Http('.cache')
response, content = h.request('https://jsonplaceholder.typicode.com/posts')
data = json.loads(content)
print (data[0])

print(data[0]["userId"])

for x in data:
    with open('users.csv', mode='a', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([x["userId"], x["id"], x["title"], x["body"]])

