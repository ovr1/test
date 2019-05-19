def filter_rare_female_names(names):
    return [name for name in names if not(name.endswith("я")) and not(name.endswith("а"))]



female_names = ['Аня', 'Маша', 'Света', 'Любовь']

filter_rare_female_names(female_names)
filter_rare_female_names(["Анна", "Мария"])

filter_rare_female_names(["Адель"])