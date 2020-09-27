#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which accepts a sequence of comma-separated numbers from console  and generate a list. 
# 1. Create the below pattern using nested for loop in Python. 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# 

# In[1]:


num1 = 1
num2 = 5
for i in range(0,2*num2):
    if i<4:
        print(('*'*num1))
        num1 = num1 + 1
    else:
        print(('*'*num1))
        num1 = num1 - 1


# 2. Write a Python program to reverse a word after accepting the input from the user. Sample Output: 
# Input word: ineuron 
# Output: norueni
# 

# In[2]:


word = input("enter a word to reverse:")
for i in range(len(word)-1,-1,-1):
    print(word[i],end = "")


# In[ ]:




