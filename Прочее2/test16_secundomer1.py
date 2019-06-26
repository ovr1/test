import time

def time_this(func_to_run):
    def func(*args, **kwargs):
        t0 = time.time()
        func_to_run(*args, **kwargs)
        t1 = time.time()
        print("Выполнение функции %s заняло %.5f секунд" % (func_to_run.__name__, t1 - t0))
    return func

@time_this
def dummy_cycle(N):
    for j in range(N):
        pass

dummy_cycle(1000000)


RUNS = 10

def time_this(func_to_run):
    def func(*args, **kwargs):
        avg = 0
        for _ in range(RUNS):
            t0 = time.time()
            func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= RUNS
        fn = func_to_run.__name__
        print("Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, RUNS, avg))
    return func

@time_this
def dummy_cycle(N):
    for j in range(N):
        pass

dummy_cycle(1000000)

import time

def time_this(RUNS=10):
    def decorator(func_to_run):
        def func(*args, **kwargs):
            avg = 0
            for _ in range(RUNS):
                t0 = time.time()
                func_to_run(*args, **kwargs)
                t1 = time.time()
                avg += (t1 - t0)
            avg /= RUNS
            fn = func_to_run.__name__
            print("Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, RUNS, avg))
        return func

    return decorator

@time_this(100)
def dummy_cycle(N):
    for j in range(N):
        pass

dummy_cycle(1000000)
