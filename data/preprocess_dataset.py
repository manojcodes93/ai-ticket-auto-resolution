import pandas as pd

df = pd.read_csv(r"Q:\Projects\ai-ticket-auto-resolution\data\dataset-tickets-multi-lang-4-20k.csv")
print("Columns: ", df.columns)
df = df[df["language"] == "en"]

print("Total English Tickets: ", len(df))

df.to_csv("English_Tickets.csv", index = False)
print("English Dataset Created!!")