import requests
from time import sleep
import time 
import difflib
import os
import filecmp
# n = int(input("Количество сайтов"))

# print("Введите сайт - название")
requests.Response.encoding = 'utf-8'
url = ['https://neerc.ifmo.ru/school/ioip/index.html',
       'https://cups.online/ru/rounds/767/leaderboard',
       'https://olymp.msu.ru/rus/event/7710/page/3118',
       'https://olymp.mephi.ru/rosatom/winners']

names = ['ИОИП', 'ТК', 'ЛОМ', 'росатом']
f = [0].copy() * len(names)
n = len(names) - 1
delay = 20 * 60 # check once a day
# <- чекпоинт 
# n = len(names)
# for i in range(n):
#     response = requests.get(url[i])
#     response.encoding = response.apparent_encoding
#     with open(f'data/{names[i]}.txt', 'w+', encoding="utf-8") as fl:
#         fl.write(response.text)
# exit(0)


for i in range(n):
    if f[i] == 1: 
        print(f'{names[i]} +++++')
        continue

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