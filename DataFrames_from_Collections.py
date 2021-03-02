#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Create DataFrame from excel,Sql,List,Map,Set,Tuple


# In[3]:


import os
print(os.path)


# In[15]:


#Create df from Excel
import pandas as pd
df=pd.read_csv("C:\\Users\\pavan\\OneDrive\\Documents\\Harika Python Project and  data files\\App1.csv")
print(df['App'].tail()) # getting the dtype just for one column
df.dtypes # getting dtypes for all the columns on the df


# In[18]:


#Filtering from df(removing the particular row from a column in a df )
df1=df[df["App"]==9065]
df1


# In[19]:


# Creating df from SQl
#df=pd.read_sql(conn,sql)


# In[22]:


## Create df from list
import pandas as pd
lst = ['Harika','Pavan','Shine','Twinkle','Rudra']
df_lst1=pd.DataFrame(lst)
df_lst1


# In[38]:


# Providing Columns & Indexes
df_lst1=pd.DataFrame(lst,columns=['Names'])
df_lst1


# In[40]:


#Assigning Columns & Indexes
df_lst1=pd.DataFrame(lst,columns=['Names'],index=['x','y','z','A','B'])
df_lst1


# In[50]:


# Creating a DF from 2 lists using Zip.
lst1=['Harika','Pavan','Shine','Twinkle','Rudra']
lst2=['L','XL','M','S','Baby']
lst3=['Gorgeous','Mental','Pretty','Cute','Adoreable']
l1_lst1=pd.DataFrame(list(zip(lst1,lst2,lst3)))
l1_lst1
l1_lst1=pd.DataFrame(list(zip(lst1,lst2,lst3)), columns=['Name','Size','Type']) # Assigning the Column names
l1_lst1


# In[51]:


ROLE = 'PAVAN'
print("Role: ",ROLE)


# In[ ]:




