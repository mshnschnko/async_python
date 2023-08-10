import aiofiles
import asyncio
import datetime
import time
import argparse
import sys
import os


async def read_file(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        print(filename)
        while True:
            # await asyncio.sleep(0.001)
            data = await f.read(1024)
            if not data:
                print(filename, "done ###############")
                break

def directory_traversal(path: str) -> None:
    file_list = list()
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default='files', help='the directory which files need to be read')
    dir = parser.parse_args(sys.argv[1:]).dir
    if not os.path.isdir(dir):
        raise FileNotFoundError("No such directory")
    
    begin = datetime.datetime.now()

    for f in asyncio.as_completed([read_file(file) for file in directory_traversal(dir)]):
        await f
    
    total_time = datetime.datetime.now() - begin
    with open('time.txt', 'a') as f:
        f.write('async: ' + str(total_time) + '\n')

asyncio.run(main())
