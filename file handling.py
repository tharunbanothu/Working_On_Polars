#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("example.txt","r") as file:
    data= file.read()
    print(data)


# In[7]:


with open("example.txt", "w") as file:
    file.write("i am the hero\n")
    file.write("i love melons")


# In[8]:


with open("example.txt","r") as file:
    data= file.read()
    print(data)


# In[39]:


with open("example.txt","w+") as file:
    file.write("hey, you are my super hero\n")
    file.write("you are my ironMan")
    file.seek(0)
    data= file.read()
    print(data)


# In[40]:


with open("example.txt","r+") as file:
    file.write("hey, you are my super hero\n")
    file.write("you are my ironMan")
    file.seek(0)
    data= file.read()
    print(data)


# In[41]:


with open("example.txt","a") as file:
    file.write("hey beautiful\n")
    file.write("you look amazing\n")


# In[42]:


with open("example.txt","r") as file:
    data = file.read()
    print(data)


# In[43]:


content=["samantha, are you ready \n","yes, tharun lets start \n","wow thats a great play rupa \n"]
with open("example.txt","a") as file:
    file.writelines(content)


# In[44]:


with open("example.txt","r") as file:
    data = file.read()
    print(data)


# In[48]:


def count_of_file(file_path):
    with open(file_path,"r") as file:
        lines= file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        
    return line_count,word_count, char_count

print(count_of_file("example.txt"))
        
        


# In[47]:


def count_of_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

    return line_count, word_count, char_count

print(count_of_file("example.txt"))


# In[ ]:




