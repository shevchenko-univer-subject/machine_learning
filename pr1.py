import time
import os
import seaborn
import pandas
import numpy as np
import matplotlib.pyplot as plt

unique_id = str(int(time.time()))
folder_path = os.path.join(os.getcwd(), unique_id)
os.makedirs(folder_path, exist_ok=True)


raw_df = pandas.read_csv("./airquality.csv")
df = pandas.DataFrame(raw_df)
print(df.describe())

df_with_removed_records = df.dropna()
print("------ df_with_removed_records")
print(df_with_removed_records.describe())
print("cov")
print(df_with_removed_records.cov())
print("corr")
print(df_with_removed_records.corr())

df_filled_with_mean = df.fillna(df.mean())
print("------ df_filled_with_mean")
print(df_filled_with_mean.describe())
print("cov")
print(df_filled_with_mean.cov())
print("corr")
print(df_filled_with_mean.corr())


df_with_interpolated_values = df.interpolate() # default method is linear
print("------ df_with_interpolated_values")
print(df_with_interpolated_values.describe())
print("cov")
print(df_with_interpolated_values.cov())
print("corr")
print(df_with_interpolated_values.corr())

seaborn.boxplot(data=df_with_removed_records)
plt.savefig(os.path.join(folder_path, '1.png'))
seaborn.boxplot(data=df_filled_with_mean)
plt.savefig(os.path.join(folder_path, '2.png'))
seaborn.boxplot(data=df_with_interpolated_values)
plt.savefig(os.path.join(folder_path, '3.png'))
