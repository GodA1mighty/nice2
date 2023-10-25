import tkinter
from tkinter import BOTH, StringVar
from PIL import Image, ImageTk

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

#Define Layout
#Define Frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

#Create widgets
name = tkinter.Entry(input_frame, text="Enter your name", width=20)
submit_button = tkinter.Button(input_frame, text="Submit")
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

#create radio buttons for text display
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text="Normal Case", variable=case_style, value='normal', bg=input_color)
upper_button = tkinter.Radiobutton(input_frame, text="Upper Case", variable=case_style, value='upper', bg=input_color)
normal_button.grid(row=1, column=0)
upper_button.grid(row=1, column=1, padx=2, pady=2)

#Add an Image
leaves_img = ImageTk.PhotoImage(Image.open('leaves.png'))
leaves_label = tkinter.label(output_frame, image=leaves_img)
leaves_label.pack()

#Run root window's main loop
root.mainloop()
