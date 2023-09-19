import seaborn
import pandas
import numpy as np

raw_df = pandas.read_csv("./airquality.csv")
df = pandas.DataFrame(raw_df)

print(df.info())
