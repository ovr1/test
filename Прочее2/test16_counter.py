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
