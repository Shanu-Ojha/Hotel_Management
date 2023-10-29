from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
from tkinter import messagebox


class report_window():
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1120x480+220+200')
        self.root.resizable(0,0)

        # ========== Title =============
        title=Label(self.root,text='REPORT',font=('Times New Roman',18,'bold')
                    ,bg='black',fg='gold',bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1120,height=40)

        # ========= Logo ===========
        img1=Image.open(r'logo.png')
        img1=img1.resize((100,40),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_img=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        label_img.place(x=4,y=4,width=60,height=30)

        # ========= Image ===========
        img2=Image.open(r'pic10.png')
        img2=img2.resize((1120,440),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_img=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        label_img.place(x=0,y=40,width=1120,height=440)

        # ================= Buttons ======================
        butadd=Button(self.root,text='SUGGESTION',font=('arial',15,'bold'),
                      bg='black',fg='gold',width=20)
        butadd.place(x=200,y=100)

        butupdate=Button(self.root,text='COMPLAINT',font=('arial',15,'bold'),
                         bg='black',fg='gold',width=20)
        butupdate.place(x=700,y=100)

        global text
        # =============== Suggestion ==================

        label_frame1=LabelFrame(self.root,bd=2,relief=RIDGE,text='Suggestion',
                                font=('Times New Roman',20,'bold'),padx=2,bg='#59AB98')
        label_frame1.place(x=60,y=160,width=500,height=300)

        text=Text(label_frame1,font=('Comic Sans MS',15),bd=3,width=40,height=7,
                      padx=2,bg='#59AB98')
        text.grid(row=0,column=0)

        butsubmit=Button(label_frame1,text='Submit',font=('arial',15,'bold'),
                         bg='black',fg='gold',width=10,command=self.submit1)
        butsubmit.grid(row=1,column=0,padx=3,pady=6)

        # =============== Complaint ==================

        label_frame1=LabelFrame(self.root,bd=2,relief=RIDGE,text='Complaint',
                                font=('Times New Roman',20,'bold'),padx=2,bg='#59AB98')
        label_frame1.place(x=580,y=160,width=500,height=300)

        text=Text(label_frame1,font=('Comic Sans MS',15),bd=3,width=40,height=7,
                      padx=2,bg='#59AB98')
        text.grid(row=0,column=0)

        butsubmit=Button(label_frame1,text='Submit',font=('arial',15,'bold'),
                         bg='black',fg='gold',width=10,command=self.submit2)
        butsubmit.grid(row=1,column=0,padx=3,pady=6)

    def submit1(self):
        text.delete(1.0,END)
        messagebox.showinfo('Suggestion',"Thank you for your kind suggestion.",
                            parent=self.root)

    def submit2(self):
        text.delete(1.0,END)
        messagebox.showinfo('Complaint',"Sorry for inconvenience we'll work upon it.",
                            parent=self.root)
        


if __name__ == "__main__" :
    root=Tk()
    obj=report_window(root)
    root.mainloop()
