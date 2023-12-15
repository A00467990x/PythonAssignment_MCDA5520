#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
"""
Created on Thu Dec 14 22:52:06 2023

@author: sammy

Python assignment, Question1
"""

def countVowel(word):
    vowels = "aeiouAEIOU"
    count = 0
    for i in word:
        if i in vowels:
            count= count + 1  
        else:
            pass
    
    return str(count)

print(countVowel("Awakening the Zodiac"))
print(countVowel("Awakning the Zodiac"))



df = pd.read_csv("titles1.csv")

print(df)


df['Vowels'] = df['title'].apply(countVowel)

print("aftervaddding new column:")
print(df)