import seaborn
import pandas
import numpy as np

raw_df = pandas.read_csv("./airquality.csv")
df = pandas.DataFrame(raw_df)

print(df.describe())

df_with_removed_records = df.dropna()
print("------ df_with_removed_records")
print(df_with_removed_records.describe())
# build correlation matrix 

df_filled_with_mean = df.fillna(df.mean())
print("------ df_filled_with_mean")
print(df_filled_with_mean.describe())

df_with_interpolated_values = df.interpolate() # default method is linear
print("------ df_with_interpolated_values")
print(df_with_interpolated_values.describe())
