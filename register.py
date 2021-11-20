from tkinter import *
from tkinter import messagebox
import pymysql

def login_window():
    myw.destroy()
    import loginpage


myw=Tk()

myw.geometry('1350x710+10+10')
myw.title('Registration Form')

bgimage=PhotoImage(file='bg2.png')
bgLabel=Label(myw,image=bgimage)
bgLabel.place(x=0,y=0)

registerFrame=Frame(myw,width=650,height=550)
registerFrame.place(x=630,y=30)

titleLabel=Label(registerFrame,text='Registration Form',font=('arial',22,'bold'),fg='green')
titleLabel.place(x=20,y=5)

firstnameLabel=Label(registerFrame,text='First Name',font=('times new roman',18,'bold'))
firstnameLabel.place(x=20,y=80)
entryfirstname=Entry(registerFrame,font=('times new roman',17))
entryfirstname.place(x=20,y=110)

lastnameLabel=Label(registerFrame,text='Last Name',font=('times new roman',18,'bold'))
lastnameLabel.place(x=370,y=80)
entrylastname=Entry(registerFrame,font=('times new roman',17))
entrylastname.place(x=370,y=110)

regnoLabel=Label(registerFrame,text='Reg no',font=('times new roman',18,'bold'))
regnoLabel.place(x=20,y=200)
entryregno=Entry(registerFrame,font=('times new roman',17))
entryregno.place(x=20,y=230)

emailLabel=Label(registerFrame,text='Email',font=('times new roman',18,'bold'))
emailLabel.place(x=370,y=200)
entryemail=Entry(registerFrame,font=('times new roman',17))
entryemail.place(x=370,y=230)

passwordLabel=Label(registerFrame,text='password',font=('times new roman',18,'bold'))
passwordLabel.place(x=20,y=310)
entrypassword=Entry(registerFrame,font=('times new roman',17))
entrypassword.place(x=20,y=340)

password2Label=Label(registerFrame,text='Confirm Password',font=('times new roman',18,'bold'))
password2Label.place(x=370,y=310)
entrypassword2=Entry(registerFrame,font=('times new roman',17))
entrypassword2.place(x=370,y=340)


box=IntVar()
checkButton=Checkbutton(registerFrame,text='I will abide by the terms and conditions',onvalue=1,offvalue=0,variable=box,font=('times new roman',15))
checkButton.place(x=20,y=410)


def registration():
    if entryfirstname.get()=='' or entrylastname.get()=='' or entryregno.get()=='' or entryemail.get()=='' or entrypassword.get()=='' or entrypassword2.get()=='':
      messagebox.showerror('Error','Please fill all the fields')
    elif entrypassword.get()!=entrypassword2.get():
        messagebox.showerror('Error','Password are not same')
    elif box.get()==0:
        messagebox.showerror('Error','Please agree to our terms and Conditions')

    else:
        try:
            call=pymysql.connect(host='localhost',user='root',password='root',database='student')
            cur=call.cursor()
            cur.execute('select * from children where email=%s',entryemail.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror('Error','user already exists')

            else:
                cur.execute('insert into children(f_name,l_name,regno,email,password) values(%s,%s,%s,%s,%s)',(entryfirstname.get(),entrylastname.get(),entryregno.get(),entryemail.get(),entrypassword.get()))
                call.commit()
                call.close()

                messagebox.showinfo('success','Registration successfull')
                myw.destroy()
                import loginpage

        except EXCEPTION as e:
            messagebox.showerror('error',f'Error {e}')

registerimage=PhotoImage(file='button.png')
registerButton=Button(registerFrame,image=registerimage,bd=0,command=registration)
registerButton.place(x=200,y=440)

loginimage=PhotoImage(file='login.png')
loginButton=Button(myw,image=loginimage,bd=0,command=login_window)
loginButton.place(x=130,y=250)



myw.mainloop()