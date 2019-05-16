a = [1, 2, 4, 7]
b = ["task", "example", "django", "test1"]
print(list(zip(a, b)))


l = {k: v for k, v in zip(a, b)}
print(l)

fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
print(celsius)
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)