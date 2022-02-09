import requests
#from bs4 import BeautifulSoup as bs
import asyncio
#import aiohttp
#тест для гит


url = 'https://chastotnik.shop/preobrazovateli-chastoti'
url2 = 'https://chastotnik.shop/preobrazovateli-chastoti?page=2'
url_mod = 'https://chastotnik.shop/preobrazovatel-chastoti-erman-seriya-er-g-220-02-dlya-nasosov-model-er-g-220-02-10'
max_page = 689

async def wait_around(n, name): 
    for i in range(n): 
        print(f"{name}: iteration {i}") 
        await asyncio.sleep(0.5) 
    
async def wait_2(n, name): 
    for i in range(n): 
        print(f"{name}: iteration {i}") 
        #await asyncio.sleep(0.5)

async def main(): 
    await asyncio.gather(*[ wait_around(2, "coroutine 0"), wait_around(5, "coroutine 1"), wait_2(10000, 'prog2')])

loop = asyncio.get_event_loop() 
loop.run_until_complete(main())
