#from ast import Str
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import ttk
import random
import time

class restaurent():
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1120x480+220+200')
        self.root.resizable(0,0)
        self.root.config(bg='black')

        # ========== Title =============
        title=Label(self.root,text='RESTAURENT CORNER',font=('Times New Roman',18,'bold')
                    ,bg='black',fg='gold',bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1120,height=40)

        # ========= Logo ===========
        img=Image.open(r'logo.png')
        img=img.resize((100,40),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        label_img=Label(self.root,image=self.photoimg,bd=0,relief=RIDGE)
        label_img.place(x=0,y=4,width=60,height=30)

        # ================= Varibles ==================
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        self.var5=IntVar()
        self.var6=IntVar()
        self.var7=IntVar()
        self.var8=IntVar()
        self.var9=IntVar()
        self.var10=IntVar()
        self.var11=IntVar()
        self.var12=IntVar()
        self.var13=IntVar()
        self.var14=IntVar()
        self.var15=IntVar()
        self.var16=IntVar()
        self.var17=IntVar()
        self.var18=IntVar()
        self.var19=IntVar()
        self.var20=IntVar()
        self.var21=IntVar()
        self.var22=IntVar()
        self.var23=IntVar()
        self.var24=IntVar()
        self.var25=IntVar()
        self.var26=IntVar()
        self.var27=IntVar()
        self.var28=IntVar()

        self.var_entry=StringVar()
                
        self.caesar_salad=StringVar()
        self.chef_salad=StringVar()
        self.coleslaw=StringVar()
        self.pasta_salad=StringVar()
        self.woldorf_salad=StringVar()
        self.sprout_salad=StringVar()
        self.tomato_salad=StringVar()

        self.biryani=StringVar()
        self.butter_chicken=StringVar()
        self.big_thali=StringVar()
        self.chole_bhature=StringVar()
        self.dal_makhani=StringVar()
        self.idli_dosa=StringVar()
        self.litti_choka=StringVar()

        self.pie=StringVar()
        self.pancake=StringVar()
        self.cake=StringVar()
        self.cookies=StringVar()
        self.ice_cream=StringVar()
        self.chocolate=StringVar()
        self.sweets=StringVar()

        self.fruit_juice=StringVar()
        self.hot_chocolate=StringVar()
        self.milk_shake=StringVar()
        self.tea=StringVar()
        self.coffee=StringVar()
        self.black_tea=StringVar()
        self.green_tea=StringVar()

        self.totalcost=StringVar()

        self.caesar_salad.set('0')
        self.chef_salad.set('0')
        self.coleslaw.set('0')
        self.pasta_salad.set('0')
        self.woldorf_salad.set('0')
        self.sprout_salad.set('0')
        self.tomato_salad.set('0')

        self.biryani.set('0')
        self.butter_chicken.set('0')
        self.big_thali.set('0')
        self.chole_bhature.set('0')
        self.dal_makhani.set('0')
        self.idli_dosa.set('0')
        self.litti_choka.set('0')
        
        self.pie.set('0')
        self.pancake.set('0')
        self.cake.set('0')
        self.cookies.set('0')
        self.ice_cream.set('0')
        self.chocolate.set('0')
        self.sweets.set('0')
        
        self.fruit_juice.set('0')
        self.hot_chocolate.set('0')
        self.milk_shake.set('0')
        self.tea.set('0')
        self.coffee.set('0')
        self.black_tea.set('0')
        self.green_tea.set('0')

                

        # =========== label Frame =======
        label_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text='ITEMS',
                                    font=('Times New Roman',20,'bold'),padx=2,bg='black',fg='gold')
        label_frame_left.place(x=3,y=40,width=790,height=435)

        # =========== label Frame Salads =======
        label_frame1=LabelFrame(label_frame_left,bd=2,relief=RIDGE,text='Salads',
                                    font=('Times New Roman',15,'bold'),padx=2,bg='black',fg='Gold')
        label_frame1.place(x=3,y=2,width=190,height=350)

        # =========== label Frame Main Course =======
        label_frame2=LabelFrame(label_frame_left,bd=2,relief=RIDGE,text='Main Course',
                                    font=('Times New Roman',15,'bold'),padx=2,bg='black',fg='Gold')
        label_frame2.place(x=200,y=2,width=210,height=350)

        # =========== label Frame Desserts =======
        label_frame3=LabelFrame(label_frame_left,bd=2,relief=RIDGE,text='Desserts',
                                    font=('Times New Roman',15,'bold'),padx=2,bg='black',fg='Gold')
        label_frame3.place(x=415,y=2,width=180,height=350)

        # =========== label Frame Drinks =======
        label_frame4=LabelFrame(label_frame_left,bd=2,relief=RIDGE,text='Drinks',
                                    font=('Times New Roman',15,'bold'),padx=2,bg='black',fg='Gold')
        label_frame4.place(x=600,y=2,width=180,height=350)

        # =============== Receipt ==================
        label_frame_right=LabelFrame(self.root,bd=2,relief=RIDGE,text='RECEIPT',
                                    font=('Times New Roman',20,'bold'),padx=2,bg='black',fg='gold')
        label_frame_right.place(x=794,y=40,width=325,height=435)

        global textReceipt
        textReceipt=Text(label_frame_right,font=('Bookman Old Style',12),
                         bd=3,width=30,height=17,padx=4,bg='grey')
        textReceipt.grid(row=0,column=0)

        # ================= Buttons And Entry ======================
        button_frame1=Frame(label_frame_left,bd=2,relief=RIDGE,bg='black')
        button_frame1.place(x=3,y=352,width=776,height=47)

        buttotal=Button(button_frame1,text='TOTAL',font=('arial',12,'bold'),
                      bg='black',fg='gold',width=10,command=self.total_amount)
        buttotal.grid(row=0,column=0,padx=3,pady=6)

        ent_search=ttk.Entry(button_frame1,width=15,font=('MV Boli',12,'bold'),
                             state='readonly',textvariable=self.var_entry)
        ent_search.grid(row=0,column=1,padx=2,pady=6)

        butreceipt=Button(button_frame1,text='SHOW RECEIPT',font=('arial',12,'bold'),
                         bg='black',fg='gold',width=15,command=self.receipt)
        butreceipt.grid(row=0,column=2,padx=300,pady=6)

        # ===================== Button on right ========================
        button_frame2=Frame(label_frame_right,bd=2,relief=RIDGE,bg='black')
        button_frame2.place(x=5,y=352,width=309,height=47)

        butreset=Button(button_frame2,text='RESET',font=('arial',12,'bold'),
                      bg='black',fg='gold',width=10,command=self.reset)
        butreset.grid(row=0,column=2,padx=100,pady=6)

        # ======================= img ==============================
        img1=Image.open(r'pic5.png')
        img1=img1.resize((150,80),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_img=Label(label_frame1,image=self.photoimg1,bd=4,relief=RIDGE)
        label_img.place(x=15,y=0,width=150,height=80)

        img2=Image.open(r'pic6.png')
        img2=img2.resize((160,70),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_img=Label(label_frame2,image=self.photoimg2,bd=4,relief=RIDGE)
        label_img.place(x=23,y=106,width=160,height=70)

        img3=Image.open(r'pic7.png')
        img3=img3.resize((120,90),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label_img=Label(label_frame3,image=self.photoimg3,bd=4,relief=RIDGE)
        label_img.place(x=40,y=0,width=120,height=90)

        img4=Image.open(r'pic8.png')
        img4=img4.resize((150,70),Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        label_img=Label(label_frame4,image=self.photoimg4,bd=4,relief=RIDGE)
        label_img.place(x=13,y=250,width=150,height=70)

        # =============== Label , entry and checkbuttom ==================
        #  ************** SALADS ***************
        # Caesar Salad
        salad1=Checkbutton(label_frame1,text='Caesar Salad',font=('arial',14),variable=self.var1,
                            onvalue=1,offvalue=0,bg='black',fg='green',command=self.salad_1)
        salad1.place(x=3,y=80)
        global ent_salad1
        ent_salad1=ttk.Entry(label_frame1,width=2,font=('arial',10,'bold'),
                             textvariable=self.caesar_salad,state=DISABLED)
        ent_salad1.place(x=153,y=85)

        # Chef Salad
        salad2=Checkbutton(label_frame1,text='Chef Salad',font=('arial',14),variable=self.var2,
                           onvalue=1,offvalue=0,bg='black',fg='green',command=self.salad_2)
        salad2.place(x=3,y=115)
        global ent_salad2
        ent_salad2=ttk.Entry(label_frame1,width=2,font=('arial',10,'bold'),
                             textvariable=self.chef_salad,state=DISABLED)
        ent_salad2.place(x=153,y=120)

        # Coleslaw
        salad3=Checkbutton(label_frame1,text='Caleslaw',font=('arial',14),variable=self.var3,
                           onvalue=1,offvalue=0,bg='black',fg='green',command=self.salad_3)
        salad3.place(x=3,y=150)
        global ent_salad3
        ent_salad3=ttk.Entry(label_frame1,width=2,font=('arial',10,'bold'),
                             textvariable=self.coleslaw,state=DISABLED)
        ent_salad3.place(x=153,y=155)

        # Pasta Salad
        salad4=Checkbutton(label_frame1,text='Pasta Salad',font=('arial',14),variable=self.var4,
                           onvalue=1,offvalue=0,bg='black',fg='green',command=self.salad_4)
        salad4.place(x=3,y=185)
        global ent_salad4
        ent_salad4=ttk.Entry(label_frame1,width=2,font=('arial',10,'bold'),
                             textvariable=self.pasta_salad,state=DISABLED)
        ent_salad4.place(x=153,y=190)        

        # Woldorf Salad
        salad5=Checkbutton(label_frame1,text='Woldorf Salad',font=('arial',14),variable=self.var5,
                           onvalue=1,offvalue=0,bg='black',fg='green',command=self.salad_5)
        salad5.place(x=3,y=220)
        global ent_salad5
        ent_salad5=ttk.Entry(label_frame1,width=2,font=('arial',10,'bold'),
                             textvariable=self.woldorf_salad,state=DISABLED)
        ent_salad5.place(x=153,y=225)

        # Sprout Salad
        salad6=Checkbutton(label_frame1,text='Sprout Salad',font=('arial',14),variable=self.var6,
                           onvalue=1,offvalue=0,bg='black',fg='green',command=self.salad_6)
        salad6.place(x=3,y=255)
        global ent_salad6
        ent_salad6=ttk.Entry(label_frame1,width=2,font=('arial',10,'bold'),
                             textvariable=self.sprout_salad,state=DISABLED)
        ent_salad6.place(x=153,y=260)

        # Tomato Salad
        salad7=Checkbutton(label_frame1,text='Tomato Salad',font=('arial',14),variable=self.var7,
                           onvalue=1,offvalue=0,bg='black',fg='green',command=self.salad_7)
        salad7.place(x=3,y=288)
        global ent_salad7
        ent_salad7=ttk.Entry(label_frame1,width=2,font=('arial',10,'bold'),
                             textvariable=self.tomato_salad,state=DISABLED)
        ent_salad7.place(x=153,y=295)

        # ******************** Main Course ******************
        # Biryani
        mainc1=Checkbutton(label_frame2,text='Biryani',font=('arial',14),variable=self.var8,
                           onvalue=1,offvalue=0,bg='black',fg='red',command=self.main_1)
        mainc1.place(x=3,y=2)
        global ent_mainc1
        ent_mainc1=ttk.Entry(label_frame2,width=2,font=('arial',10,'bold'),
                             textvariable=self.biryani,state=DISABLED)
        ent_mainc1.place(x=170,y=7)

        # Butter Chicken
        mainc2=Checkbutton(label_frame2,text='Butter Chicken',font=('arial',14),variable=self.var9,
                           onvalue=1,offvalue=0,bg='black',fg='red',command=self.main_2)
        mainc2.place(x=3,y=37)
        global ent_mainc2
        ent_mainc2=ttk.Entry(label_frame2,width=2,font=('arial',10,'bold'),
                             textvariable=self.butter_chicken,state=DISABLED)
        ent_mainc2.place(x=170,y=42)

        # Big Thali
        mainc3=Checkbutton(label_frame2,text='Big Thali',font=('arial',14),variable=self.var10,
                           onvalue=1,offvalue=0,bg='black',fg='red',command=self.main_3)
        mainc3.place(x=3,y=72)
        global ent_mainc3
        ent_mainc3=ttk.Entry(label_frame2,width=2,font=('arial',10,'bold'),
                             textvariable=self.big_thali,state=DISABLED)
        ent_mainc3.place(x=170,y=77)

        # Chole Bhature
        mainc4=Checkbutton(label_frame2,text='Chole Bhature',font=('arial',14),variable=self.var11,
                           onvalue=1,offvalue=0,bg='black',fg='red',command=self.main_4)
        mainc4.place(x=3,y=178)
        global ent_mainc4
        ent_mainc4=ttk.Entry(label_frame2,width=2,font=('arial',10,'bold'),
                             textvariable=self.chole_bhature,state=DISABLED)
        ent_mainc4.place(x=170,y=182)

        # Dal Makhani
        mainc5=Checkbutton(label_frame2,text='Dal Makhani',font=('arial',14),variable=self.var12,
                           onvalue=1,offvalue=0,bg='black',fg='red',command=self.main_5)
        mainc5.place(x=3,y=212)
        global ent_mainc5
        ent_mainc5=ttk.Entry(label_frame2,width=2,font=('arial',10,'bold'),
                             textvariable=self.dal_makhani,state=DISABLED)
        ent_mainc5.place(x=170,y=217)

        # idli & Dosa
        mainc6=Checkbutton(label_frame2,text='idli & Dosa',font=('arial',14),variable=self.var13,
                           onvalue=1,offvalue=0,bg='black',fg='red',command=self.main_6)
        mainc6.place(x=3,y=247)
        global ent_mainc6
        ent_mainc6=ttk.Entry(label_frame2,width=2,font=('arial',10,'bold'),
                             textvariable=self.idli_dosa,state=DISABLED)
        ent_mainc6.place(x=170,y=252)

        # Litti Choka
        mainc7=Checkbutton(label_frame2,text='Litti Choka',font=('arial',14),variable=self.var14,
                           onvalue=1,offvalue=0,bg='black',fg='red',command=self.main_7)
        mainc7.place(x=3,y=282)
        global ent_mainc7
        ent_mainc7=ttk.Entry(label_frame2,width=2,font=('arial',10,'bold'),
                             textvariable=self.litti_choka,state=DISABLED)
        ent_mainc7.place(x=170,y=287)

        # ****************** Desserts *************************
        # Pie
        dessert1=Checkbutton(label_frame3,text='Pie',font=('arial',14),variable=self.var15,
                             onvalue=1,offvalue=0,bg='black',fg='#ff4f6e',command=self.dessert_1)
        dessert1.place(x=3,y=90)
        global ent_dessert1
        ent_dessert1=ttk.Entry(label_frame3,width=2,font=('arial',10,'bold'),
                               textvariable=self.pie,state=DISABLED)
        ent_dessert1.place(x=140,y=95)

        # Pancake
        dessert2=Checkbutton(label_frame3,text='Pancake',font=('arial',14),variable=self.var16,
                             onvalue=1,offvalue=0,bg='black',fg='#ff4f6e',command=self.dessert_2)
        dessert2.place(x=3,y=125)
        global ent_dessert2
        ent_dessert2=ttk.Entry(label_frame3,width=2,font=('arial',10,'bold'),
                               textvariable=self.pancake,state=DISABLED)
        ent_dessert2.place(x=140,y=130)

        # Cake
        dessert3=Checkbutton(label_frame3,text='Pie',font=('arial',14),variable=self.var17,
                             onvalue=1,offvalue=0,bg='black',fg='#ff4f6e',command=self.dessert_3)
        dessert3.place(x=3,y=160)
        global ent_dessert3
        ent_dessert3=ttk.Entry(label_frame3,width=2,font=('arial',10,'bold'),
                               textvariable=self.cake,state=DISABLED)
        ent_dessert3.place(x=140,y=165)

        # Cookies
        dessert4=Checkbutton(label_frame3,text='Cookies',font=('arial',14),variable=self.var18,
                             onvalue=1,offvalue=0,bg='black',fg='#ff4f6e',command=self.dessert_4)
        dessert4.place(x=3,y=195)
        global ent_dessert4
        ent_dessert4=ttk.Entry(label_frame3,width=2,font=('arial',10,'bold'),
                               textvariable=self.cookies,state=DISABLED)
        ent_dessert4.place(x=140,y=200)

        # Ice cream
        dessert5=Checkbutton(label_frame3,text='Ice cream',font=('arial',14),variable=self.var19,
                             onvalue=1,offvalue=0,bg='black',fg='#ff4f6e',command=self.dessert_5)
        dessert5.place(x=3,y=225)
        global ent_dessert5
        ent_dessert5=ttk.Entry(label_frame3,width=2,font=('arial',10,'bold'),
                               textvariable=self.ice_cream,state=DISABLED)
        ent_dessert5.place(x=140,y=230)

        # Chocalate
        dessert6=Checkbutton(label_frame3,text='Chocalate',font=('arial',14),variable=self.var20,
                             onvalue=1,offvalue=0,bg='black',fg='#ff4f6e',command=self.dessert_6)
        dessert6.place(x=3,y=255)
        global ent_dessert6
        ent_dessert6=ttk.Entry(label_frame3,width=2,font=('arial',10,'bold'),
                               textvariable=self.chocolate,state=DISABLED)
        ent_dessert6.place(x=140,y=260)

        # Sweets
        dessert7=Checkbutton(label_frame3,text='Sweets',font=('arial',14),variable=self.var21,
                             onvalue=1,offvalue=0,bg='black',fg='#ff4f6e',command=self.dessert_7)
        dessert7.place(x=3,y=285)
        global ent_dessert7
        ent_dessert7=ttk.Entry(label_frame3,width=2,font=('arial',10,'bold'),
                               textvariable=self.sweets,state=DISABLED)
        ent_dessert7.place(x=140,y=290)

        #============== Drinks =================
        # Fruit Juice
        drink1=Checkbutton(label_frame4,text='Fruit juice',font=('arial',14),variable=self.var22,
                           onvalue=1,offvalue=0,bg='black',fg='brown',command=self.drink_1)
        drink1.place(x=3,y=2)
        global ent_drink1
        ent_drink1=ttk.Entry(label_frame4,width=2,font=('arial',10,'bold'),
                             textvariable=self.fruit_juice,state=DISABLED)
        ent_drink1.place(x=150,y=7)

        # Hot Chocolate
        drink2=Checkbutton(label_frame4,text='Hot Chocolate',font=('arial',14),variable=self.var23,
                           onvalue=1,offvalue=0,bg='black',fg='brown',command=self.drink_2)
        drink2.place(x=3,y=37)
        global ent_drink2
        ent_drink2=ttk.Entry(label_frame4,width=2,font=('arial',10,'bold'),
                             textvariable=self.hot_chocolate,state=DISABLED)
        ent_drink2.place(x=150,y=42)

        # Milk Shake
        drink3=Checkbutton(label_frame4,text='Milk Shake',font=('arial',14),variable=self.var24,
                           onvalue=1,offvalue=0,bg='black',fg='brown',command=self.drink_3)
        drink3.place(x=3,y=72)
        global ent_drink3
        ent_drink3=ttk.Entry(label_frame4,width=2,font=('arial',10,'bold'),
                             textvariable=self.milk_shake,state=DISABLED)
        ent_drink3.place(x=150,y=77)

        # Tea
        drink4=Checkbutton(label_frame4,text='Tea',font=('arial',14),variable=self.var25,
                           onvalue=1,offvalue=0,bg='black',fg='brown',command=self.drink_4)
        drink4.place(x=3,y=107)
        global ent_drink4
        ent_drink4=ttk.Entry(label_frame4,width=2,font=('arial',10,'bold'),
                             textvariable=self.tea,state=DISABLED)
        ent_drink4.place(x=150,y=112)

        # Coffee
        drink5=Checkbutton(label_frame4,text='Coffee',font=('arial',14),variable=self.var26,
                           onvalue=1,offvalue=0,bg='black',fg='brown',command=self.drink_5)
        drink5.place(x=3,y=142)
        global ent_drink5
        ent_drink5=ttk.Entry(label_frame4,width=2,font=('arial',10,'bold'),
                             textvariable=self.coffee,state=DISABLED)
        ent_drink5.place(x=150,y=147)

        # Black Tea
        drink6=Checkbutton(label_frame4,text='Black Tea',font=('arial',14),variable=self.var27,
                           onvalue=1,offvalue=0,bg='black',fg='brown',command=self.drink_6)
        drink6.place(x=3,y=177)
        global ent_drink6
        ent_drink6=ttk.Entry(label_frame4,width=2,font=('arial',10,'bold'),
                             textvariable=self.black_tea,state=DISABLED)
        ent_drink6.place(x=150,y=182)

        # Green Tea
        drink7=Checkbutton(label_frame4,text='Green Tea',font=('arial',14),variable=self.var28,
                           onvalue=1,offvalue=0,bg='black',fg='brown',command=self.drink_7)
        drink7.place(x=3,y=210)
        global ent_drink7
        ent_drink7=ttk.Entry(label_frame4,width=2,font=('arial',10,'bold'),
                             textvariable=self.green_tea,state=DISABLED)
        ent_drink7.place(x=150,y=215)

    def salad_1(self):
        if self.var1.get()==1:
            ent_salad1.config(state=NORMAL)
            ent_salad1.delete(0,END)
            ent_salad1.focus()
        else:
            ent_salad1.config(state=DISABLED)
            self.caesar_salad.set('0')

    def salad_2(self):
        if self.var2.get()==1:
            ent_salad2.config(state=NORMAL)
            ent_salad2.delete(0,END)
            ent_salad2.focus()
        else:
            ent_salad2.config(state=DISABLED)
            self.chef_salad.set('0')

    def salad_3(self):
        if self.var3.get()==1:
            ent_salad3.config(state=NORMAL)
            ent_salad3.delete(0,END)
            ent_salad3.focus()
        else:
            ent_salad3.config(state=DISABLED)
            self.coleslaw.set('0')

    def salad_4(self):
        if self.var4.get()==1:
            ent_salad4.config(state=NORMAL)
            ent_salad4.delete(0,END)
            ent_salad4.focus()
        else:
            ent_salad4.config(state=DISABLED)
            self.pasta_salad.set('0')

    def salad_5(self):
        if self.var5.get()==1:
            ent_salad5.config(state=NORMAL)
            ent_salad5.delete(0,END)
            ent_salad5.focus()
        else:
            ent_salad5.config(state=DISABLED)
            self.woldorf_salad.set('0')

    def salad_6(self):
        if self.var6.get()==1:
            ent_salad6.config(state=NORMAL)
            ent_salad6.delete(0,END)
            ent_salad6.focus()
        else:
            ent_salad6.config(state=DISABLED)
            self.sprout_salad.set('0')

    def salad_7(self):
        if self.var7.get()==1:
            ent_salad7.config(state=NORMAL)
            ent_salad7.delete(0,END)
            ent_salad7.focus()
        else:
            ent_salad7.config(state=DISABLED)
            self.tomato_salad.set('0')

    def main_1(self):
        if self.var8.get()==1:
            ent_mainc1.config(state=NORMAL)
            ent_mainc1.delete(0,END)
            ent_mainc1.focus()
        else:
            ent_mainc1.config(state=DISABLED)
            self.biryani.set('0')

    def main_2(self):
        if self.var9.get()==1:
            ent_mainc2.config(state=NORMAL)
            ent_mainc2.delete(0,END)
            ent_mainc2.focus()
        else:
            ent_mainc2.config(state=DISABLED)
            self.butter_chicken.set('0')

    def main_3(self):
        if self.var10.get()==1:
            ent_mainc3.config(state=NORMAL)
            ent_mainc3.delete(0,END)
            ent_mainc3.focus()
        else:
            ent_mainc3.config(state=DISABLED)
            self.big_thali.set('0')

    def main_4(self):
        if self.var11.get()==1:
            ent_mainc4.config(state=NORMAL)
            ent_mainc4.delete(0,END)
            ent_mainc4.focus()
        else:
            ent_mainc4.config(state=DISABLED)
            self.chole_bhature.set('0')

    def main_5(self):
        if self.var12.get()==1:
            ent_mainc5.config(state=NORMAL)
            ent_mainc5.delete(0,END)
            ent_mainc5.focus()
        else:
            ent_mainc5.config(state=DISABLED)
            self.dal_makhani.set('0')

    def main_6(self):
        if self.var13.get()==1:
            ent_mainc6.config(state=NORMAL)
            ent_mainc6.delete(0,END)
            ent_mainc6.focus()
        else:
            ent_mainc6.config(state=DISABLED)
            self.idli_dosa.set('0')

    def main_7(self):
        if self.var14.get()==1:
            ent_mainc7.config(state=NORMAL)
            ent_mainc7.delete(0,END)
            ent_mainc7.focus()
        else:
            ent_mainc7.config(state=DISABLED)
            self.litti_choka.set('0')

    def dessert_1(self):
        if self.var15.get()==1:
            ent_dessert1.config(state=NORMAL)
            ent_dessert1.delete(0,END)
            ent_dessert1.focus()
        else:
            ent_dessert1.config(state=DISABLED)
            self.pie.set('0')

    def dessert_2(self):
        if self.var16.get()==1:
            ent_dessert2.config(state=NORMAL)
            ent_dessert2.delete(0,END)
            ent_dessert2.focus()
        else:
            ent_dessert2.config(state=DISABLED)
            self.pancake.set('0')

    def dessert_3(self):
        if self.var17.get()==1:
            ent_dessert3.config(state=NORMAL)
            ent_dessert3.delete(0,END)
            ent_dessert3.focus()
        else:
            ent_dessert3.config(state=DISABLED)
            self.cake.set('0')

    def dessert_4(self):
        if self.var18.get()==1:
            ent_dessert4.config(state=NORMAL)
            ent_dessert4.delete(0,END)
            ent_dessert4.focus()
        else:
            ent_dessert4.config(state=DISABLED)
            self.cookies.set('0')

    def dessert_5(self):
        if self.var19.get()==1:
            ent_dessert5.config(state=NORMAL)
            ent_dessert5.delete(0,END)
            ent_dessert5.focus()
        else:
            ent_dessert5.config(state=DISABLED)
            self.ice_cream.set('0')

    def dessert_6(self):
        if self.var20.get()==1:
            ent_dessert6.config(state=NORMAL)
            ent_dessert6.delete(0,END)
            ent_dessert6.focus()
        else:
            ent_dessert6.config(state=DISABLED)
            self.chocolate.set('0')

    def dessert_7(self):
        if self.var21.get()==1:
            ent_dessert7.config(state=NORMAL)
            ent_dessert7.delete(0,END)
            ent_dessert7.focus()
        else:
            ent_dessert7.config(state=DISABLED)
            self.sweets.set('0')

    def drink_1(self):
        if self.var22.get()==1:
            ent_drink1.config(state=NORMAL)
            ent_drink1.delete(0,END)
            ent_drink1.focus()
        else:
            ent_drink1.config(state=DISABLED)
            self.fruit_juice.set('0')

    def drink_2(self):
        if self.var23.get()==1:
            ent_drink2.config(state=NORMAL)
            ent_drink2.delete(0,END)
            ent_drink2.focus()
        else:
            ent_drink2.config(state=DISABLED)
            self.hot_chocolate.set('0')

    def drink_3(self):
        if self.var24.get()==1:
            ent_drink3.config(state=NORMAL)
            ent_drink3.delete(0,END)
            ent_drink3.focus()
        else:
            ent_drink3.config(state=DISABLED)
            self.milk_shake.set('0')

    def drink_4(self):
        if self.var25.get()==1:
            ent_drink4.config(state=NORMAL)
            ent_drink4.delete(0,END)
            ent_drink4.focus()
        else:
            ent_drink4.config(state=DISABLED)
            self.tea.set('0')

    def drink_5(self):
        if self.var26.get()==1:
            ent_drink5.config(state=NORMAL)
            ent_drink5.delete(0,END)
            ent_drink5.focus()
        else:
            ent_drink5.config(state=DISABLED)
            self.coffee.set('0')

    def drink_6(self):
        if self.var27.get()==1:
            ent_drink6.config(state=NORMAL)
            ent_drink6.delete(0,END)
            ent_drink6.focus()
        else:
            ent_drink6.config(state=DISABLED)
            self.black_tea.set('0')

    def drink_7(self):
        if self.var28.get()==1:
            ent_drink7.config(state=NORMAL)
            ent_drink7.delete(0,END)
            ent_drink7.focus()
        else:
            ent_drink7.config(state=DISABLED)
            self.green_tea.set('0')


    def total_amount(self):

        if self.var1.get() != 0 or self.var2.get() != 0 or \
           self.var3.get() != 0 or self.var4.get() != 0 or \
           self.var5.get() != 0 or self.var6.get() != 0 or \
           self.var7.get() != 0 or self.var8.get() != 0 or \
           self.var9.get() != 0 or self.var10.get() != 0 or\
           self.var11.get() != 0 or self.var12.get() != 0 or \
           self.var13.get() != 0 or self.var14.get() != 0 or \
           self.var15.get() != 0 or self.var16.get() != 0 or \
           self.var17.get() != 0 or self.var18.get() != 0 or \
           self.var19.get() != 0 or self.var20.get() != 0 or \
           self.var21.get() != 0 or self.var22.get() != 0 or \
           self.var23.get() != 0 or self.var24.get() != 0 or \
           self.var25.get() != 0 or self.var26.get() != 0 or \
           self.var27.get() != 0:
            t1=int(self.caesar_salad.get())*40
            t2=int(self.chef_salad.get())*50
            t3=int(self.coleslaw.get())*55
            t4=int(self.pasta_salad.get())*100
            t5=int(self.woldorf_salad.get())*60
            t6=int(self.sprout_salad.get())*85
            t7=int(self.tomato_salad.get())*35

            t8=int(self.biryani.get())*150
            t9=int(self.butter_chicken.get())*200
            t10=int(self.big_thali.get())*180
            t11=int(self.chole_bhature.get())*210
            t12=int(self.dal_makhani.get())*120
            t13=int(self.idli_dosa.get())*150
            t14=int(self.litti_choka.get())*130

            t15=int(self.pie.get())*25
            t16=int(self.pancake.get())*40
            t17=int(self.cake.get())*50
            t18=int(self.cookies.get())*20
            t19=int(self.ice_cream.get())*80
            t20=int(self.chocolate.get())*30
            t21=int(self.sweets.get())*40

            t22=int(self.fruit_juice.get())*70
            t23=int(self.hot_chocolate.get())*150
            t24=int(self.milk_shake.get())*120
            t25=int(self.tea.get())*30
            t26=int(self.coffee.get())*55
            t27=int(self.black_tea.get())*80
            t28=int(self.green_tea.get())*40

            total=(t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12+t13+t14+t15+t16+t17+t18+t19+t20+
                                t21+t22+t23+t24+t25+t26+t27+t28)
            self.var_entry.set('Rs. '+str(total))
        else:
            messagebox.showerror('Error','No Item Is selected')

    def reset(self):
        textReceipt.delete(1.0,END)
        self.caesar_salad.set('0')
        self.chef_salad.set('0')
        self.coleslaw.set('0')
        self.pasta_salad.set('0')
        self.woldorf_salad.set('0')
        self.sprout_salad.set('0')
        self.tomato_salad.set('0')

        self.biryani.set('0')
        self.butter_chicken.set('0')
        self.big_thali.set('0')
        self.chole_bhature.set('0')
        self.dal_makhani.set('0')
        self.idli_dosa.set('0')
        self.litti_choka.set('0')
        
        self.pie.set('0')
        self.pancake.set('0')
        self.cake.set('0')
        self.cookies.set('0')
        self.ice_cream.set('0')
        self.chocolate.set('0')
        self.sweets.set('0')
        
        self.fruit_juice.set('0')
        self.hot_chocolate.set('0')
        self.milk_shake.set('0')
        self.tea.set('0')
        self.coffee.set('0')
        self.black_tea.set('0')
        self.green_tea.set('0')
        self.var_entry.set('')

        ent_salad1.config(state=DISABLED)
        ent_salad2.config(state=DISABLED)
        ent_salad3.config(state=DISABLED)
        ent_salad4.config(state=DISABLED)
        ent_salad5.config(state=DISABLED)
        ent_salad6.config(state=DISABLED)
        ent_salad7.config(state=DISABLED)

        ent_mainc1.config(state=DISABLED)
        ent_mainc2.config(state=DISABLED)
        ent_mainc3.config(state=DISABLED)
        ent_mainc4.config(state=DISABLED)
        ent_mainc5.config(state=DISABLED)
        ent_mainc6.config(state=DISABLED)
        ent_mainc7.config(state=DISABLED)

        ent_dessert1.config(state=DISABLED)
        ent_dessert2.config(state=DISABLED)
        ent_dessert3.config(state=DISABLED)
        ent_dessert4.config(state=DISABLED)
        ent_dessert5.config(state=DISABLED)
        ent_dessert6.config(state=DISABLED)
        ent_dessert7.config(state=DISABLED)

        ent_drink1.config(state=DISABLED)
        ent_drink2.config(state=DISABLED)
        ent_drink3.config(state=DISABLED)
        ent_drink4.config(state=DISABLED)
        ent_drink5.config(state=DISABLED)
        ent_drink6.config(state=DISABLED)
        ent_drink7.config(state=DISABLED)

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
        self.var13.set(0)
        self.var14.set(0)
        self.var15.set(0)
        self.var16.set(0)
        self.var17.set(0)
        self.var18.set(0)
        self.var19.set(0)
        self.var20.set(0)
        self.var21.set(0)
        self.var22.set(0)
        self.var23.set(0)
        self.var24.set(0)
        self.var25.set(0)
        self.var26.set(0)
        self.var27.set(0)
    def receipt(self):
        textReceipt.delete(1.0,END)
        if self.var_entry.get()!='':
            a=random.randint(1001,99999)
            billno='BILL NO. '+ str(a)
            date=time.strftime('     %d/%m/%Y')
            textReceipt.insert(END,'******************************************\n')
            textReceipt.insert(END,'\t   ROYAL HOTEL \n')
            textReceipt.insert(END,'******************************************\n')
            textReceipt.insert(END,billno+'\t\t'+date+'\n')
            textReceipt.insert(END,'******************************************\n')
            textReceipt.insert(END,' Items:         \t\t              Amount \n')
            textReceipt.insert(END,'******************************************\n')
            
            if self.caesar_salad.get()!='0':
                textReceipt.insert(END,f'Caesar Salad \t\t\t {int(self.caesar_salad.get())*40}\n')
            if self.chef_salad.get()!='0':
                textReceipt.insert(END,f'Chef Salad \t\t\t {int(self.chef_salad.get())*50}\n')
            if self.coleslaw.get()!='0':
                textReceipt.insert(END,f'Coleslaw \t\t\t {int(self.coleslaw.get())*55}\n')
            if self.pasta_salad.get()!='0':
                textReceipt.insert(END,f'Pasta Salad \t\t\t {int(self.pasta_salad.get())*100}\n')
            if self.woldorf_salad.get()!='0':
                textReceipt.insert(END,f'Woldorf Salad \t\t\t {int(self.woldorf_salad.get())*60}\n')
            if self.sprout_salad.get()!='0':
                textReceipt.insert(END,f'Sprout Salad \t\t\t {int(self.sprout_salad.get())*85}\n')
            if self.tomato_salad.get()!='0':
                textReceipt.insert(END,f'Tomato Salad \t\t\t {int(self.tomato_salad.get())*35}\n')
                
            if self.biryani.get()!='0':
                textReceipt.insert(END,f'Biryani \t\t\t {int(self.biryani.get())*150}\n')
            if self.butter_chicken.get()!='0':
                textReceipt.insert(END,f'Butter chicken \t\t\t {int(self.butter_chicken.get())*200}\n')
            if self.big_thali.get()!='0':
                textReceipt.insert(END,f'Big thali \t\t\t {int(self.big_thali.get())*180}\n')
            if self.chole_bhature.get()!='0':
                textReceipt.insert(END,f'Chole bhature \t\t\t {int(self.chole_bhature.get())*210}\n')
            if self.dal_makhani.get()!='0':
                textReceipt.insert(END,f'Dal makhani \t\t\t {int(self.dal_makhani.get())*120}\n')
            if self.idli_dosa.get()!='0':
                textReceipt.insert(END,f'Idli & Dosa \t\t\t {int(self.idli_dosa.get())*150}\n')
            if self.litti_choka.get()!='0':
                textReceipt.insert(END,f'Litti Choka \t\t\t {int(self.litti_choka.get())*130}\n')
                
            if self.pie.get()!='0':
                textReceipt.insert(END,f'Pie \t\t\t {int(self.pie.get())*25}\n')
            if self.pancake.get()!='0':
                textReceipt.insert(END,f'Pancake \t\t\t {int(self.pancake.get())*40}\n')
            if self.cake.get()!='0':
                textReceipt.insert(END,f'Cake \t\t\t {int(self.cake.get())*50}\n')
            if self.cookies.get()!='0':
                textReceipt.insert(END,f'Cookies \t\t\t {int(self.cookies.get())*20}\n')
            if self.ice_cream.get()!='0':
                textReceipt.insert(END,f'Ice cream \t\t\t {int(self.ice_cream.get())*80}\n')
            if self.chocolate.get()!='0':
                textReceipt.insert(END,f'Chocolate \t\t\t {int(self.chocolate.get())*30}\n')
            if self.sweets.get()!='0':
                textReceipt.insert(END,f'Sweets \t\t\t {int(self.sweets.get())*40}\n')
                
            if self.fruit_juice.get()!='0':
                textReceipt.insert(END,f'Fruit juice \t\t\t {int(self.fruit_juice.get())*70}\n')
            if self.hot_chocolate.get()!='0':
                textReceipt.insert(END,f'Hot chocolate \t\t\t {int(self.hot_chocolate.get())*150}\n')
            if self.milk_shake.get()!='0':
                textReceipt.insert(END,f'Milk shake \t\t\t {int(self.milk_shake.get())*120}\n')
            if self.tea.get()!='0':
                textReceipt.insert(END,f'Tea \t\t\t {int(self.tea.get())*30}\n')
            if self.coffee.get()!='0':
                textReceipt.insert(END,f'Coffee \t\t\t {int(self.coffee.get())*55}\n')
            if self.black_tea.get()!='0':
                textReceipt.insert(END,f'Black tea \t\t\t {int(self.black_tea.get())*80}\n')
            if self.green_tea.get()!='0':
                textReceipt.insert(END,f'Green tea \t\t\t {int(self.green_tea.get())*40}\n')

            textReceipt.insert(END,'******************************************\n')
            textReceipt.insert(END,'\n')
            textReceipt.insert(END,f'Total Amount: \t\t    {self.var_entry.get()}\n')
            textReceipt.insert(END,'******************************************\n')
            textReceipt.insert(END,'\t    THANK YOU  \t')
        else:
            messagebox.showerror('Error','No Item Is selected')
        

if __name__ == "__main__":
    root=Tk()
    obj=restaurent(root)
    root.mainloop()
