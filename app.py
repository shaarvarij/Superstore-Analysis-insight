import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/SampleSuperstore.csv')


df.info()
df.describe()
df.head()
df.isnull().sum() #check for missing values

import matplotlib.pyplot as plt
import seaborn as sns

# For better visuals
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")


region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

sns.barplot(x=region_sales.values, y=region_sales.index, palette='viridis')
plt.title('Sales by Region')
plt.xlabel('Sales ($)')
plt.show()


top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)

top_cities.plot(kind='barh', color='skyblue')
plt.title('Top 10 Cities by Sales')
plt.xlabel('Sales ($)')
plt.gca().invert_yaxis()
plt.show()


# Category
sns.barplot(x='Category', y='Sales', data=df, estimator=sum, ci=None, palette='pastel')
plt.title('Sales by Category')
plt.show()

# Sub-Category
subcat_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values()

subcat_sales.plot(kind='barh', color='coral')
plt.title('Sales by Sub-Category')
plt.xlabel('Sales ($)')
plt.show()


segment = df.groupby('Segment')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)

segment.plot(kind='bar', rot=0)
plt.title('Sales and Profit by Customer Segment')
plt.ylabel('$ Amount')
plt.show()


heatmap_data = df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum')

sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Sales Heatmap by Region and Category")
plt.show()


