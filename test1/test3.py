def filter_rare_female_names(names):
    rare = []
    for name in names:
        ya_end = name.endswith("я")
        a_end = name.endswith("а")

        if not (ya_end) and not (a_end):
            rare.append(name)
    print(rare)

female_names = ['Аня', 'Маша', 'Света', 'Любовь']
#Это даст нам:

filter_rare_female_names(female_names)
filter_rare_female_names(["Анна", "Мария"])
filter_rare_female_names(["Адель"])