from multiprocessing import Pool
import multiprocessing as multi
import time
import datetime

from Task import Task
from config import PRODUCT_LIST, MULTI_PROCESS_COUNT

def handle_task(process_count):
    print("Process " + str(process_count + 1) + " started")
    task = Task(PRODUCT_LIST, process_count)
    task.run()
    print("Process " + str(process_count + 1) + " finished")

def main():
    now = datetime.datetime.now()
    print("Supreme Bot started at " + str(now.strftime("%Y-%m-%d %H:%M:%S")))

    start = time.perf_counter()

    p = Pool(multi.cpu_count())
    p.map(handle_task, range(0, MULTI_PROCESS_COUNT))
    p.close()

    finish = time.perf_counter()
    print(f'Job finsiehd in {round(finish-start, 2)} second(s).')

if __name__ == "__main__":
    main()
