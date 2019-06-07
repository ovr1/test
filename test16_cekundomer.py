import time

t0 = time.time()
for j in range(1000000):
    pass
t1 = time.time()
print("Выполнение заняло %.5f секунд" % (t1 - t0))

avg = 0
for _ in range(10):
    t0 = time.time()
    for j in range(1000000):
        pass
    t1 = time.time()
    avg += (t1 - t0)
avg /= 10
print("Выполнение заняло %.5f секунд" % avg)