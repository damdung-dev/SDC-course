import pandas as pd
import matplotlib.pyplot as plt

'''data=pd.read_csv('D:\\SDC_course\\processing_of_data\\products.csv')
data.dropna(inplace=True)
data['Date']=pd.to_datetime(data['Date'],format="mixed")
data.dropna(subset='Date',inplace=True)
data.drop_duplicates(inplace=True)
data.loc[7,"Duration"]=45
print(data)
data.plot()
data.plot(kind="scatter",x="Calories",y="Duration")
plt.show()'''

data=pd.read_csv("D:\\relity_data\\order_and_supply_chain_dataset\\Ecommerce Order Dataset\\train\\df_OrderItems.csv")
data.dropna(inplace=True)
data['price']=data['price'].astype(int)
data.drop_duplicates(inplace=True)
data.plot(kind="scatter",x="price",y="shipping_charges")
print(data)
plt.show()