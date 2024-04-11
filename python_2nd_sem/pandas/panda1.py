# import pandas as pd
# # data = pd.Series([10, 20, 45, 50])
# # print(data, type(data))


# series = pd.Series(['ravi', 'saket', 'rahul','sanskar'])
# print(series)


import pandas as pd

# Sample DataFrame
data = {'Date': ['2024-01-01', '2024-01-05', '2024-02-02', '2024-02-15'],
        'Product': ['A', 'B', 'A', 'C'],
        'Revenue': [100, 200, 150, 120]}
df = pd.DataFrame(data)

# Function to find top 3 selling products for each month
def top_selling_products(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    top_products = df.groupby(['Month', 'Product']).sum()
    top_products = top_products.groupby('Month').apply(lambda x: x.nlargest(3, 'Revenue')).reset_index(drop=True)
    return top_products

print(top_selling_products(df))