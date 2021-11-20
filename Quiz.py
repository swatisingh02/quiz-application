import tkinter
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import json
from tkinter import ttk
import time

# root = Tk()
# root.geometry("800x500")
# root.title("Quiz")
# with open('quiz.json') as f:
#     obj = json.load(f)
# q = (obj['ques'])
# options = (obj['options'])
# a = (obj['ans'])

class Quiz_Window(Toplevel):
    def __init__(self,master=None):
        super().__init__(master = master)
        self.title("Quiz")
        with open('quiz.json') as f:
            obj = json.load(f)
        self.q = (obj['ques'])
        self.options = (obj['options'])
        self.a = (obj['ans'])
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.my_progress['value'] = 10
        self.correct = 0
        self.withdraw()

    
    def question(self, qn):
        global t
        t = Label(root, text="Quiz on HTML/CSS", width=50, bg="blue", fg="white", font=("times", 20, "bold"), justify=CENTER)
        t.place(x=0, y=2)
        
        qn = Label(root, text=self.q[qn], bg="#ffffff", width=60, font=("times", 16, "bold"), anchor="w", wraplength=600)
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            global btn
            btn = Radiobutton(root, text=" ", bg="#ffffff", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = self.q[qn]
        for op in self.options[qn]:
              self.opts[val]['text'] = op
              val += 1

    def buttons(self):
        nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.place(x=380,y=380)
        self.my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length = 300, mode="determinate")
        self.my_progress.place(x = 210, y = 485)

    def checkans(self, qn):
        if self.opt_selected.get() == self.a[qn]:
            return True
        
    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        self.my_progress['value'] += 10
        if self.qn == len(self.q):
            self.display_result()
        else:
            self.display_options(self.qn)       
        

    def display_result(self):
        lbl_resut_img= Label(
        root,
        bg = '#ffffff',
        border=0
        )
        lbl_resut_img.pack(pady = (50, 30))
        lbl_result_text = Label(
            root, 
            font = ("Consolas", 20),
            bg = '#ffffff'
        )
        lbl_result_text.pack()
        if self.correct >= 8:
            img = ImageTk.PhotoImage(Image.open(r'C:\Users\swati\Desktop\Quiz_Application_INT213\images\great.jpg'))
            lbl_resut_img.configure(image=img)
            lbl_resut_img.image = img
            lbl_result_text.configure(text="You Were Excellent !!") 

        elif (self.correct >= 5 and self.correct < 8):
            img = ImageTk.PhotoImage(Image.open(r'C:\Users\swati\Desktop\Quiz_Application_INT213\images\ok.png'))
            lbl_resut_img.configure(image=img)
            lbl_resut_img.image = img
            lbl_result_text.configure(text="You Can Do Better !!")
        else:
            img = ImageTk.PhotoImage(Image.open(r'C:\Users\swati\Desktop\Quiz_Application_INT213\images\sad2.png'))
            lbl_resut_img.configure(image=img)
            lbl_resut_img.image = img
            lbl_result_text.configure(text="Better Luck Next Time!!")

        score = int(self.correct / len(self.q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(self.q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))



root = tkinter.Tk()
root.title("Quiz Application")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0, 0)
# *setting an icon for the window
root.iconbitmap(
    r'C:\Users\swati\Desktop\Quiz_Application_INT213\images\ideas.ico')

f = ("Arial",24)

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("20")
second.set("00")

hour_tf= Entry(root, width=3, font=("Arial",24),textvariable=hour)
hour_tf.place(x=480,y=65)
mins_tf= Entry(root, width=3, font=("Arial",24),textvariable=minute)
mins_tf.place(x=530,y=65)
sec_tf = Entry(root, width=3, font=("Arial",24),textvariable=second)
sec_tf.place(x=580,y=65)


def startCountdown():
	try:
		userinput = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		mb.showwarning('', 'Invalid Input!')
	while userinput >-1:
		mins,secs = divmod(userinput,60) 

		hours=0
		if mins >60:
			hours, mins = divmod(mins, 60)
	
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

	
		root.update()
		time.sleep(1)

	
		if (userinput == 0):
			mb.showinfo("", "Time's Up")
		userinput -= 1

# * Quiz Image and text:
img1 = ImageTk.PhotoImage(Image.open(r'C:\Users\swati\Desktop\Quiz_Application_INT213\images\quiz_img1.jpg'))
lbl_img = Label(
    root,
    image=img1,
    bg='#ffffff')

lbl_img.pack(pady=(45, 0))

lbl_text = Label(
    root,
    text="QuiZ Me UP!",
    font=("Comic sans MS", 24, "bold"),
    bg='#ffffff')

lbl_text.pack(pady=(0, 50))




# * After start is pressed, quiz questions display function:

def OnStartClick():
    lbl_img.destroy()
    lbl_text.destroy()
    lbl_Instruction.destroy()
    lbl_Rules.destroy()
    btnStart.destroy()
    

def changeOnHover(button, colorOnHover, colorOnLeave):

    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


img2 = ImageTk.PhotoImage(Image.open(r'C:\Users\swati\Desktop\Quiz_Application_INT213\images\start_btn.png'))
btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
)
btnStart.bind("<Button>",
         lambda e: [ OnStartClick(),Quiz_Window(root), startCountdown()])
changeOnHover(btnStart, "black", "white")
btnStart.pack()


# * Quiz Instructions label:
lbl_Instruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are Ready",
    bg='#ffffff',
    font=("Comic sans MS", 14),
    justify=CENTER
)

lbl_Instruction.pack(pady=(10, 90))


# * Quiz Rules label:
lbl_Rules = Label(
    root,
    text="This quiz contains 10 questions.\nYou wil get 2 minutes to solve each question.\nOnce you select an option, click next to move on to the next question.\nGood Luck !",
    width=100,
    font=("Times", 14),
    bg="#000000",
    fg="#FACA2F"
)

lbl_Rules.pack()
root.mainloop()
