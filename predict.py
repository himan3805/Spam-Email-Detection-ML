import pickle
import sys

# Load saved model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_spam(email_text):
    """Predict if the given email is spam or not."""
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)[0]
    return "Spam" if prediction == 1 else "Not Spam"

# Test with command-line input
if __name__ == "__main__":
    email = input("Enter email content: ")
    print(f"Prediction: {predict_spam(email)}")
