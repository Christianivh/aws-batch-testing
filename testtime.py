
import time
import sys

sleep_time = 200

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sleep_time = int(sys.argv[1])

    print('Start: ', time.strftime("%I:%M:%S %p", time.localtime()))
    time.sleep(sleep_time)
    print('Finish: ', time.strftime("%I:%M:%S %p", time.localtime()))
    print('Sleep Time: ', sleep_time)
