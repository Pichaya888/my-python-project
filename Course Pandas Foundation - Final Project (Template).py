# -*- coding: utf-8 -*-

# -- Project --

# # Final Project - Analyzing Sales Data
# 
# **Date**: 16 May 2025
# 
# **Author**: Pichaya udomsiri
# 
# **Course**: `Pandas Foundation`


# import data
import pandas as pd
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')

# TODO - convert order date and ship date to datetime in the original dataframed
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date']) 

print(df[['Order Date', 'Ship Date']].dtypes)

# TODO - count nan in postal code column
df['Postal Code'].isna().sum()

# TODO - filter rows with missing values
df[df['Postal Code'].isna()]

# TODO - Explore this dataset on your owns, ask your own questions
df.dropna().sort_values('Postal Code').head(10)

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
len(df)

len(df.columns)

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
df.isna().sum()

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
df2 = df.query('State == "California"')

df2.to_csv('mydata.csv')

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
# Ensure 'Order Date' is converted to datetime (if not already done)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Filter for California and Texas data in 2017
df_filtered = df[(df['State'].isin(['California', 'Texas'])) & (df['Order Date'].dt.year == 2017)]

# Export the filtered data to a CSV file
df_filtered.to_csv('california_texas_2017_orders.csv', index=False)

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
df['Order Date'] = pd.to_datetime(df['Order Date'])

df_2017 = df[df['Order Date'].dt.year == 2017]

total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
std_dev_sales = df['Sales'].std()

print(f"Total Sales in Sales: ${total_sales}")
print(f"Average Sales in Sales: ${average_sales:.2f}")
print(f"Standard Deviation of Sales in Sales: ${std_dev_sales:.2f}")

# TODO 06 - which Segment has the highest profit in 2018
df['Order Date'] = pd.to_datetime(df['Order Date'])

df_2018 = df[df['Order Date'].dt.year == 2018]

Segment_Profit = df_2018.groupby('Segment')['Profit'].sum()

highest_profit_Segment = Segment_Profit.idxmax()
highest_profit_value = Segment_Profit.max()

print(f"The segment with the highest profit in 2018 is: {highest_profit_Segment}")
print(f"Total Profit: ${highest_profit_value:.2f}")


# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
df['Order Date'] = pd.to_datetime(df['Order Date'])

start_date = '2019-04-15'
end_date = '2019-12-31'
mask = (df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)
df_filtered = df[mask]

state_sales = df_filtered.groupby('State')['Sales'].sum()

least_sales_states = state_sales.nsmallest(5)

# Display result
print("Top 5 States with the Least Total Sales (15 April 2019 - 31 Dec 2019):")
print(least_sales_states)

# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
df['Order Date'] = pd.to_datetime(df['Order Date'])

df_2019 = df[df['Order Date'].dt.year == 2019]

west_central_df = df_2019[df_2019['Region'].isin(['West', 'Çentral'])]

total_sales_2019 = df_2019['Sales'].sum()
west_central_sales = west_central_df['Sales'].sum()

proportion = (west_central_sales / total_sales_2019) * 100

# Display result
print(f"Proportion of total sales in West + Central (2019): {proportion:.2f}%")

    

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020

df['Order Date'] = pd.to_datetime(df['Order Date'])

df_filtered = df[(df['Order Date'].dt.year >= 2019) & (df['Order Date'].dt.year <= 2020)]

product_stats = df_filtered.groupby('Product Name').agg(
    Number_of_Orders = ('Order ID' , 'count'),
    Total_Sales = ('Sales', 'sum')   
).sort_values(by='Number_of_Orders', ascending=False)

top_10_products = product_stats.head(10)

# Display result
print("Top 10 Products (2019–2020) by Number of Orders:")
print(top_10_products)

# TODO 10 - plot at least 2 plots, any plot you think interesting :)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df['Order Date'] = pd.to_datetime(df['Order Date'])

# Filter data for 2019 and 2020
df_filtered = df[(df['Order Date'].dt.year >= 2019) & (df['Order Date'].dt.year <= 2020)]

# Group by Product Name
product_stats = df_filtered.groupby('Product Name').agg(
    Number_of_Orders=('Order ID', 'count'),
    Total_Sales=('Sales', 'sum')
)

# Top 10 by number of orders
top10_orders = product_stats.sort_values(by='Number_of_Orders', ascending=False).head(10)

# Top 10 by total sales
top10_sales = product_stats.sort_values(by='Total_Sales', ascending=False).head(10)

# Plot 1: Bar plot - Number of Orders
plt.figure(figsize=(12, 6))
sns.barplot(x=top10_orders['Number_of_Orders'], y=top10_orders.index, palette='viridis')
plt.title('Top 10 Products by Number of Orders (2019–2020)')
plt.xlabel('Number of Orders')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()

# Plot 2: Horizontal Bar plot - Total Sales
plt.figure(figsize=(12, 6))
sns.barplot(x=top10_sales['Total_Sales'], y=top10_sales.index, palette='magma')
plt.title('Top 10 Products by Total Sales (2019–2020)')
plt.xlabel('Total Sales ($)')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()






