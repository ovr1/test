def get_intersection(lhs, rhs):
    print(list(dict((x, (lhs + rhs).count(x)) for x in set(lhs + rhs) if (lhs + rhs).count(x) > 1)))

a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]
female_names = ['Аня', 'Маша', 'Света', 'Любовь', 'Женя', 'Саша']
male_names = ['Миша', 'Саша', 'Валентин', 'Женя', 'Егор']

get_intersection(a,b)
get_intersection(female_names, b)

get_intersection(female_names, male_names)






