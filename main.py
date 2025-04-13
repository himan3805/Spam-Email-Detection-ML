import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from database_manager import save_prediction  # Make sure this is correct

# Load trained model & vectorizer
with open("spam_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Function to preprocess and predict email
def predict_email():
    email_text = email_input.get("1.0", tk.END).strip()
    
    if not email_text:
        messagebox.showerror("Error", "Please enter an email!")
        return

    try:
        email_tfidf = vectorizer.transform([email_text])
        prediction = model.predict(email_tfidf)[0]
    except Exception as e:
        messagebox.showerror("Prediction Error", f"An error occurred:\n{e}")
        return

    if prediction == 1:
        result_text = "🚨 SPAM Email! 🚨"
        result_label.config(text=result_text, fg="red")
    else:
        result_text = "✅ NOT Spam (Ham) ✅"
        result_label.config(text=result_text, fg="green")

    # Save prediction to database
    save_prediction(email_text, "Spam" if prediction == 1 else "Ham")

# Function to clear the text input
def clear_input():
    email_input.delete("1.0", tk.END)
    result_label.config(text="")

# Setup GUI
root = tk.Tk()
root.title("Spam Email Classifier")
root.geometry("550x420")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter Email Text:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)

email_input = tk.Text(root, height=10, width=60, wrap=tk.WORD)
email_input.pack(pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

predict_button = tk.Button(button_frame, text="Check Spam", command=predict_email, font=("Arial", 12), bg="blue", fg="white")
predict_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_input, font=("Arial", 12), bg="gray", fg="white")
clear_button.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
