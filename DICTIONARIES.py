#!/usr/bin/env python
# coding: utf-8

# # DICTIONARY IN PYTHON

# #GROUP OF (KEY,VALUE) ,PAIRS SEPARATED WITH COMMA(,) AND ENCLOSED IN CURLY BREAKET
# 

# In[2]:


DICT={"NAME":"abc","rno":"312","dept":"se"}
#      key     value 
# (NAME,abc),(rno,312),(dept,se) are the item of dictionary 


# In[3]:


# how to create a dictionary 
# empty dictionary
dict={}

# how to create dictionary with elements 
# dict={key1:value1,key2:value2........}
#dict={ key1:value1,
#         key2:value2,
#     key3:value3 }
# by using dictionary function we also create dictionary
#dict( [(key1:value1),(key2:value2...)])
#we also create dictionary by using dictionary comprehension
# we need to specify the following order
1 expression
2 iteration
3 condition
for example 
dict={ expression iteration condition}
 dict={x:x**2  for x in range(5) if x%2==0}
    
# # how to accessing elements
with the help of keys we can acces the corresponding values

# In[6]:


# for exmple 
dict={"name":"adil","rolno":"123","dept":"se"}
dict["name"]
print(dict["rolno"])


# In[7]:


dict.items()


# In[8]:


dict.keys()


# In[9]:


dict.values()


# In[10]:


d={'name':'adil',"father_name":"ghulam murtaza","roll_no":"12345","branch":"sce"}
d['name']


# In[11]:


# how to adding  new element to dict
# for example
d={'name':'adil',"father_name":"ghulam murtaza","roll_no":"12345","branch":"sce"}
d["course"]="software"
print(d)


# In[12]:


# how to modify  element to dict
# for example
d["branch"]="islamabad"
print(d)


# In[13]:


# how to deleting  element to dict
# for example
del d["course"]
print(d)


# In[15]:


d.clear()
print(d)


# In[ ]:




