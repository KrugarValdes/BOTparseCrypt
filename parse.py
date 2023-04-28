from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку
import time
import re
import statistics
def currency():
    url = 'https://coinmarketcap.com'
    page = requests.get(url)
    # print('Cтатуc страницы',page.status_code)

    soup = BeautifulSoup(page.text, 'lxml')
    block = soup.findAll('tr')
    cur = ""
    for data in block:
        if data.find('p', class_="sc-4984dd93-0 iqdbQL coin-item-symbol"):
            cur += 'валюта - ' + data.find('p', class_="sc-4984dd93-0 iqdbQL coin-item-symbol").text + '\n'+ 'цена - ' + data.find('div',class_="sc-cadad039-0 clgqXO").text + '\n'
    return cur
def limitcheck(crypta):
    url = 'https://coinmarketcap.com'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')
    block = soup.findAll('tr')
    value = 0
    for data in block:
        if data.find('p', class_="sc-4984dd93-0 iqdbQL coin-item-symbol"):
            t = data.find('p', class_="sc-4984dd93-0 iqdbQL coin-item-symbol").text
            if ( t == crypta) :
                result = data.find('div',class_="sc-cadad039-0 clgqXO").text
                value = float((result.replace('$','')).replace(',',''))
    return value

