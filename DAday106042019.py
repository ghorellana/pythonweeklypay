#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input("Enter your name: ")
response="Hello, " + name + "!"
print (response)


# In[10]:


response = input("Input something ")
print (response)


# In[12]:


var1 = int(input('value'))
if var1 < 5:
    print("You are a child")


# # Steps(Markdown)
# 1- Order Pizza
# 2- Pay
# 3- Eat
# 4- rest

# In[2]:



1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Integer division rounds down for both positive and negative numbers.
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0 # works on floats too
-5.0 // 3.0  # => -2.0

# The result of division is always a float
10.0 / 3  # => 3.3333333333333335

# Modulo operation
7 % 3  # => 1

# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# Enforce precedence with parentheses
(1 + 3) * 2  # => 8


# In[15]:



for i in range(4, 8, ):
    print (i)


# In[25]:


for n in range(1, 100):
    if n%3 == 0:
        print('Fizz')
    elif n%5 == 0:
        print('Buzz')
    elif (n%3 != 0 and n%5 != 0):
        print('FizzBuzz')
    else:
        print (n)
        


# In[27]:


wage = float(input("Enter wage: $"))
regularhours = float(input("Enter regular hours: $"))
overtimehrs = float(input("Enter OT: $"))
totalpay = float((wage*regularhours)+(wage*1.5*overtimehrs))
print("The total weekly pay is $" + str(round(totalpay, 2)))


# In[47]:


for bottle in range(99, 0, -1):
    print(str(bottle) + " bottles on the wall, " + str
          (bottle-1) + " bottles left")
    if bottle ==1:
        print("finished")


# In[49]:


intro = "My Name is Avi"
intro.isalpha()


# In[51]:


newstr = "2019-6-24"
newstr.split("-")


# In[52]:


extra = "           hello world            "
print("X{}X".format(extra.strip()))


# In[ ]:


while True:
        answer = input 
        if answer.lower() == 'q':
            

