


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
list1 = []
headers = {
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }

dict1 = {'Устройства плавного пуска': 
            {'https://chastotnik.shop/ustrojstva-plavnogo-puska-abb': {'Устройства плавного пуска ABB': 
            {'https://chastotnik.shop/ustrojstva-plavnogo-puska-abb-seriya-pse': {'Устройства плавного пуска ABB серия PSE': 
            {'https://chastotnik.shop/ustrojstva-plavnogo-puska-abb-seriya-pse-model-pse105-600-70': [] }}}}}}

print('--------------------------')
print('-----start parser---------')
print('--------------------------')

def print_d(d, indent=0):
    s = "...."
    for key, value in d.items():
        print(s * indent + str(key))
        if isinstance(value, dict): # вернет True, если проверяемый объект object является экземпляром словаря
            print_d(value, indent+1)
        else:
            print(s * (indent+1) + str(value))

#функция удаления переноса строки
def del_n(str):
    sy = '\n'
    str = str.replace( 2*sy, sy)
    if 2*sy in str:
        return del_n(str)
    else:
        return str

#заполнение словаря
def d_find(d, l):    
    for key, value in d.items():        
        if isinstance(value, dict): # вернет True, если проверяемый объект object является экземпляром словаря
            d_find(value,l)
        else:
            d[key]=l

#Функция парсинга ссылок с главной страницы
def fun_parser_homepage(url):
    out = []    
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  #lxml это быстрая и гибкая библиотека для обработки разметки XML и HTML на Python

    refs = soup.find('div', class_= "product-info").find('h1').text #поиск названия    
    out.append(refs)

    refs = soup.find('div', class_= "tab-pane active").text #поиск описания    
    out.append(del_n(refs.lstrip()).replace('\n ', '\n'))

    refs = soup.find_all('div', class_ = 'attr-td')         #поиск характеристик
    for l in (refs):        
        out.append(l.text)
    return out


    # for l in range(0,len(refs),2):
    #     #print(f'{refs[l].text} : {refs[l+1].text}')
    #     out.append(f'{refs[l].text} : {refs[l+1].text}')
    # return out


    

def main():
    print('main')
    curr_date = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    #print (f'текущая дата {curr_date}')
    url = 'https://chastotnik.shop/ustrojstva-plavnogo-puska-abb-seriya-pse-model-pse105-600-70'
    list1=(fun_parser_homepage(url))
    d_find(dict1,list1)
    print(dict1)
    print_d(dict1)
    #print(*list1, sep = "\n")

    

    #print (*refs_page2, sep = "\n") # печать результатов

    finish_time = time.time() - start_time #общее время выполнения скрипта
    print(f'Затраченное время: {finish_time}')
    print('************************************************')
    print('************************************************')
    

if __name__ == '__main__': 
    #позволяет выполнять main только при выполнении данного модуля
    #если импортировать модуль - то программа не будет выполнена
    main()
    
