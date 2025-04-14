import tkinter as tk
from tkinter import ttk
import winsound  # Importing for sound effects

# Root window
root = tk.Tk()
root.title("Ultimate Mobile Calculator")
root.geometry("370x550")
root.configure(bg="#121212")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.theme_use("clam")

expression = ""

# Function to play a click sound
def play_click_sound():
    winsound.Beep(1500, 100)  # Frequency and duration of the beep

# Functions
def press(num):
    global expression
    play_click_sound()
    expression += str(num)
    input_text.set(expression)

def equal_press():
    global expression
    play_click_sound()
    try:
        total = str(eval(expression))
        input_text.set(total)
        expression = total
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    play_click_sound()
    expression = ""
    input_text.set("")

# Toggle light/dark mode
def toggle_mode():
    if root.cget("bg") == "#121212":  # Dark mode active
        root.configure(bg="#FFFFFF")  # Switch to light mode
        entry.config(bg="#FFFFFF", fg="black", insertbackground='black')
        for button in buttons_list:
            button.config(bg="#f1f1f1", fg="black", activebackground="#e0e0e0")
        title.config(bg="#FFFFFF", fg="black")
        btn_toggle.config(bg="#f1f1f1", fg="black")
    else:
        root.configure(bg="#121212")  # Switch to dark mode
        entry.config(bg="#1f1f2e", fg="lime", insertbackground='white')
        for button in buttons_list:
            button.config(bg="#262626", fg="white", activebackground="#333")
        title.config(bg="#121212", fg="white")
        btn_toggle.config(bg="#262626", fg="white")

# Entry field
input_text = tk.StringVar()
entry = tk.Entry(root, textvariable=input_text, font=("Helvetica", 28), bd=0,
                 bg="#1f1f2e", fg="lime", justify="right", insertbackground='white')
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

# Custom button creator with hover effects, glow, and lighting borders
def create_button(frame, text, command, bg="#262626", fg="white", font=("Helvetica", 18)):
    button = tk.Button(
        frame, text=text, command=command, font=font,
        bg=bg, fg=fg, width=5, height=2, activebackground="#333", bd=0,
        highlightthickness=0, relief="flat", cursor="hand2", pady=10
    )
    
    # Adding hover effects and lighting borders
    button.bind("<Enter>", lambda event, btn=button: btn.config(bg="#2a2a2a", bd=2))
    button.bind("<Leave>", lambda event, btn=button: btn.config(bg=bg, bd=0))
    button.bind("<ButtonPress>", lambda event, btn=button: btn.config(bg="#00adb5", fg="black"))
    button.bind("<ButtonRelease>", lambda event, btn=button: btn.config(bg="#262626", fg="white"))
    
    return button

# Button grid
btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack()

buttons = [
    ["C", "/", "*", "-"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "="],
    ["1", "2", "3", "."],
    ["0"]
]

buttons_list = []

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == "=":
            btn = create_button(btn_frame, char, equal_press, bg="#00adb5")
        elif char == "C":
            btn = create_button(btn_frame, char, clear, bg="#ff5722")
        else:
            btn = create_button(btn_frame, char, lambda ch=char: press(ch))
        btn.grid(row=i, column=j, padx=10, pady=10)
        buttons_list.append(btn)

# Make "0" button stretch across 2 columns
btn_zero = create_button(btn_frame, "0", lambda: press("0"))
btn_zero.grid(row=4, column=0, columnspan=2, sticky="we", padx=10, pady=10)
buttons_list.append(btn_zero)

# Adjust layout
btn_frame.grid_columnconfigure(0, weight=1)
btn_frame.grid_columnconfigure(1, weight=1)
btn_frame.grid_columnconfigure(2, weight=1)
btn_frame.grid_columnconfigure(3, weight=1)

# Title with Toggle Button for Light/Dark Mode
title = tk.Label(root, text="Ultimate Calculator", font=("Helvetica", 24, "bold"),
                 bg="#121212", fg="white", pady=20)
title.pack(fill="x")

# Light/Dark Mode toggle button
btn_toggle = tk.Button(root, text="Toggle Mode", command=toggle_mode, font=("Helvetica", 14),
                       bg="#262626", fg="white", activebackground="#333", bd=0, relief="flat")
btn_toggle.pack(pady=10)

# Launch the app
root.mainloop()
