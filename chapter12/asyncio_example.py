import asyncio


async def compute1():
    for i in range(5):
        print(f"compute1 : {i}")
        await asyncio.sleep(.1)

        
async def compute2():
    for i in range(5):
        print(f"compute2 : {i}")
        await asyncio.sleep(.2)
        
        
async def main():
    await asyncio.gather(compute1(), compute2())
    

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
