from tkinter import *
from tkinter import messagebox
#from Hotel import HotelManagementSystem


class Login:    
    def __init__(self,root):
        self.root=root
        self.root.title('Login System')
        self.root.geometry('1000x600+180+50')
        self.root.resizable(0,0)
        #** BG Image **#
        self.bg=PhotoImage(file=r"log.png")
        self.bg_image=Label(self.root,image=self.bg)
        self.bg_image.place(x=0,y=0,relwidth=1,relheight=1)
                
        #*** Login Frame ***#
        Frame_login=Frame(self.root,bg='#002c59')
        Frame_login.place(x=450,y=20,height=320,width=500)

        title=Label(Frame_login,text='LOGIN HERE',font=('Showcard Gothic',43),fg='#1e8eff',bg='#002c59')
        title.place(x=85,y=20)

        title_user=Label(Frame_login,text='Username',font=('Freestyle Script',30,'bold'),fg='white',bg='#002c59')
        title_user.place(x=50,y=90)
        self.txt_user=Entry(Frame_login,font=('Comic Sans MS',14),bg='lightgray')
        self.txt_user.place(x=50,y=130,width=350,height=30)

        title_pass=Label(Frame_login,text='Password',font=('Freestyle Script',30,'bold'),fg='white',bg='#002c59')
        title_pass.place(x=50,y=170)
        self.txt_pass=Entry(Frame_login,show='*',font=('Comic Sans MS',14),bg='lightgray')
        self.txt_pass.place(x=50,y=210,width=350,height=30)
        
        login_button=Button(self.root,text='Login',command=self.Login_function,bg='#0051a3',fg='white',font=('MV Boli',20,'bold'))
        login_button.place(x=500,y=310,width=180,height=40)

        exit_button=Button(self.root,text='Exit',command=self.exit_function,bg='#0051a3',fg='white',font=('MV Boli',20,'bold'))
        exit_button.place(x=700,y=310,width=180,height=40)

    def Login_function(self):
        if self.txt_pass.get()==''or self.txt_user.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)

        elif self.txt_pass.get()!='password'or self.txt_user.get()!='13280@apsspmlko.com':
            messagebox.showerror('Error','Invalid Username or Password',parent=self.root)
        else:
            message=messagebox.askyesno('Welcome','Do you want to continue.',parent=self.root)
            if message>0:
                self.new_window=Toplevel(self.root)
                self.app=HotelManagementSystem(self.new_window)
            else:
                if not message:
                    return

    def exit_function(self):
        self.root.destroy()
        
                

root=Tk()
obj=Login(root)
root.mainloop()
