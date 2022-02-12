#Прочитать по асинхронному программированию:
#https://tonais.ru/library/asinhronnoe-programmirovanie-dlya-veb-razrabotki-v-python

#youtube.com/watch?v=87A1Rq0CGtE
import asyncio
import aiohttp
print('-------------------------')
print('-----start parser---------')
print('-------------------------')

async def fun_parser():
    #парсер сайта
    pass

async def fun_creater_tasks():
    #формирование списка задач    
    async with aiohttp.ClientSession() as sesion:
        pass
    pass

def main():
    print('main')

if __name__ == '__main__':
    main()