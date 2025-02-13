import firebase_admin
from firebase_admin import credentials, auth

# Load Firebase credentials
cred = credentials.Certificate("ai-chatbot-firebase-config.json")
firebase_admin.initialize_app(cred)

print("Firebase initialized successfully!")
