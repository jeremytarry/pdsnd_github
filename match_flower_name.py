# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Write your code here

# HINT: create a dictionary from flowers.txt

fh = open('flowers.txt')

flower_dict = {}
for line in fh:
    words = line.split()
    flower_dict[words[0]] = words[1]

print(flowers_dict)
# HINT: create a function to ask for user's first and last name


# print the desired output