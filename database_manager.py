import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect("spam_classifier.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            label TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Call this once when script is imported
initialize_database()

# Function to save prediction to database
def save_prediction(email_text, label):
    conn = sqlite3.connect("spam_classifier.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO predictions (email, label) VALUES (?, ?)", (email_text, label))
    conn.commit()
    conn.close()

# Function to fetch all predictions
def fetch_all_emails():
    conn = sqlite3.connect("spam_classifier.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, label FROM predictions")
    data = cursor.fetchall()
    conn.close()
    return data
