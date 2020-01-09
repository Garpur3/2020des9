import time
import datetime

t0 = time.time()
total_sum = 0
total_mul = 1
limit = 10000
for i in range(1,limit):
    total_sum += i
    total_mul *= i
print(f'For the first {limit} number\nTotal sum: {total_sum}\nTotal multiple: {total_mul}')
t1 = time.time()
limit = 100000
for i in range(1,limit):
    total_sum += i
    total_mul *= i
print(f'For the first {limit} number\nTotal sum: {total_sum}\nTotal multiple: {total_mul}')
t2 = time.time()
print(f'Time required: {t1-t0} seconds\nDatetime format: {datetime.datetime.fromtimestamp(int(t1)) - datetime.datetime.fromtimestamp(int(t0))}')            # \nDatetime time: {datetime.datetime.fromtimestamp(int(t1)) - datetime.datetime.fromtimestamp(int(t0))}
print(f'Time required for later run: {t2-t1} seconds\nDatetime format: {datetime.datetime.fromtimestamp(int(t2)) - datetime.datetime.fromtimestamp(int(t1))}')
print(f'Total time: {t2-t0} seconds\nDatetime format: {datetime.datetime.fromtimestamp(int(t2)) - datetime.datetime.fromtimestamp(int(t0))}')