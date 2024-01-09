#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        print(str(k) + ': ' + str(a_dictionary[k]))
