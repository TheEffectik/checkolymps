import requests
from time import sleep
import time 
import difflib
import os
import filecmp
import pathlib
from pathlib import Path


requests.Response.encoding = 'utf-8'

directory = "." 

url = []
names = []

delay = 60

with open(f'{str(directory)}\links.txt', 'r', encoding="utf-8") as mn:
    for i in mn.readlines():
        lnk, name = map(str, i.split())
        url.append(lnk)
        names.append(name)
    

n = len(names)

# <- чекпоинт 

for i in range(n):
    response = requests.get(url[i])
    response.encoding = response.apparent_encoding
    with open(f'{directory}/data/{names[i]}.txt', 'w+', encoding="utf-8") as fl:
        fl.write(response.text)
sleep(delay)