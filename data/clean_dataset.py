import pandas as pd
import re

df = pd.read_csv(r"Q:\Projects\ai-ticket-auto-resolution\data\synthetic-it-call-center-tickets.csv")
print("Size of Original dataset: ", len(df))

## Combining subject + body 
df["ticket"] = df["short_description"].fillna("") + " " + df["content"].fillna("")
df = df[["ticket", "subcategory", "close_notes"]]

df = df.rename(columns={
    "subcategory": "category",
    "close_notes": "answer"
})

df = df.dropna(subset = ["ticket", "category", "answer"])
print("Size after removing missing rows: ", len(df))

## Text cleaning
def clean_text(text):

    text = str(text).lower()

    # remove urls
    text = re.sub(r"http\S+", "", text)

    # remove placeholders like <tel_num> or [name]
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"\[.*?\]", " ", text)

    # remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

df["ticket"] = df["ticket"].apply(clean_text)
df["answer"] = df["answer"].apply(clean_text)

## removing short tickets
df = df[df["ticket"].str.split().str.len() > 10]
print("Size after removing short tickets: ", len(df))

## removing low quality answers
df = df[df["answer"].str.split().str.len() > 5]
print("Size after removing weak answers: ", len(df))

## Removing rare categories
category_counts = df["category"].value_counts()
df = df[df["category"].isin(category_counts[category_counts > 40].index)]
print("Size after removing rare categories: ", len(df))

## Resetting the index
df = df.reset_index(drop=True)


df.to_csv("data/final_it_tickets.csv", index=False)
print("\nClean dataset saved successfully!")
print("Final dataset size: ", len(df))

print("\nCategory distribution:\n")
print(df["category"].value_counts())