import customtkinter as ctk
import re
from tkinter import messagebox

# App appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Strength checking function
def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Minimum 8 characters required.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("Add an uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Add a lowercase letter.")

    if re.search(r'\d', password):
        strength += 1
    else:
        remarks.append("Add a number.")

    if re.search(r'[@$!%*#?&]', password):
        strength += 1
    else:
        remarks.append("Add a special character.")

    return strength, remarks

# Evaluation function
def evaluate_password():
    password = entry.get()
    strength, remarks = check_password_strength(password)

    if strength == 5:
        result_label.configure(text="Strong Password 💪", text_color="green")
        progress_bar.set(1.0)
        progress_bar.configure(progress_color="green")
    elif strength >= 3:
        result_label.configure(text="Moderate Password 🤔", text_color="orange")
        progress_bar.set(0.6)
        progress_bar.configure(progress_color="orange")
    else:
        result_label.configure(text="Weak Password ⚠️", text_color="red")
        progress_bar.set(0.3)
        progress_bar.configure(progress_color="red")

    if strength < 5:
        messagebox.showinfo("Suggestions", "\n".join(remarks))

# Toggle password visibility
def toggle_password():
    if entry.cget("show") == "*":
        entry.configure(show="")
        toggle_btn.configure(text="Hide")
    else:
        entry.configure(show="*")
        toggle_btn.configure(text="Show")

# GUI Setup
app = ctk.CTk()
app.title("🔐 Password Complexity Checker")
app.geometry("450x300")

title = ctk.CTkLabel(app, text="Enter your password", font=ctk.CTkFont(size=16, weight="bold"))
title.pack(pady=10)

entry_frame = ctk.CTkFrame(app, fg_color="transparent")
entry_frame.pack()

entry = ctk.CTkEntry(entry_frame, placeholder_text="Password", width=250, show="*")
entry.pack(side="left", padx=(0, 5))

toggle_btn = ctk.CTkButton(entry_frame, text="Show", width=60, command=toggle_password)
toggle_btn.pack(side="left")

check_btn = ctk.CTkButton(app, text="Check Strength", command=evaluate_password)
check_btn.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
result_label.pack(pady=5)

progress_bar = ctk.CTkProgressBar(app, width=300)
progress_bar.set(0)
progress_bar.pack(pady=5)

app.mainloop()
