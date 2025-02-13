from dotenv import load_dotenv
import sys
import os
import json
import subprocess
import requests
from customtkinter import *
from firebase_admin import auth, credentials, initialize_app
from PIL import Image
import firebase_admin
import re
from tkinter import messagebox

load_dotenv()
FIREBASE_API_KEY = os.environ["Firebase_Api_Key"]

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('../config/ai-chatbot-firebase-config.json')
    initialize_app(cred)

def open_signup_page():
    """ Opens the signup.py file when the user clicks 'Sign Up Now'. """
    messagebox.showinfo(title="Redirect", message="Redirecting to Signup Page...")
    subprocess.Popen([sys.executable, "../sign-up/signup.py"])  # Opens signup.py in a new window
    app.destroy()

def open_dashboard():
    messagebox.showinfo(title="Welcome", message="Redirecting to Dashboard...")
    # Add code to launch chatbot or main application UI

def login_user():
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showerror(title="Error", message="Please enter email and password!")
        return

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"

    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, data=payload, headers=headers)
        data = response.json()

        if "idToken" in data:
            messagebox.showinfo(title="Success", message="Login Successful!")
            app.quit()  # Close login window
            open_dashboard()  # Redirect user to dashboard
        else:
            error_message = data.get("error", {}).get("message", "Login Failed!")
            messagebox.showerror(title="Login Error", message=error_message)

    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))

    finally:
        # Clear fields
        email_entry.delete(0, END)
        password_entry.delete(0, END)

def validate_email(email):
    # Simple email format validation using regular expressions
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    return False

app = CTk()
app.geometry("600x480")
app.resizable(False,False)

side_img_data = Image.open("../assets/side-img.png")
email_icon_data = Image.open("../assets/email-icon.png")
password_icon_data = Image.open("../assets/password-icon.png")


side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))


CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(False)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left",
         font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left",
         font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
         image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
email_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
                       text_color="#000000")
email_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
         image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
                          text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

# Buttons
CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225, command=login_user).pack(anchor="w", pady=(40, 0), padx=(25, 0))


# Not a user? Sign Up Now section
not_user_label = CTkLabel(master=frame, text="Not a user?", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
                 compound="left")
not_user_label.pack(anchor="w", padx=(25, 0),pady=(30,0))

signup_button = CTkButton(master=frame, text="Sign Up Now", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225,  command=open_signup_page)
signup_button.pack(anchor="w", padx=(25, 0))

app.mainloop()