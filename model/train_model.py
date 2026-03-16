import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv(r"Q:\Projects\ai-ticket-auto-resolution\data\final_it_tickets.csv")
print("Dataset loaded")

X = df["ticket"]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.23, random_state = 42, stratify = y)

##Converting the text into vectors
vectorizer = TfidfVectorizer(stop_words = "english", max_features = 20000, ngram_range=(1,2), min_df=2)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
print("Vectorization complete")

model = LogisticRegression(max_iter = 1000, class_weight="balanced")
model.fit(X_train_vec, y_train)
print("Model training is completed")

y_pred = model.predict(X_test_vec)

print("\nAccuracy: ", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("\nModel saved successfully!")