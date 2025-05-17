#!/usr/bin/env python
# coding: utf-8

# In[1]:


import polars as pl


# In[2]:


pip i polars


# In[3]:


pip install polars


# In[4]:


import polars as pl


# In[7]:


import datetime as dt 
df= pl.DataFrame({
    "name":["tharun",'rupa','roshan','karthik'],
    "birthday":[
        dt.date(2003,1,5),
        dt.date(2003,1,26),
        dt.date(2002,7,23),
        dt.date(2002,6,24),
    ],
    "weight":[65,58,72,70],   #in kgs
    "height":[1.56, 1.77, 1.65, 1.75]   #in mts
})


# In[8]:


print(df)


# In[9]:


df.write_csv("C:/Users/banot/OneDrive/Desktop/output.csv")


# In[11]:


df_csv=pl.read_csv("C:/Users/banot/OneDrive/Desktop/output.csv",try_parse_dates=True)
print(df_csv)


# In[18]:


result= df.select(
    pl.col("name"),
    pl.col("birthday").dt.year().alias("birth_year"),
    (pl.col("weight") / (pl.col("height")**2)).alias("bmi"),
)
print(result)


# In[19]:


res = df.select(
    pl.col("name"),
    (pl.col("weight","height") * 0.95 ).round(2).name.suffix("-5%"),
)
print(res)


# In[20]:


print(df)


# In[22]:


result1= df.with_columns(
    birth_year = pl.col("birthday").dt.year(),
    bmi = (pl.col("weight") / (pl.col("height")**2 ) ),
)
print(result1)


# In[29]:


result_above_2003= df.filter(
    pl.col("birthday").dt.year()>=2003,
)
print(result_above_2003)


# In[30]:


result3= df.filter(
    pl.col("birthday").is_between(dt.date(2003,1,1),dt.date(2003,2,2)),
    pl.col("weight") >55,
    
)
print(result3)


# In[55]:


count_of_birth_in_decade = df.group_by(
    (pl.col("birthday").dt.year() // 10 *10 ).alias("decade"),
    maintain_order=True,
).len()
print(count_of_birth_in_decade)


# In[42]:


df3 = pl.DataFrame(
    {
        "name": ["Ethan Edwards", "Fiona Foster", "Grace Gibson", "Henry Harris"],
        "birthday": [
            dt.date(1977, 5, 10),
            dt.date(1975, 6, 23),
            dt.date(1973, 7, 22),
            dt.date(1971, 8, 3),
        ],
        "weight": [67, 72, 57, 93],  # (kg)
        "height": [1.76, 1.6, 1.66, 1.8],  # (m)
    }
)

df4 = pl.concat([df, df3], how="vertical")


# In[ ]:





# In[47]:


print(df4)


# In[54]:


count_of_birth_in_decade = df4.group_by(
    (pl.col("birthday").dt.year() // 10 * 10).alias("decade"),
    maintain_order=True,
).len()
print(count_of_birth_in_decade)


# In[52]:


df_additional_details = pl.DataFrame({
    "name":["tharun",'rupa','roshan','karthik',"Ethan Edwards", "Fiona Foster", "Grace Gibson", "Henry Harris"],
    "parents":[True, False,True,True,True,True,False,True],
    "siblings":[1,3,2,4,1,2,3,4],
})
df5 = df4.join(df_additional_details, on="name", how="left")

print(df5)


# In[53]:


df_additional_details = pl.DataFrame({
    "name":["tharun",'rupa','roshan','karthik',"Ethan Edwards", "Fiona Foster", "Grace Gibson", "Henry Harris"],
    "parents":[True, False,True,True,True,True,False,True],
    "siblings":[1,3,2,4,1,2,3,4],
})
df5 = df4.join(df_additional_details, on="name", how="right")

print(df5)


# In[57]:


final_result = ( df5.with_columns(
    ( pl.col("birthday").dt.year() // 10 * 10 ).alias("decade"),
    pl.col("name").str.split(by=" ").list.first(),
)
.select( pl.all().exclude("birthday"))
.group_by(
    pl.col("decade"),
    maintain_order= True
)
.agg(
    pl.col("name"),
    pl.col("weight","height").mean().round(2).name.prefix("avg_")
)
               
)
print(final_result)


# In[ ]:




