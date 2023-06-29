#!/usr/bin/env python
# coding: utf-8

# ## Q1. What does an empty dictionary's code look like?

# Sol.1: Two curly brackets: {}

# In[2]:


{}


# ## Q2. What is the value of a dictionary value with the key 'foo' and the value 42?

# In[4]:


#Sol.2:   
{'foo': 42}


# ## Q3. What is the most significant distinction between a dictionary and a list?

# 3. The items stored in a dictionary are unordered , while the items in a list 
# are ordered.

# ## Q4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# Sol.4: You get a KeyError error.

# In[5]:


spam={'bar':100}
spam['foo']


# ## Q5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and'cat' in spam.keys()?

# Sol.5: There is no difference. The in operator checks whether a value exists as 
# a key in the dictionary.

# ## Q6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

# Sol.6: The 'cat' in spam checks whether there is a 'cat' key in the dictionary, 
# while 'cat' in spam.values() checks whether there is a value 'cat' for 
# one of the keys in spam.

# ## Q7. What is a shortcut for the following code?
# #### if 'color' not in spam:
# ####          spam['color']='black'

# In[7]:


# Sol.7: 
spam.setdefault('color', 'black')


# ## Q8. How do you "pretty print" dictionary values using which module and function?

# There are different ways to ‘pretty print’ dictionary values in Python, but one of the most common methods is to use the pprint module and its pprint() function. This module allows you to format and sort the dictionary keys and values in a more readable way. For example:

# In[12]:


import pprint
sample_dict = {'age': 31,'gender': 'male','books': ['Harry Potter','Lord of the Rings']}
pprint.pprint(sample_dict)


# In[ ]:




