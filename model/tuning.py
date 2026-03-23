import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

## Loading dataset
df = pd.read_csv("data/final_it_tickets.csv")

X = df["ticket"]
y = df["category"]

## Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

## TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=30000,
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.9
)

X_train = vectorizer.fit_transform(X_train)

## Hyperparameter tuning
param_grid = {
    "C": [0.5, 1, 2, 5]
}

grid = GridSearchCV(
    LogisticRegression(max_iter=1000),
    param_grid,
    cv=3,
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("Best params:", grid.best_params_)