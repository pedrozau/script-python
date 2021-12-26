import asyncio 

async def main():
    print('time')
    await foo('Hello,Guys!!')

async def foo(text):
    print(text)
    await asyncio.sleep(10)

asyncio.run(main())