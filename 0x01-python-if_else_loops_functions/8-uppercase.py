#!/usr/bin/python3
def uppercase(str):
    for char in str:
        diff = 32 if ord(char) >= 97 and ord(char) <= 122 else 0
        print("{:c}".format(ord(char) - diff), end="")
    print()
