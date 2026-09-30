# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 01:36:25 2022

@author: User
"""

"""
7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any
single digit besides 1 (2–9)
"""
single_dgt=[2,3,4,5,6,7,8,9]
print("\nNumbers from 1–1000 divisible by any single digit:\n")
nums=[[j for j in range(1,1001) if (j%i==0)] for i in single_dgt]
nums2=[y for x in nums for y in x ]
nums2=list(set(nums2))
for i in nums2:
    print(i,end=" ")
