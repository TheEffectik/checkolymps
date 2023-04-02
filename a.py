import requests
from time import sleep
import time 
import difflib
import os
import filecmp

requests.Response.encoding = 'utf-8'

url = []
names = []

with open('links.txt', 'r', encoding="utf-8") as mn:
    for i in mn.readlines():
        print(i)
        lnk, name = map(str, i.split())
        url.append(lnk)
        names.append(name)
    

n = len(names)

# <- чекпоинт 

# for i in range(n):
#     response = requests.get(url[i])
#     response.encoding = response.apparent_encoding
#     with open(f'data/{names[i]}.txt', 'w+', encoding="utf-8") as fl:
#         fl.write(response.text)
# exit(0)


for i in range(n):
    response = requests.get(url[i])
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        print(names[i], end=' ')
        with open(f'data/{names[i]}2.txt', 'w+', encoding="utf-8") as fl:
            fl.write(response.text)

        if (filecmp.cmp(f'data/{names[i]}.txt', f'data/{names[i]}2.txt')):
            print("-")
        else: print("+")
    else:
        print('Error:', response.status_code)