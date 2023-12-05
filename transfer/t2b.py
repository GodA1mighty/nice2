import tkinter
from tkinter import BOTH, StringVar, END

#Define window
root = tkinter.Tk()
root.title("Hello GUI World")
root.iconbitmap('wave.ico')
root.geometry("400x400")
root.resizable(0,0)

#define fonts and colors
root_color = "#E8AE68"
input_color = "#FFD275"
output_color = "#DB5A42"
root.config(bg=root_color)

#Define Functions
def submit_name():
    """Say Hello to the user."""
    #Create a Label for the user name based of radio button values
    if case_style.get() == 'text_binary':
        name_label = tkinter.Label(output_frame, text="Hello " + name.get() + " Keep Learning Tkinter!", bg=output_color)
    elif case_style.get() == 'binary_text':
        name_label = tkinter.Label(output_frame, text="Hello " + name.get() + " Keep Learning Tkinter!", bg=output_color)
    #Pack label onto screen
    name_label.pack()

    #Clear the entry field for the user
    name.delete(0, END)


#Define Layout
#Define Frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

#Create widgets
name = tkinter.Entry(input_frame, text="Enter your name", width=20)
submit_button = tkinter.Button(input_frame, text="Submit", command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

#create radio buttons for text display
case_style = StringVar()
case_style.set('text_binary')
text_binary = tkinter.Radiobutton(input_frame, text="Text to Binary", variable=case_style, value='text_binary',
                                    bg=input_color)
binary_text = tkinter.Radiobutton(input_frame, text="Binary to Text", variable=case_style, value='binary_text',
                                   bg=input_color)
text_binary.grid(row=1, column=0)
binary_text.grid(row=1, column=1, padx=2, pady=2)

#Run root window's main loop
root.mainloop()
