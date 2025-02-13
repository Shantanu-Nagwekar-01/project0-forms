import re
import subprocess
import sys
from customtkinter import *
from tkinter import messagebox
from PIL import Image
import firebase_admin
from firebase_admin import auth, credentials

cred = credentials.Certificate("../config/ai-chatbot-firebase-config.json")
firebase_admin.initialize_app(cred)


def is_valid_email(email):
    """Check if email format is valid"""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)
def open_login_page():
    """Close the signup window and open the login page"""
    messagebox.showinfo(title="Redirect", message="Redirecting to Login Page...")
    subprocess.Popen([sys.executable, "../Login/login_page.py"])  # Opens login_page.py in a new window
    app.destroy()  # Closes the signup window

def signup():
    email  = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showwarning("Warning", "⚠️ Please fill in all fields!")
        return
    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "⚠️ Please enter a valid email address!")
        return
    try:
        user = auth.create_user(email = email,password = password)
        messagebox.showinfo("Success", "✅ Account Created Successfully!")
        print("🎉 User created successfully: ",user.uid)
        # Clear fields
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        # Redirect to login page
        open_login_page()

    except Exception as e:
        messagebox.showerror("Error", f"⚠️ {str(e)}")
        print(f"Error: {e}")

app = CTk()
app.geometry("600x480")
app.resizable(width=False,height=False)

# images section
side_img_data = Image.open("../assets/side-img.png")
email_icon_data = Image.open("../assets/email-icon.png")
password_icon_data = Image.open("../assets//password-icon.png")


side_img = CTkImage(dark_image=side_img_data,light_image=side_img_data, size=(300,480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height= 480, fg_color="#ffffff")
frame.pack_propagate(False)
frame.pack(expand=True, side="right")


CTkLabel(master=frame, text="Welcome!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Create a new account!", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
email_entry = CTkEntry(master=frame,width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
                       text_color="#000000")
email_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
                          text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Sign Up", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225, command=signup).pack(anchor="w", pady=(40, 0), padx=(25, 0))


app.mainloop()