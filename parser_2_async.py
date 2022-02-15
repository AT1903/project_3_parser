
import asyncio
#Модуль asyncio предоставляет инструменты для создания асинхронных/параллельных приложений 
    # с использованием сопрограмм. 
    #
    # asyncio — новый модуль для организации конкурентного программирования, который появился 
    # в Python 3.4 (16 марта 2014 года). Он предназначен для упрощения использования корутин и футур 
    # в асинхронном коде — чтобы код выглядел как синхронный, без коллбэков.

from wsgiref import headers
    #wsgiref.headers – содержит класс для упрощения работы с заголовками ответа в виде объекта, 
    # похожего на словарь;

import aiohttp 
    #aiohttp – это библиотека Python для выполнения асинхронных HTTP запросов. 
    #Кроме того, он обеспечивает основу для объединения серверной части веб-приложения

import requests
    #Библиотека requests является стандартным инструментом для составления HTTP-запросов в Python.

from bs4 import BeautifulSoup
    #BeautifulSoup является библиотекой Python для парсинга HTML и XML документов. Часто используется 
    # для скрапинга веб-страниц.

import time
import datetime

start_time = time.time()#время начала выполнения скрипта
refs_homepage = [] #создаем список для хранения ссылок с главной страницы
refs_page2 = [] #создаем список для хранения ссылок со страницы 2-го уровня
result = dict() #словарь со сслыками

headers = {
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }  

print('--------------------------')
print('-----start parser---------')
print('--------------------------')

#Функция парсинга ссылок с главной страницы
def fun_parser_homepage():
    url = 'https://chastotnik.shop/'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  #lxml это быстрая и гибкая библиотека для обработки разметки XML и HTML на Python    
    refs = soup.find_all('a', class_= "show-more") #поиск все элементов с кнопок "смотреть все"
    for link in refs: refs_homepage.append(link.get('href')) #копируем в список все найденные ссылки
    #print (*refs_homepage, sep = "\n") # печать результатов

#Асинхронная функция парсинга ссылок со страницы 2-го уровня
async def fun_asy_parser_2page(session, url,num):
    async with session.get(url=url, headers=headers) as response:
        #refs_page2=[]
        response_text = await response.text() #await означает что при выполнение следующего за ней кода возможно переключение на другую сопрограмму
        soup = BeautifulSoup(response_text, 'lxml')  #lxml это быстрая и гибкая библиотека для обработки разметки XML и HTML на Python       
        refs1 = soup.find('div', class_= "card card-category").find('h1').text #поиск названия страницы 2 го уровня
        print (refs1) #вывод обнаруженного названия - для информации
        result[refs1]=dict() #создание ключа словаря 2 го уровня
        refs = soup.find('div', class_= "card card-subcategory").find_all('a') #поиск всех элементов типа "а" со страницы 2    
        for link in refs:        
            #refs_page2.append(link.get('href')) #копируем в список все найденный ссылки
            result[refs1][link.get('href')]=[]  
        print(f'обработал {num} из {len(refs_homepage)} результатов')
        #result[refs1] = refs_page2
        #print (*refs_page2, sep = "\n") # печать результатов

#создаем асинхронную функция для формирование списка задач (страницы 2го уровня)
async def fun_creater_tasks_2():  
    #Устанавливаем сессию ClientSession из aiohttp.
    async with aiohttp.ClientSession() as session:
        #создаем пустой список tasks        
        tasks = []
        c=1
        for page in refs_homepage:
            task = asyncio.create_task(fun_asy_parser_2page(session, page,c))
            tasks.append(task)
            c+=1
        await asyncio.gather(*tasks)

def main():
    print('main')
    curr_date = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    print (f'текущая дата {curr_date}')
    #парсинг ссылок с главной страницы
    fun_parser_homepage() 

    #запуск асинхронного парсинга   
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fun_creater_tasks_2())

    print (*refs_page2, sep = "\n") # печать результатов

    finish_time = time.time() - start_time #общее время выполнения скрипта
    print(f'Затраченное время: {finish_time}')
    print('************************************************')
    print('*****************FINISH*************************')
    print('************************************************')
    # for key, value in result.items():
    #     print(key)
    #     print(*value, sep = "\n")
    #print(result)

    for key, value in result.items():
        print(key)
        print(value)


if __name__ == '__main__': 
    #позволяет выполнять main только при выполнении данного модуля
    #если импортировать модуль - то программа не будет выполнена
    main()
    

    


#*****************INFO**********************
#
#Прочитать по асинхронному программированию:
#https://tonais.ru/library/asinhronnoe-programmirovanie-dlya-veb-razrabotki-v-python
#youtube.com/watch?v=87A1Rq0CGtE