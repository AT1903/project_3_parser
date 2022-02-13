
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


print('--------------------------')
print('-----start parser---------')
print('--------------------------')

#Функция парсинга ссылок с главной страницы
def fun_parser_homepage():
    headers = {
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
    url = 'https://chastotnik.shop/'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  #lxml это быстрая и гибкая библиотека для обработки разметки XML и HTML на Python    
    refs_homepage = set()                        #создаем пустое множество для хранения ссылок с главной страницы
    refs = soup.find_all('a', class_= "show-more") #поиск все элементов с кнопок "смотреть все"
    for link in refs: refs_homepage.add(link.get('href')) #копируем в множество всей найденный ссылки
    print (*refs_homepage, sep = "\n") # печать результатов
    


#создаем асинхронную функция для парсинга  
async def fun_parser():
    headers = {
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
    url = 'https://chastotnik.shop/preobrazovateli-chastoti?page='    

#создаем асинхронную функция для формирование списка задач  
async def fun_creater_tasks():  
    #Устанавливаем сессию ClientSession из aiohttp.
    async with aiohttp.ClientSession() as sesion:
        #создаем пустой список tasks
        tasks = []

        url = 'https://chastotnik.shop/preobrazovateli-chastoti'
        headers = {
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)   

def main():
    print('main')
    curr_date = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    print (f'текущая дата {curr_date}')

    fun_parser_homepage()

    finish_time = time.time() - start_time #общее время выполнения скрипта
    print(f'Затраченное время: {finish_time}')



if __name__ == '__main__': 
    #позволяет выполнять main только при выполнении данного модуля
    #если импортировать модуль - то программа не будет выполнена
    main()
    

    


#*****************INFO**********************
#
#Прочитать по асинхронному программированию:
#https://tonais.ru/library/asinhronnoe-programmirovanie-dlya-veb-razrabotki-v-python
#youtube.com/watch?v=87A1Rq0CGtE