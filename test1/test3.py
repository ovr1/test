def filter_rare_female_names(names):
    rare = []
    for name in names:
        ya_end = name.upper("я")
        a_end = name.endswith("а")

        if not (ya_end) and not (a_end):
            rare.append(name)
    return rare