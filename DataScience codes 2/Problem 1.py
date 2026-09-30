# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 01:28:46 2022

@author: User
"""

"""
1. Find all of the numbers from 1–1000 that are divisible by 8.
"""

nums = [i for i in range(1,1001)]

filtered_nums= filter(lambda z:(z%8==0), nums)

print("\nNumbers that are disivible by 8 from 1 to 1000:\n")
for i in filtered_nums:
    print(i,end=" ")