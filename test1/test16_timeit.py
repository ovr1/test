import timeit

def dummy_cycle():
    for j in range(1000000):
        pass

def another_cycle():
    for j in range(1000000):
        j**2

print(timeit.Timer(dummy_cycle).timeit(number=10))
print(timeit.Timer(another_cycle).timeit(number=10))

def cube_cycle():
    for j in range(1000000):
        j**3

print(timeit.Timer(cube_cycle).repeat(number=10, repeat=3))
print(timeit.Timer(cube_cycle).repeat(number=1, repeat=5))