import timeit

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp

unsorted = [52, 27, 91, 18, 71, 33, 55, 44, 109]
bubble_sort(unsorted)
print(unsorted)

def regular_sort(a):
    return sorted(a)

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

unsorted = [52, 27, 91, 18, 71, 33, 55, 44, 109]
#import random
#unsorted = [random.randint(1, 100) for _ in range(10000)]

runs = 100

bubble_times = timeit.Timer(lambda: bubble_sort(unsorted)).repeat(number=1, repeat=runs)
avg_bubble = sum(bubble_times) / runs
print("Среднее время для пузырьковой сортировки: %g" % avg_bubble)

regsort_times = timeit.Timer(lambda: regular_sort(unsorted)).repeat(number=1, repeat=runs)
avg_regsort = sum(regsort_times) / runs
print("Среднее время для стандартной сортировки: %g" % avg_regsort)

print("Стандартная сортировка быстрее нашей пузырьковой в %.3f раз" % (avg_bubble/avg_regsort))

