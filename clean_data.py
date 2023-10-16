import pandas as pd

df = pd.read_csv(r"C:\Users\ADMIN\Downloads\hw5_supplementary-1\chart.csv")
df = df[0:167]
df = df[["Category", "Annual number of days"]]
df["Category"] = df["Category"].str[0:4]
df = df[df["Annual number of days"] != "-"]
df = df.rename(columns={'Category': 'Year', 'Annual number of days': 'days'})
df.to_csv("hw5.csv", index = False)