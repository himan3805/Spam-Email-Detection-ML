import pickle

# Create a sample email mapping dictionary (modify as needed)
spam_mapping = {"example@example.com": "spam"}

# Save to a .pkl file
with open("spam_mapping.pkl", "wb") as file:
    pickle.dump(spam_mapping, file)

print("spam_mapping.pkl file created successfully!")
