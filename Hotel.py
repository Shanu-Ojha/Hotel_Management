from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from Customer import Cust_window
from Room import room_window
from Restaurent import restaurent
from Report import report_window

class HotelManagementSystem():
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1350x690+0+0')
        self.root.resizable(0,0)

        # ========= 1st Image ===========
        img1=Image.open(r'pic1.png')
        img1=img1.resize((1350,120),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_img=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        label_img.place(x=0,y=0,width=1350,height=120)

        # ========= Logo ===========
        img2=Image.open(r'logo.png')
        img2=img2.resize((200,120),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_img=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        label_img.place(x=0,y=0,width=205,height=120)

        # ========== Title =============
        title=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',font=('Times New Roman',35,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        title.place(x=0,y=120,width=1350,height=45)

        # ============== Date ===========
        def date():
            string=strftime('%d %h %Y')
            lbl.config(text=string)

        lbl =Label(self.root,font=('ds-digital',20,'bold'),bg='black',fg='gold')
        lbl.place(x=40,y=127)
        date()

        # ============== Time ===========
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl =Label(self.root,font=('ds-digital',20,'bold'),bg='black',fg='gold')
        lbl.place(x=1160,y=127)
        time()

        # =========== Main Frame =======
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=165,width=1350,height=525)

        # ============ Menu ============
        title_menu=Label(main_frame,text='MENU',font=('Times New Roman',20,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        title_menu.place(x=0,y=0,width=205)

        # =========== Button Frame =======
        button_frame=Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=205,height=197)

        cust_button=Button(button_frame,text='CUSTOMER',command=self.cust_details,font=('Times New Roman',15,'bold'),bg='black',fg='gold',bd=0,width=16,cursor='hand2')
        cust_button.grid(row=0,column=0,pady=1)

        room_button=Button(button_frame,text='ROOM',command=self.room_window,font=('Times New Roman',15,'bold'),bg='black',fg='gold',bd=0,width=16,cursor='hand2')
        room_button.grid(row=1,column=0,pady=1)

        detail_button=Button(button_frame,text='RESTAURENT',command=self.Restaurent,font=('Times New Roman',15,'bold'),bg='black',fg='gold',bd=0,width=16,cursor='hand2')
        detail_button.grid(row=2,column=0,pady=1)

        report_button=Button(button_frame,text='REPORT',command=self.report,font=('Times New Roman',15,'bold'),bg='black',fg='gold',bd=0,width=16,cursor='hand2')
        report_button.grid(row=3,column=0,pady=1)

        exit_button=Button(button_frame,text='LOGOUT',command=self.close_window,font=('Times New Roman',15,'bold'),bg='black',fg='gold',bd=0,width=16,cursor='hand2')
        exit_button.grid(row=4,column=0,pady=1)

        # ========== Right side image ============
        img3=Image.open(r'pic2.png')
        img3=img3.resize((1145,570),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label_img=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        label_img.place(x=205,y=0,width=1139,height=520)

        # ========== Down image ==================
        img4=Image.open(r'pic3.png')
        img4=img4.resize((205,200),Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        label_img=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        label_img.place(x=0,y=230,width=205,height=150)

        img5=Image.open(r'pic4.png')
        img5=img5.resize((205,138),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        label_img=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        label_img.place(x=0,y=380,width=205,height=138)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_window(self.new_window)

    def room_window(self):
        self.new_window1=Toplevel(self.root)
        self.app=room_window(self.new_window1)

    def Restaurent(self):
        self.new_window2=Toplevel(self.root)
        self.app=restaurent(self.new_window2)

    def report(self):
        self.new_window3=Toplevel(self.root)
        self.app=report_window(self.new_window3)

    def close_window(self):
        message=messagebox.askyesno('Alert','Are you sure you want to logout.',parent=self.root)
        if message>0:
            self.root.destroy()
        else:
            if not message:
                return
        


if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
