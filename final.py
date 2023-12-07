#Name: Adam Venecia
#Date: December 7, 2023
#ITSE-1402-V01
#Purpose: Converts Text into Binary and Binary into Text
    
#Use Case Definition:
#1. User is first greeted with three buttons and a form. 
    #The three buttons are the 'Toggle Mode' button, a 'Convert Text to Binary' button, and a 'Copy Result' button.
#2. Above the form is where the user is prompted to "Enter Text:".
#3. Once the user has entered their text, there can click on the "Convert to Text to Binary" Button to get their result.
#4. Once the conversion is complete, the result will be displayed to the right of the application.
#5. The 'Copy Result' button will copy the result on the user's clipboard.
#convert binary to text, errors, exit.
import tkinter as tk
from tkinter import messagebox

def convert_text():
    if conversion_mode.get() == "Text to Binary":
        text = input_entry.get()
        if not text.isalpha(): #Data Validation
            result_label.config(text="Error: Please enter valid text")
            return
        binary_result = ' '.join(format(ord(char), '08b') for char in text)
        #Main Function
        #1 for char in text: this part of the code is a loop that iterates over each character in the variable 'text'.
        #2 ord(char): It takes a character as an input and returns its unicode then turning it into an integer value.
        #3 format(ord(char), '09b'): Converts the Unicode of each character into binary as a string. 
            #'08b' specifices that the string should be 8 digits, '08' and binary, 'b'.
        #4 ' '.join(...): Joins the binary strings into a single string, seperated by spaces.
        result_label.config(text="Binary: " + binary_result)
    elif conversion_mode.get() == "Binary to Text":
        binary_text = input_entry.get()
        try: #start of Try
            binary_values = binary_text.split()
            text_result = ''.join(chr(int(binary, 2)) for binary in binary_values)
            result_label.config(text="Text: " + text_result)
        except ValueError: #start of except
            result_label.config(text="Error: Please enter valid binary") #Data Validation

def toggle_conversion_mode():
    current_mode = conversion_mode.get()
    new_mode = "Binary to Text" if current_mode == "Text to Binary" else "Text to Binary"
    conversion_mode.set(new_mode)
    convert_button.config(text=f"Convert {new_mode}")
    result_label.config(text="")
    input_label.config(text="Enter binary" if new_mode == "Binary to Text" else "Enter text")

def copy_to_clipboard():
    result_text = result_label.cget("text")
    if result_text.startswith("Error"):
        messagebox.showerror("Error", result_text)
    else:
        root.clipboard_clear()
        root.clipboard_append(result_text.split(": ")[1])
        root.update()

# Create the main window
root = tk.Tk()
root.title("Text/Binary Converter")

# Set warm colors with a modern font
bg_color = "#F4DFC8"
fg_color = "#3d0c02"
font_family = "Segoe UI"

# Set root background color
root.configure(bg=bg_color)

# Create and place widgets for input form
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(side=tk.LEFT, padx=10, pady=10)

toggle_button = tk.Button(input_frame, text="Toggle Mode", command=toggle_conversion_mode, bg=fg_color, fg="white", font=(font_family, 12))
toggle_button.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter text:", bg=bg_color, fg=fg_color, font=(font_family, 12))
input_label.pack(pady=10)

input_entry = tk.Entry(input_frame, width=30, bg=fg_color, fg="white", font=(font_family, 12))
input_entry.pack(pady=10)

convert_button = tk.Button(input_frame, text="Convert Text to Binary", command=convert_text, bg=fg_color, fg="white", font=(font_family, 12))
convert_button.pack(pady=10)

# Create and place widgets for result form
result_frame = tk.Frame(root, bg=bg_color)
result_frame.pack(side=tk.RIGHT, padx=10, pady=10)

result_label = tk.Label(result_frame, text="Binary: ", wraplength=200, bg=bg_color, fg=fg_color, font=(font_family, 12))  # Adjust wraplength as needed
result_label.pack(pady=10)

copy_button = tk.Button(result_frame, text="Copy Result", command=copy_to_clipboard, bg=fg_color, fg="white", font=(font_family, 12))
copy_button.pack(pady=10)

# Variable to track conversion mode
conversion_mode = tk.StringVar()
conversion_mode.set("Text to Binary")

# Run the Tkinter event loop
root.mainloop()
