import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("spam_dataset.csv")

# Remove unnecessary columns
df.drop(columns=["Email No."], inplace=True)  # Keeping only word frequency columns

# Splitting features (X) and target (y)
X_text = df.drop(columns=["Prediction"])  # All text features
y = df["Prediction"]  # Target column

# Convert feature names (word frequencies) to a single text representation
X_text_combined = X_text.apply(lambda row: " ".join([f"{col} " * row[col] for col in X_text.columns]), axis=1)

# **TF-IDF Vectorization**
vectorizer = TfidfVectorizer(max_features=3000)  # Limiting features to 3000 most important words
X_tfidf = vectorizer.fit_transform(X_text_combined)

# Save the vectorizer
with open("vectorizer.pkl", "wb") as vec_file:
    pickle.dump(vectorizer, vec_file)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Model selection: Testing different classifiers
models = {
    "NaiveBayes": MultinomialNB(),
    "SVM": SVC(),
    "RandomForest": RandomForestClassifier()
}

# Hyperparameter tuning for the best model
param_grid = {
    "NaiveBayes": {"alpha": [0.1, 0.5, 1.0]},
    "SVM": {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]},
    "RandomForest": {"n_estimators": [50, 100, 200], "max_depth": [10, 20, None]}
}

best_model = None
best_score = 0

for model_name, model in models.items():
    print(f"Training {model_name}...")
    grid_search = GridSearchCV(model, param_grid[model_name], cv=5, scoring="accuracy", n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    best_params = grid_search.best_params_
    best_estimator = grid_search.best_estimator_
    
    # Evaluate on test set
    y_pred = best_estimator.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"Best Parameters for {model_name}: {best_params}")
    print(f"Accuracy: {acc:.4f}")
    
    if acc > best_score:
        best_score = acc
        best_model = best_estimator

# Save the best model
with open("spam_model.pkl", "wb") as model_file:
    pickle.dump(best_model, model_file)

print("\n✅ Best Model Trained & Saved Successfully!")
