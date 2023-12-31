#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] == 0:
                    print("division by 0")
                else:
                    result = my_list_1[i] / my_list_2[i]
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
