from customtkinter import *
from PIL import Image
from tkinter import messagebox



questions = [
    {

    "question":"Decode a Base64-encoded string.\nSGVsbG8sIFdvcmxkIQ==\n•Hint: Base64 encoding",
    "choices":["Hello, World!","42 Great Job!","Hi"],
    "answer":"Hello, World!"
    },
    {
    "question":"A multi-layered encoding with Base64, Base32,\nor Base58\nNDIgR3JlYXQgSm9iIQ==\nHint: Base64 -> Base32",
    "choices":["Hello","42 Great Job!","yes"],
    "answer":"42 Great Job!"
    },
    {
    "question":"How is the resolution of the screen shown?",
    "choices":["Dots","Dot per inch","Pixels per inch"],
    "answer":"Pixels per inch",
    },
    {
    "question":"Which of the following is not an image/graphic\nfile format?",
    "choices":["PNG","GI","BMP"],
    "answer":"GI",
    },
    {
    "question":"Which of the following is not the same as the\nother three?",
    "choices":["MAC address","Hardware address","IP address"],
    "answer":"IP address",
    }

            ]


current_question = 0
score = 0
pad_y = 0

def check_answer(selected_choice):
    global current_question,score
    if selected_choice == questions[current_question]["answer"]:
        score +=10
    current_question +=1
    if current_question < len(questions):
        update_question()
    else:
        show_final_score()

def update_question():
    question_label.configure(text=f"Question {current_question+1}")
    question_display.configure(text=questions[current_question]["question"])
    for i,choice in enumerate(questions[current_question]["choices"]):
        option[i].configure(text=choice,command=lambda c=choice: check_answer(c))
        
def show_final_score():
    widget_to_keep = image_label
    for widget in root.winfo_children(): 
        if widget != widget_to_keep: 
            widget.destroy()
    final_window()

def reset_window():
    global user_name
    user_name = name.get()
    if not user_name.strip():
            messagebox.showerror("Team Name","Team Name, Not be blank or empty")
    elif len(user_name) > 10:
        messagebox.showerror("Team Name","Team Name, is too long.\nKeep it short")
    elif len(user_name) < 5:
        messagebox.showerror("Team Name","Team Name, is too Short.\nKeep it short")
    else:
        widget_to_keep = image_label
        for widget in root.winfo_children(): 
            if widget != widget_to_keep: 
                widget.destroy()
        quiz_window()

def final_window():
    image = CTkImage(dark_image=Image.open("end.png"),size=(200,200))
    image_label =CTkLabel(root, image=image,text="",bg_color="#8b5dfe",fg_color="#8b5dfe")
    image_label.place(relx=0.4, rely=0.15,x=10)
    font_1 = CTkFont(family="arial",size=30,weight="bold")
    user_label = CTkLabel(root,text=user_name,font=font_1,bg_color="white",text_color="Black")
    user_label.place(x=10,y=50)
    font_2 = CTkFont(family="arial",size=40,weight="bold")
    final_score = CTkLabel(root,text=f"WOO HOO ! \n\nYou Scored :- {score}/{len(questions)*10}",font=font_2,bg_color="#8b5dfe",text_color="White")
    final_score.place(relx=0.3,rely=0.5,x=35)

    

# root 
root  = CTk()


#root title 
root.title("Quiz Game")
# root.iconbitmap
root.iconbitmap("logo.ico")

#geometry 
width = 1080
height = 720
root.geometry(f"{width}x{height}")
root.maxsize(width,height)
root.minsize(width,height)

#root background 
image = CTkImage(dark_image=Image.open("layout.jpg"),size=(width,height))
image_label =CTkLabel(root, image=image,text="")
image_label.place(relx=0.5, rely=0.5, anchor="center")

#name label 
def initial_window():
    global name
    font = CTkFont(family="arial",size=13,weight="bold")
    user_label = CTkLabel(root,text="Developed By - Eesh Mishra",font=font,bg_color="white",text_color="Black")
    user_label.place(x=5,y=60)
    font = CTkFont(family="arial",size=18,weight="bold")
    name = CTkEntry(root,width=200,height=50,placeholder_text="Enter your team name",fg_color="white",bg_color="#8b5dfe",border_width=2,border_color="white",text_color="black",font=font)
    name.place(relx=0.5,rely=0.4,anchor="center")
    font_1 = CTkFont(family="arial",size=50,weight="bold")
    title = CTkLabel(master=root,text="Quiz Game",font=font_1,bg_color="#8b5dfe",text_color="white")
    title.place(relx=0.25,x=145,y=60)
    start = CTkButton(root,width=400,height=70,text="Start Quiz",font=("arial",30),text_color="white",fg_color="#8b5dfe",bg_color="#8b5dfe",hover_color="#D76C82",corner_radius=40,border_color="white",border_width=5,command=reset_window)
    start.place(relx=0.5,rely=0.5,anchor="center",y=50)

def quiz_window():
    global root,question_display,question_label,pad_y,option
    font = CTkFont(family="arial",size=30,weight="bold")
    user_label = CTkLabel(root,text=user_name,font=font,bg_color="white",text_color="Black")
    user_label.place(x=10,y=50)
    #text 
    font = CTkFont(family="arial",size=30,weight="bold")
    question_label = CTkLabel(master=root,text="",font=font,bg_color="#8b5dfe",text_color="white")
    question_label.place(relx=0.25,x=60,y=60)
    font_2 = CTkFont(family="arial",size=20,weight="bold")
    question_display = CTkLabel(root,text=questions[current_question]["question"],font=font_2,bg_color="#8b5dfe",text_color="White")
    question_display.place(relx=0.25,y=150,x=50)

    option = []
    for j in range(3):
        opt = CTkButton(root,width=400,height=70,text="",font=("arial",30),text_color="white",fg_color="#8b5dfe",bg_color="#8b5dfe",hover_color="#D76C82",corner_radius=40,border_color="white",border_width=5)
        opt.place(relx=0.5,rely=0.5,anchor="center",y=50+pad_y)
        option.append(opt)
        pad_y+=100

    update_question()





initial_window()


root.mainloop()
