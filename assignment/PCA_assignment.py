import csv
import pandas as pd
import numpy as np

df=pd.read_csv("D:\\data for education system\\datasets\\student-scores.csv")
df=np.array(df)
print(df)