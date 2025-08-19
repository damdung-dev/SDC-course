#Exercise1

'''import numpy as np

vector_a=np.array([2,1])
vector_b=np.array([3,5])
vector_c=np.array([3,3])

dot_productab=np.dot(vector_a,vector_b)
dot_productac=np.dot(vector_a,vector_c)
dot_productbc=np.dot(vector_b,vector_c)
print(dot_productbc)

cosine_ab=dot_productab/(np.linalg.norm(vector_a)*np.linalg.norm(vector_b))
cosine_ac=dot_productac/(np.linalg.norm(vector_a)*np.linalg.norm(vector_c))
cosine_bc=dot_productbc/(np.linalg.norm(vector_b)*np.linalg.norm(vector_c))
print(cosine_ab,cosine_ac,cosine_bc)
angle_ab=np.arccos(cosine_ab)
angle_ac=np.arccos(cosine_ac)
angle_bc=np.arccos(cosine_bc)
print(angle_ab,angle_ac,angle_bc)
degree_ab=np.degrees(angle_ab)
degree_ac=np.degrees(angle_ac)
degree_bc=np.degrees(angle_bc)

print(degree_ab,degree_ac,degree_bc)'''


#Exercise 2

'''import numpy as np

#y=ax+b
a_elements=np.random.randint(0,10,(2,2))
b_elements=np.random.randint(0,10,(2,2))
a=np.array(a_elements)
b=np.array(b_elements)
a_inv=np.linalg.inv(a)
dot_product=np.dot(a_inv,b)
print(dot_product)'''

#Exercise 3
import numpy as np
import datetime
import pandas as pd


stock={
    "vnindex":[[1226.8,datetime.datetime(2025,4,28)],
               [1226.3,datetime.datetime(2025,4,29)],
               [1240.5,datetime.datetime(2025,5,5)],
               [1241.95,datetime.datetime(2025,5,6)],
               [1250.37,datetime.datetime(2025,5,7)],
               [1269.9,datetime.datetime(2025,5,8)],
               [1267.3,datetime.datetime(2025,5,9)],
               [1283.28,datetime.datetime(2025,5,12)]],
    "hnxindex":[[211.45,datetime.datetime(2025,4,28)],
               [211.94,datetime.datetime(2025,4,29)],
               [212.81,datetime.datetime(2025,5,5)],
               [212.89,datetime.datetime(2025,5,6)],
               [213.41,datetime.datetime(2025,5,7)],
               [215.23,datetime.datetime(2025,5,8)],
               [214.13,datetime.datetime(2025,5,9)],
               [216.04,datetime.datetime(2025,5,12)]],
    "vn30":[[1312.32,datetime.datetime(2025,4,28)],
               [1309.73,datetime.datetime(2025,4,29)],
               [1320.41,datetime.datetime(2025,5,5)],
               [1319.66,datetime.datetime(2025,5,6)],
               [1324.8,datetime.datetime(2025,5,7)],
               [1351.1,datetime.datetime(2025,5,8)],
               [1352.25,datetime.datetime(2025,5,9)],
               [1372.04,datetime.datetime(2025,5,12)]]
}
dates = [item[1] for item in stock["vnindex"]]
vnindex_values = [item[0] for item in stock["vnindex"]]
hnxindex_values = [item[0] for item in stock["hnxindex"]]
vn30_values = [item[0] for item in stock["vn30"]]

df = pd.DataFrame({
    "Date": dates,
    "VN-Index": vnindex_values,
    "HNX-Index": hnxindex_values,
    "VN30": vn30_values
})

df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%d/%m/%Y")
print("Covariance Matrix:\n", df[["VN-Index","HNX-Index","VN30"]].cov())
print("\nCorrelation Matrix:\n", df[["VN-Index","HNX-Index","VN30"]].corr())

vnindex_hnxindex_arr=df[["VN-Index","HNX-Index"]].to_numpy()
vnindex_vn30=df[["VN-Index","VN30"]].to_numpy()
hnxindex_vn30=df[["HNX-Index","VN30"]].to_numpy()
print("Pearson product-moment correlation VN-Index and VN30: ", np.corrcoef(vnindex_vn30)[0,1])
print("Pearson product-moment correlation VN-Index and HNX-Index", np.corrcoef(vnindex_hnxindex_arr)[0,1])
print("Pearson product-moment correlation HNX-Index and VN30", np.corrcoef(hnxindex_vn30)[0,1])

vnindex_arr=df[["VN-Index"]].to_numpy()
vn30_arr=df[["VN30"]].to_numpy()
hnxindex_arr=df[["HNX-Index"]].to_numpy()
print("Covariance matrix: ", np.cov(vnindex_hnxindex_arr))
print("Covariance matrix: ", np.cov(vnindex_vn30))
print("Covariance matrix: ", np.cov(hnxindex_vn30))


