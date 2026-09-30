# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 01:35:50 2022

@author: User
"""

"""
6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)
"""

string = "Practice Problems to Drill List Comprehension in Your Head."
print("\nLength of each word:\n")
string=string.replace('.', '')
lst=string.split(" ")
dct={i:len(i) for i in lst}
for i,j in dct.items():
    print(i,":",j)