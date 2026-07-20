import pandas as pd

df = pd.read_csv("data/raw/customers.csv")

df.loc[df["Account_Manager_ID"] == 100, "Account_Manager_ID"] = 99

df.to_csv("data/raw/customers.csv", index=False)

print("Done")

