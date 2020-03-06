from multiprocessing import Pool
import multiprocessing as multi
import time
import datetime
import logging

from Task import Task
from config import PRODUCT_LIST, MULTI_PROCESS_COUNT

formatter = '%(asctime)s: %(message)s'
filename = 'logs/main.log'
logging.basicConfig(level=logging.INFO, filename=filename, format=formatter)

def handle_task(process_count):
    logging.info('Process ' + str(process_count + 1) + ' started')
    task = Task(PRODUCT_LIST, process_count)
    task.run()
    logging.info('Process ' + str(process_count + 1) + ' finished')

def main():
    now = datetime.datetime.now()
    logging.info('Supreme Bot is running...')

    start = time.perf_counter()

    p = Pool(multi.cpu_count())
    p.map(handle_task, range(0, MULTI_PROCESS_COUNT))
    p.close()

    finish = time.perf_counter()
    logging.info(f'Supreme Bot finsiehd in {round(finish-start, 2)} second(s).')

if __name__ == "__main__":
    main()
