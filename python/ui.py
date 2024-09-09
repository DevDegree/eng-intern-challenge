import tkinter as tk
from tkinter import ttk

# Import the translate function from translator.py
from translator import translate

def translate_text():
  input_text = input_text_var.get()
  translated_text = translate(input_text)
  output_text_var.set(translated_text)

# Create the main window
root = tk.Tk()
root.title("Braille Translator")

# Set window size
root.geometry("500x300")

# Create a main frame
main_frame = ttk.Frame(root, padding="20")  # Increased padding
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Title and description (bold font for title)
title_label = ttk.Label(main_frame, text="Braille Translator", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

description_label = ttk.Label(main_frame, text="Enter text to translate between English and Braille.", font=("Helvetica", 10))
description_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

# Input field
input_text_var = tk.StringVar()
input_label = ttk.Label(main_frame, text="Enter text:", font=("Helvetica", 12))
input_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
input_entry = ttk.Entry(main_frame, textvariable=input_text_var, width=50, font=("Helvetica", 12))
input_entry.grid(row=2, column=1, padx=5, pady=5)

# Translate button with new color scheme and black text
translate_button = ttk.Button(main_frame, text="Translate", command=translate_text, style="TButton")
translate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Output field
output_text_var = tk.StringVar()
output_label = ttk.Label(main_frame, text="Translated text:", font=("Helvetica", 12))
output_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
output_entry = ttk.Entry(main_frame, textvariable=output_text_var, width=50, font=("Helvetica", 12), state="readonly")
output_entry.grid(row=4, column=1, padx=5, pady=5)

# Style configuration
style = ttk.Style()
style.configure(
    "TButton",
    padding=6,
    relief="flat",
    background="#3F51B5",  # Dark blue button background
    foreground="black",  # Black text color
    font=("Helvetica", 12),
)
style.map("TButton", background=[("active", "#303F9F")])  # Darker blue on hover

# Run the main loop
root.mainloop()