# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("Coffee: prepare ingridients")
    sleep(1)
    print("coffee : waiting...")
    await asyncio.sleep(5)
    print("coffee: ready")
    
async def fry_eggs():
    print("eggs: prepare ingridients")
    sleep(1)
    print("egg: frying....")
    await asyncio.sleep(3)
    print ("eggs: ready")
    
async def main():
    start = time()
    coffee_task = asyncio.create_task(make_coffee())
    eggs_task = asyncio.create_task(fry_eggs())
    
    await coffee_task
    await eggs_task
    print(f"breakfast is ready in {time()-start}min")

asyncio.run(main())