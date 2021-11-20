from tkinter import*
from tkinter import messagebox
import pymysql


def register_window():
    nw.destroy()
    import register


def loginin():
    if moreentry.get()==''or passentry.get()=='':
        messagebox.showerror('error','Please fill all the fields')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root',database='student')
            call=con.cursor()
            call.execute('select * from children where email=%s and password=%s',(moreentry.get(),passentry.get()))
            row=call.fetchone()

            if row==None:
                messagebox.showerror('error','Invalid credentials')
            else:
                nw.destroy()
                import Quiz
            con.close()
        except EXCEPTION as e:
            messagebox.showerror('error',f'Error is due to {e}')


nw=Tk()

nw.geometry('900x600')
nw.title('Login Page')

bgloginimage=PhotoImage(file='lgbg.png')
bgloginLabel=Label(nw,image=bgloginimage)
bgloginLabel.place(x=0,y=0)


frame=Frame(nw,width=560,height=320,bg='white')
frame.place(x=100,y=140)

userimage=PhotoImage(file='user.png')
userimageLabel=Label(frame,image=userimage,bg='white')
userimageLabel.place(x=10,y=50)

morelabel=Label(frame,text='Email',font=('arial',18,'bold'),bg='white')
morelabel.place(x=220,y=32)
moreentry=Entry(frame,font=('arial',18),bg='white')
moreentry.place(x=220,y=70)

passlabel=Label(frame,text='Password',font=('arial',18,'bold'),bg='white')
passlabel.place(x=220,y=120)
passentry=Entry(frame,font=('arial',18),bg='white',show='*')
passentry.place(x=220,y=160)



regButton=Button(frame,text='Register new account?',font=('arial',10),bd=0,bg='white',activebackground='white',command=register_window)
regButton.place(x=220,y=200)

loginButton=Button(frame,text='Login',font=('arial',16,'bold'),fg='white',bg='gray',command=loginin)
loginButton.place(x=450,y=240)




nw.mainloop()