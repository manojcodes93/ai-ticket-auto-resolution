import pandas as pd

df = pd.read_csv(r"Q:\Projects\ai-ticket-auto-resolution\data\English_Tickets.csv")

df["ticket"] = df["subject"].fillna('') + " " + df["body"].fillna('')
df = df[["ticket", "queue", "answer"]]
df = df.rename(columns={"queue": "category"})

df = df.dropna()
df = df.reset_index(drop=True)
df.to_csv("cleaned_tickets.csv", index=False)

print("Cleaned Dataset Created")
print("Total tickets: ", len(df))