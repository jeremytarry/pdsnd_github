# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Creates a dictionary named 'flowers_dict' from the flowers.txt file.

fh = open('flowers.txt')

flower_dict = {}
for line in fh:
    words = line.split()
    flower_dict[words[0]] = words[1]

print(flowers_dict)
