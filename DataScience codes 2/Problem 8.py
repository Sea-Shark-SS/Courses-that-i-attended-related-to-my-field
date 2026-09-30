# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 01:37:08 2022

@author: User
"""

"""
8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single
digit any of the numbers is divisible by
"""
div_hghst_num={k:v for k in range(1,1001) for v in range(1,10) if(k%v==0)}
print("\nThe highest single digit for the number of 1–1000 is:\n")
for i,j in div_hghst_num.items():
    print(i,':',j,"    ", end="")