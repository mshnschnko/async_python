import datetime
import time
import argparse
import sys
import os

def read_file(filename: str) -> None:
    with open(filename, mode='rb') as f:
        print(filename)
        while True:
            # time.sleep(0.001)
            data = f.read(1024)
            if not data:
                print(filename, "done ###############")
                break

def directory_traversal(path: str) -> None:
    file_list = list()
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default='files', help='the directory which files need to be read')
    dir = parser.parse_args(sys.argv[1:]).dir
    if not os.path.isdir(dir):
        raise FileNotFoundError(f"No such directory: {dir}")
    
    begin = datetime.datetime.now()

    files = directory_traversal(dir)
    for file in files:
        read_file(file)
    
    total_time = datetime.datetime.now() - begin
    with open('time.txt', 'a') as f:
        f.write('sync: ' + str(total_time) + '\n')

main()