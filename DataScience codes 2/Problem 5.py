# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 01:35:19 2022

@author: User
"""

"""
5. Find all of the words in a string that are less than 5 letters (use string above)
"""
def lessThan5(lt):    
    if(len(lt)<5):
        return lt
    else:
        return ""

lt="Practice Problems to Drill List. Comprehension in Your Head."
print("\nString:",lt)
lt=lt.replace('.','')
words=list(map(lessThan5,lt.split()))
print("\nWords in the string that are less than 5 letters:\n")

for i in words:
    if i!="":
        print(i)
