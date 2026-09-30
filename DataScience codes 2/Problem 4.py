# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 01:34:37 2022

@author: User
"""

"""
4. Remove all of the vowels in a string (use string above)
"""

vowels = ['a', 'e', 'i', 'o', 'u']
lt="Practice Problems to Drill List Comprehension in Your Head."
filteredVowels = filter(lambda i: (i not in vowels) , lt)
print("\nString:",lt)
print("\nNew string:","".join(list(filteredVowels)))