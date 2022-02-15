


import asyncio
from wsgiref import headers
import aiohttp 
import requests   
from bs4 import BeautifulSoup
import time
import datetime

start_time = time.time()#время начала выполнения скрипта
refs_homepage = [] #создаем список для хранения ссылок с главной страницы
refs_page2 = [] #создаем список для хранения ссылок со страницы 2-го уровня

res = dict() #словарь со сслыками
headers = {
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }  

print('--------------------------')
print('-----start parser---------')
print('--------------------------')

#Функция парсинга ссылок с главной страницы
def fun_parser_homepage(url):    
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  #lxml это быстрая и гибкая библиотека для обработки разметки XML и HTML на Python    
    refs = soup.find_all('h3') #поиск все элементов 
    #print(refs)
    for link in refs:
        print(link.find('a').get('href'))
        #refs_homepage.append(link.find('h3').get('href')) #копируем в список все найденные ссылки
    print(refs_homepage)
    # refs = soup.find_all('div', class_= "caption").get_text() #find('h1')#

    # print(refs)
    # p1 = refs.find('всего')
    # p2 = refs.find('стр')
    # pages = int(refs[p1+6:p2-1])
    # print(pages)
    #print(refs[p1+6:p2-1])
    

def main():
    print('main')
    curr_date = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    print (f'текущая дата {curr_date}')

    #url = 'https://chastotnik.shop/index.php?route=product/category&path=1351_1403_1404'
    url = 'https://chastotnik.shop/ustrojstva-plavnogo-puska-abb-seriya-pse'
    fun_parser_homepage(url)
    

    print (*refs_page2, sep = "\n") # печать результатов

    finish_time = time.time() - start_time #общее время выполнения скрипта
    print(f'Затраченное время: {finish_time}')
    print('************************************************')
    print('************************************************')
    

if __name__ == '__main__': 
    #позволяет выполнять main только при выполнении данного модуля
    #если импортировать модуль - то программа не будет выполнена
    main()
    
