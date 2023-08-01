import aiofiles
import asyncio
import datetime
import time


async def read_file(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        print(filename)
        while True:
            # await asyncio.sleep(0.001)
            data = await f.read(1024)
            if not data:
                print(filename, "done ###############")
                break

async def main():
    begin = datetime.datetime.now()
    files = ['files/{}'.format(i) for i in range(1, 11)]
    
    for f in asyncio.as_completed([read_file(file) for file in files]):
        await f

    total_time = datetime.datetime.now() - begin
    with open('time.txt', 'a') as f:
        f.write('async: ' + str(total_time) + '\n')

asyncio.run(main())
