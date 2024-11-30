"""--------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇 --------------------

Description:
 A GUI application that asks the user questions about their project and determines which Agile methodology is best for them


Usage:
 python agileselector.py

Parameters:
 None

---------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇--------------------"""
from tkinter import *
from tkinter import ttk
import inspect, os, ctypes

# Initialize global variables
current_question = 0
answers = []
user_answer1 = None
user_answer2 = None
user_answer3 = None

# Determine the path and parent directory of this script
script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
script_dir = os.path.dirname(script_path)

questions = ["Does project success depend on frequent feedback?",
             "What is the delivery strategy?",
             "Will the project invest in enhanced quality?"] 

def load_question():
    if current_question == 0:
        lbl_question.config(text=questions[0]) # Project feedback question
        btn_answer1.config(text="Yes")
        btn_answer2.config(text="No")
    elif current_question == 1:
        lbl_question.config(text=questions[1]) # delivery strategy question
        btn_answer1.config(text="Phased Deployment")
        btn_answer2.config(text="Big Bang Deployment")
    elif current_question == 2:
        lbl_question.config(text=questions[2]) # Enhanced quality question
        btn_answer1.config(text="Yes")
        btn_answer2.config(text="No")

def option1_clicked():  
    answers.append(btn_answer1.cget("text"))
    handle_answers()

def option2_clicked():
    answers.append(btn_answer2.cget("text"))
    handle_answers()
    
def handle_answers():
    global current_question, user_answer1, user_answer2, user_answer3
    if len(answers) == 1:
        if answers[0] == "Yes":
            user_answer1 = 0 # Yes
        else:
            user_answer1 = 1 # No
    if len(answers) == 2:
        if answers[1] == "Phased Deployment":
            user_answer2 = 0 # Phased Deployment
        else: 
            user_answer2 = 1 # Big Bang Deployment
    if len(answers) == 3:
        if answers[2] == "Yes":
            user_answer3 = 0 # Yes
        else:
            user_answer3 = 1 # No
    current_question += 1
    load_question()
    display_result()
  

def display_result():
    global current_question, answers, user_answer1, user_answer2, user_answer3
    result = None
    if user_answer1 == 1:
        if user_answer2 == 0:
            result = "Incremental"
        elif user_answer2 == 1:
            if user_answer3 == 0:
                result = "Incremental"
            elif user_answer3 == 1:
                result = "Waterfall"
    elif user_answer1 == 0:
        if user_answer2 == 0:
            result = "Agile"
        elif user_answer2 == 1:
            if user_answer3 == 0:
                result = "Agile"
            elif user_answer3 == 1:
                result = "Iterative"

    if result:
        lbl_title.config(text=f"The Best Agile Methodology For Your Project is:\n\n\t {result}")
        current_question = 0
        answers.clear()
        user_answer1, user_answer2, user_answer3 = None, None, None        
        load_question()
  
# Create the main window
root = Tk()
root.title("Agile Methodology Selector")
root.minsize(600, 600)
root.maxsize(600, 600)
 # Set the icon 
root.iconbitmap(os.path.join(script_dir, "agile_icon.ico"))
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Agile.agileselector")
root.withdraw()
root.iconbitmap(os.path.join(script_dir, "agile_icon.ico"))
root.deiconify()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=60)  
root.rowconfigure(1, weight=20)
root.rowconfigure(2, weight=20)

# Top frame for title
top_frm = ttk.Frame(root)
top_frm.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")
top_frm.columnconfigure(0, weight=1)
top_frm.rowconfigure(0, weight=1)

# top subframe for description
sub_frm = ttk.Frame(root)    
sub_frm.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="new")
sub_frm.columnconfigure(0, weight=1)
sub_frm.rowconfigure(0, weight=1)

# middle frame for description
middle_frm = ttk.Frame(root)    
middle_frm.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="new")
middle_frm.columnconfigure(0, weight=1)
middle_frm.rowconfigure(0, weight=1)

# bottom left frame for button 1
bottom_left_frm = ttk.Frame(root)
bottom_left_frm.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
bottom_left_frm.columnconfigure(0, weight=1)
bottom_left_frm.rowconfigure(2, weight=1)

# bottom right frame for button 2
bottom_right_frm = ttk.Frame(root)
bottom_right_frm.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
bottom_right_frm.columnconfigure(1, weight=1)
bottom_right_frm.rowconfigure(2, weight=1)

# add widget to top frame
lbl_title = ttk.Label(top_frm, text="Agile Methodology Selector", font=("Arial", 20), anchor="center", wraplength=500)
lbl_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")  

# Add a second label for the smaller text
lbl_subtitle = ttk.Label(sub_frm, text="Please answer these few questions and we will help you determine what Agile Methodology is best for you", font=("Arial", 12), anchor="center", wraplength=500)
lbl_subtitle.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="new")

# add widgets to middle frame
lbl_question = ttk.Label(middle_frm, text=questions[0], font=("Arial", 12), anchor="center")
lbl_question.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="new")

# add button to bottom left frame
btn_answer1 = ttk.Button(bottom_left_frm, text="Yes", command=option1_clicked ,width=10)
btn_answer1.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

# add button to bottom right frame
btn_answer2 = ttk.Button(bottom_right_frm, text="No", command=option2_clicked, width=10)
btn_answer2.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

# Run the application
root.mainloop()