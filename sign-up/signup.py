from customtkinter import *
from PIL import Image


app = CTk()
app.geometry("600x480")
app.resizable(width=False,height=False)

# images section
side_img_data = Image.open("./assets/frame0/side-img.png")
email_icon_data = Image.open("./assets/frame0/email-icon.png")
password_icon_data = Image.open("./assets/frame0/password-icon.png")
email_entry_img_data = Image.open("./assets/frame0/entry_1.png")

side_img = CTkImage(dark_image=side_img_data,light_image=side_img_data, size=(300,480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
email_entry_img = CTkImage(dark_image=email_entry_img_data,light_image=email_entry_img_data,)

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height= 480, fg_color="#ffffff")
frame.pack_propagate(False)
frame.pack(expand=True, side="right")


CTkLabel(master=frame, text="Welcome!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Create a new account!", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
CTkEntry(master=frame,width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Sign Up", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))



app.mainloop()