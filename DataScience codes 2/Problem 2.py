# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 01:33:37 2022

@author: User
"""

"""
2. Find all of the numbers from 1–1000 that have a 6 in them.
"""
nums = [i for i in range(1,1001)]
filtered_nums= filter(lambda n:('6'in str(n)), nums)
print("\n\nNumbers that have '6' from 1 to 1000:\n")
for i in filtered_nums:
    print(i,end=" ")
    