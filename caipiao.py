# coding:utf-8

import requests

from bs4 import BeautifulSoup
import time


def formatIndex(index):
    h = str(index)
    h0 = len(h)
    if h0 == 3:
        return h

    if h0 < 3:
        h0 = 3 - h0

    for a in range(h0):
        h = "0" + h
    return h


data = []
year = '17'
index = 1
while (True):
    num = year + formatIndex(index)
    print(num)
    response = requests.get("http://kaijiang.500.com/shtml/qxc/" + num + ".shtml")
    if response.status_code == 404:
        break
    aaa = ''
    doc = response.text
    soup = BeautifulSoup(doc)
    for div in soup.find_all('li', class_='ball_orange'):
        aaa = aaa + ',' + div.text
    index = index + 1
    data.append(num + aaa + '\n')
    # time.sleep(1)

file_object = open('data/qxc.txt', 'w')
file_object.writelines(data)
file_object.close()
