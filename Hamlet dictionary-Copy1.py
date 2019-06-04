#!/usr/bin/env python
# coding: utf-8

# # 0. Take in a text file, save as a string

# In[5]:


data = ""

with open('hamlet.txt', 'r') as f:
    data = f.read()


# # 1. Inspect the string

# In[6]:


print (data)


# # 2. Cut the string up into individual words

# In[7]:


# split up a string (by default, by spaces)
list_1 = data.split() # individual words
print(list_1)


# In[8]:


# just look at the 1st 10 items in a list
list_1[:10]


# # 3. Realize we don't want punctuation mixed up with words

# # 4. Remove punctuation from original data before splitting

# In[9]:


# make copy of data
data_2 = ""
punctuation = '.,?"'
for letter in data:
    if letter not in punctuation:
        data_2 += letter

print(data_2) # inspect data_2


# # 5. Realize we want to compare words regardless of capitalization

# # 6. Convert the story to all lowercase letters

# In[10]:


# make our story entirely lowercase
data_2 = str.lower(data_2)
print(data_2)


# # 7. Make a dictionary of unique words where word frequency is the value

# In[11]:


# First, let's determine the keys by converting
# our list of words into a unique set
list_2 = data_2.split()
set_1 = set(list_2)
print(set_1)


# In[12]:


# Secondly, let's create an empty dictionary where all the values are 0
dict_1 = dict.fromkeys(set_1, 0)
print(dict_1)


# In[13]:


# Thirdly and lastly, we must update the count values for each word
# by looping through our story and counting up each word

for word in list_2:
    if word in dict_1:
        dict_1[word] += 1
        
print(dict_1)


# In[29]:


listing = [(k, v) for k, v in dict_1.items()]
#sorted(listing, reverse=false)
#print(sort(listing))
def getKey(item):
    return item[1]
sorted(listing, key=getKey,  reverse=True)


# In[ ]:




