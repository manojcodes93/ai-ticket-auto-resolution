import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("Q:/Projects/ai-ticket-auto-resolution/data/tickets.csv")

X = data["ticket"]
y = data["category"]

vectorizer = TfidfVectorizer()
model = LogisticRegression()

X_vectors = vectorizer.fit_transform(X)
model.fit(X_vectors, y)

## Saving the model
pickle.dump(model, open("model.pkl", "wb"))

## Saving hte vectorizer
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
