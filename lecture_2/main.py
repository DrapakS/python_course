import time

t_start = time.time()
a = 0
for i in range(100000000):
    a += i
t_end = time.time()
print("Execution time, seconds: ", t_end - t_start)
