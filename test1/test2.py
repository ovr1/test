def filter_rare_female_names(names):
    N =[]
    for name in names:
        if (5<= len(name)) and (('Л' in (name[0])) or ('А' in (name[0]))):
            N.append(name)
    print(N)


female_names = ['Аня', 'Маша', 'Света', 'Любовь']
#Это даст нам:

filter_rare_female_names(female_names)
filter_rare_female_names(["Анна", "Мария"])
filter_rare_female_names(["Адель"])