def give_length(names):
    print(list(map(len,names)))

female_names = ['Аня', 'Маша', 'Света']
male_names = ['Денис', 'Рома', 'Петя']


give_length(female_names)
give_length(male_names)
give_length(male_names + female_names)