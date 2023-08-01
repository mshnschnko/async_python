import datetime
import time

def read_file(filename):
    with open(filename, mode='rb') as f:
        print(filename)
        while True:
            # time.sleep(0.001)
            data = f.read(1024)
            if not data:
                print(filename, "done ###############")
                break


def main():
    begin = datetime.datetime.now()
    files = ['files/{}'.format(i) for i in range(1, 11)]
    for f in files:
        read_file(f)
    total_time = datetime.datetime.now() - begin
    with open('time.txt', 'a') as f:
        f.write('sync: ' + str(total_time) + '\n')

main()