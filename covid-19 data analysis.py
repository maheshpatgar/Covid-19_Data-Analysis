#!/usr/bin/env python
# coding: utf-8

# In[86]:


import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv(r"C:\Users\lokesh\Downloads\covid.csv")
df.head(10)


# In[87]:


df.drop(columns=["NewCases","NewDeaths","NewRecovered","iso_alpha","WHO Region"],inplace=True)


# In[88]:


df.head(10)


# In[89]:


df.drop(columns =["Serious,Critical"],inplace=True)


# In[90]:


df.head(10)


# In[91]:


df["TotalDeaths"].fillna(df["TotalDeaths"].mean(),inplace=True)


# In[92]:


df["Deaths/1M pop"].fillna(df["Deaths/1M pop"].mean(),inplace=True)


# In[93]:


df["TotalTests"].fillna(df["TotalTests"].mean(),inplace=True)


# In[94]:


df["Tests/1M pop"].fillna(df["Tests/1M pop"].mean(),inplace=True)


# In[95]:


df["Population"].fillna(df["Population"].mean(),inplace=True)


# In[96]:


df["TotalRecovered"].fillna(df["TotalRecovered"].median(),inplace=True)


# In[97]:


df["ActiveCases"].fillna(df["ActiveCases"].median(),inplace=True)


# In[98]:


df.head(20)


# In[99]:


df.isnull().sum()


# In[100]:


df["Tot Cases/1M pop"].fillna(df["Tot Cases/1M pop"].mean(),inplace=True)


# In[101]:


df.isnull().sum()


# In[102]:


df.fillna("Asia")


# In[103]:


df.isnull().sum()


# In[104]:


df["Continent"].fillna("Asia", inplace=True)


# In[105]:


df['Continent'].head(5)


# In[106]:


import pandas as pd
import matplotlib.pyplot as plt

top_cases = df.sort_values(by='TotalCases', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top_cases['Country/Region'], top_cases['TotalCases'])
plt.xticks(rotation=45)
plt.title('Top 10 Countries by Total COVID Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.show()


# In[107]:


top_deaths = df.sort_values(by='TotalDeaths', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top_deaths['Country/Region'], top_deaths['TotalDeaths'])
plt.xticks(rotation=45)
plt.title('Top 10 Countries by Total Deaths')
plt.xlabel('Country')
plt.ylabel('Total Deaths')
plt.show()


# In[108]:


continent_cases = df.groupby('Continent')['TotalCases'].sum()

plt.figure(figsize=(8,8))
plt.pie(continent_cases, labels=continent_cases.index, autopct='%1.1f%%')
plt.title('Total COVID Cases by Continent')
plt.show()


# In[109]:


plt.figure(figsize=(10,6))
plt.scatter(df['Population'], df['TotalCases'])
plt.title('Population vs Total Cases')
plt.xlabel('Population')
plt.ylabel('Total Cases')
plt.show()


# In[110]:


plt.figure(figsize=(10,6))
plt.hist(df['TotalCases'], bins=20)
plt.title('Distribution of Total Cases')
plt.xlabel('Total Cases')
plt.ylabel('Number of Countries')
plt.show()


# In[111]:


plt.figure(figsize=(12,6))
df.boxplot(column='Tot Cases/1M pop', by='Continent')
plt.title('Cases Per Million by Continent')
plt.suptitle('')
plt.xlabel('Continent')
plt.ylabel('Cases Per 1M Population')
plt.xticks(rotation=45)
plt.show()


# In[112]:


import seaborn as sns

numeric_df = df.select_dtypes(include='number')

plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[113]:


df.rename(columns={'Country/Region': 'Country'}, inplace=True)


# In[114]:


df.columns


# In[115]:


df['DeathRate'] = (df['TotalDeaths'] / df['TotalCases']) * 100
df['RecoveryRate'] = (df['TotalRecovered'] / df['TotalCases']) * 100
df['ActiveRate'] = (df['ActiveCases'] / df['TotalCases']) * 100


# In[116]:


df.head()


# In[118]:


from sqlalchemy import create_engine

username="root"
password="Karavali%402022"
host="localhost"
port = "3306"
database = "covidsql"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

table_name = "corona" 
df.to_sql(table_name, engine, if_exists="replace", index=False)

pd.read_sql("SELECT * FROM corona LIMIT 5;", engine)


# In[ ]:





# In[ ]:




