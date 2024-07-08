import os
import pandas as pd
import matplotlib.pyplot as plt

#loading data
df = pd.read_csv(r'd:\DataAnalysus\archive\sales_data_sample.csv', encoding='ISO-8859-1')

#inspecting and cleaning
print(df.head())
print(df.info())
df=df.dropna() #handle missing values
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE']) #conversion to datetime for easy sort and filtering

#adding derived columns
df['YEAR'] = df['ORDERDATE'].dt.year
df['MONTH'] = df['ORDERDATE'].dt.month

#exploratory data analysis (EDA)
#1 sales trend over time
df.groupby('ORDERDATE')['SALES'].sum().plot()
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.show()

#2 sales by product line
df.groupby('ORDERDATE')['SALES'].sum().plot(kind='bar')
plt.title('Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Sales Amount')
plt.show()

#3 sales by country
df.groupby('ORDERDATE')['SALES'].sum().plot(kind='bar')
plt.title('Sales by country')
plt.xlabel('Country')
plt.ylabel('Sales Amount')
plt.show()

df.to_csv('cleaned_sales.csv', index = False)


