#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_value = max(a_dictionary.values())
    for k in a_dictionary:
        if a_dictionary[k] == max_value:
            return k
