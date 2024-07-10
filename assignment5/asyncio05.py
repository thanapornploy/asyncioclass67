import asyncio
from random import random

# Coroutine สำหรับทำข้าวผัด
async def cook_rice():
    Value = 1 + random()
    print(f"Cooking rice {Value} sec")
    await asyncio.sleep(Value)
    return f'rice is {Value}'

# Coroutine สำหรับทำก๋วยเตี๋ยว
async def cook_noodle():
    Value = 1 + random()
    print(f"Cooking noodle {Value} sec")
    await asyncio.sleep(Value)
    return f'noodle is {Value}'

# Coroutine สำหรับทำข้าวแกง
async def cook_curry():
    Value = 1 + random()
    print(f"Cooking Curry {Value} sec")
    await asyncio.sleep(Value)
    return f'curry is {Value}'

async def main():
    # สร้าง tasks สำหรับแต่ละ coroutine
    tasks = [
        asyncio.create_task(cook_rice(), name="rice"),
        asyncio.create_task(cook_noodle(), name="noodle"),
        asyncio.create_task(cook_curry(), name="curry")
    ]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first = done.pop()
    print(first.result())
    print(f'{len(done)} task uncomplete')
# เริ่มโปรแกรม asyncio
asyncio.run(main())
