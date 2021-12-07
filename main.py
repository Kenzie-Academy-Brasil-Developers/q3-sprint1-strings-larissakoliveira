def standardize_names(name):
    remove_black_spaces = name.strip()
    split_words =  remove_black_spaces.split(' ')
    words_len = len(split_words)
    if words_len == 1:
        return remove_black_spaces
    else:
        return str('-'.join(split_words))

hero_standardized = standardize_names(" Batman     ")
print(hero_standardized)

hero_standardized = standardize_names("      Super Man")
print(hero_standardized)