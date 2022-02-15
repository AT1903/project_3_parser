


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
def fun_parser_homepage():
    url='https://chastotnik.shop/index.php?route=product/category&path=1351_1508'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  #lxml это быстрая и гибкая библиотека для обработки разметки XML и HTML на Python    
    refs = soup.find('div', class_= "card card-category").find('h1')#    
    print(refs.text)
    # for link in refs: refs_homepage.append(link.get('href')) #копируем в список все найденные ссылки
    # print (*refs_homepage, sep = "\n") # печать результатов

def main():
    print('main')
    curr_date = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    print (f'текущая дата {curr_date}')

    fun_parser_homepage()
    
    # for r in refs_homepage:
    #     fun_parser_2page(r)#refs_homepage[0])
    # print (*refs_page2, sep = "\n") # печать результатов

    print (*refs_page2, sep = "\n") # печать результатов

    finish_time = time.time() - start_time #общее время выполнения скрипта
    print(f'Затраченное время: {finish_time}')
    print('************************************************')
    print('************************************************')
    print('************************************************')


if __name__ == '__main__': 
    #позволяет выполнять main только при выполнении данного модуля
    #если импортировать модуль - то программа не будет выполнена
    main()
    
