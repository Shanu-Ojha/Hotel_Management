from distutils import command
from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
from time import strptime
from datetime import datetime 
import random
import mysql.connector as msql
from tkinter import messagebox


class room_window():
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1120x480+220+200')
        self.root.resizable(0,0)

        # ============== Variables =================

        self.var_ref=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomno=StringVar()
        self.var_noofdays=StringVar()
        self.var_amount=StringVar()
        self.var_tax=StringVar()
        self.var_total=StringVar()
        self.var_search=StringVar()
        self.var_entry=StringVar()

        # ========== Title =============
        title=Label(self.root,text='ROOM BOOKING DETAILS',font=('Times New Roman',18,'bold')
                    ,bg='black',fg='gold',bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1120,height=40)

        # ========= Logo ===========
        img1=Image.open(r'logo.png')
        img1=img1.resize((100,40),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_img=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        label_img.place(x=4,y=4,width=60,height=30)

        # ========= Right img ===========
        img2=Image.open(r'pic9.png')
        img2=img2.resize((350,200),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_img=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        label_img.place(x=750,y=55,width=350,height=200)

         # =========== label Frame =======
        label_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Booking Details',
                                    font=('Times New Roman',15,'bold'),padx=2)
        label_frame_left.place(x=3,y=40,width=360,height=435)
     
        # ============= Labels and entry ============
        # Customer Ref
        lbl_cust_ref=Label(label_frame_left,text='Customer Ref:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        ent_ref=ttk.Entry(label_frame_left,width=10,font=('MV Boli',11,'bold'),
                          textvariable=self.var_ref)
        ent_ref.grid(row=0,column=1,sticky=W)

        # Fetch button
        butbill=Button(label_frame_left,text='FETCH DATA',command=self.fetch_details,font=('arial',10,'bold'),
                        bg='black',fg='gold',width=11)
        butbill.place(x=250,y=3)

        # Check_in date
        lbl_checkin=Label(label_frame_left,text='Check In:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_checkin.grid(row=1,column=0,sticky=W)

        ent_checkin=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),
                          textvariable=self.var_checkin)
        ent_checkin.grid(row=1,column=1)

        # Check_out date
        lbl_checkout=Label(label_frame_left,text='Check Out:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_checkout.grid(row=2,column=0,sticky=W)

        ent_checkout=ttk.Entry(label_frame_left,width=15,font=('MV Boli',11,'bold'),
                          textvariable=self.var_checkout)
        ent_checkout.grid(row=2,column=1,sticky=W)

        # No of days
        lbl_days=Label(label_frame_left,text='No. of Days:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_days.grid(row=3,column=0,sticky=W)

        ent_days=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),
                          textvariable=self.var_noofdays,state='readonly')
        ent_days.grid(row=3,column=1)

        # OK button
        butbill=Button(label_frame_left,text='OK',command=self.date,font=('arial',10,'bold'),
                        bg='black',fg='gold',width=3)
        butbill.place(x=310,y=73)

        # Room type
        lbl_roomtype=Label(label_frame_left,text='Room Type:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_roomtype.grid(row=4,column=0,sticky=W)

        combo_roomtype=ttk.Combobox(label_frame_left,font=('MV Boli',13,'bold'),width=14,state='readonly',
                          textvariable=self.var_roomtype)
        combo_roomtype['values']=('Single','Double','King','Queen','Twin','Cabana')
        combo_roomtype.current(0)
        combo_roomtype.grid(row=4,column=1)

        # Room No.
        lbl_room=Label(label_frame_left,text='Room No:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_room.grid(row=5,column=0,sticky=W)

        ent_room=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),
                          textvariable=self.var_roomno)
        ent_room.grid(row=5,column=1)

        # Bill button
        butbill=Button(label_frame_left,text='BILL',command=self.total,font=('arial',10,'bold'),
                        bg='black',fg='gold',width=7)
        butbill.grid(row=6,column=0,padx=3,pady=6)

        # Amount
        lbl_amount=Label(label_frame_left,text='Amount:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_amount.grid(row=7,column=0,sticky=W)

        ent_amount=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),state='readonly',
                          textvariable=self.var_amount)
        ent_amount.grid(row=7,column=1)

        # Tax
        lbl_tax=Label(label_frame_left,text='Paid Tax:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_tax.grid(row=8,column=0,sticky=W)

        ent_tax=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),state='readonly',
                          textvariable=self.var_tax)
        ent_tax.grid(row=8,column=1)

        # Total Amount
        lbl_tamount=Label(label_frame_left,text='Total Amount:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_tamount.grid(row=9,column=0,sticky=W)

        ent_tamount=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),state='readonly',
                          textvariable=self.var_total)
        ent_tamount.grid(row=9,column=1)

        # ================= Buttons ======================
        button_frame=Frame(label_frame_left,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=355,width=350,height=45)

        butadd=Button(button_frame,text='ADD',font=('arial',12,'bold'),
                      bg='black',fg='gold',width=7,command=self.add_detail)
        butadd.grid(row=0,column=0,padx=3,pady=6)

        butupdate=Button(button_frame,text='UPDATE',font=('arial',12,'bold'),
                         bg='black',fg='gold',width=7,command=self.update)
        butupdate.grid(row=0,column=1,padx=3,pady=6)

        butdelete=Button(button_frame,text='DELETE',font=('arial',12,'bold'),
                         bg='black',fg='gold',width=7,command=self.Delete)
        butdelete.grid(row=0,column=2,padx=3,pady=6)

        butreset=Button(button_frame,text='RESET',font=('arial',12,'bold'),
                        bg='black',fg='gold',width=7,command=self.reset)
        butreset.grid(row=0,column=3,padx=3,pady=6)

        # ====================== table frame and search=========================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search',
                               font=('Times New Roman',15,'bold'),padx=2)
        table_frame.place(x=370,y=230,width=745,height=245)

        lbl_search=Label(table_frame,text='Search By:',font=('Times New Roman',12,'bold'),
                         bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(table_frame,font=('MV Boli',12,'bold'),width=9,state='readonly',
                                    textvariable=self.var_search)
        combo_search['values']=('Room_no','Ref')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        ent_search=ttk.Entry(table_frame,width=15,font=('MV Boli',12,'bold'),textvariable=self.var_entry)
        ent_search.grid(row=0,column=3,padx=2)

        butsearch=Button(table_frame,text='Search',font=('arial',10,'bold'),
                         bg='black',fg='gold',width=10,command=self.search)
        butsearch.grid(row=0,column=4,padx=3)

        butshowall=Button(table_frame,text='Show All',font=('arial',10,'bold'),
                          bg='black',fg='gold',width=10,command=self.fetch_data)
        butshowall.grid(row=0,column=5,padx=6)

        # ======================== Table all Record ========================
        data_frame=Frame(table_frame,bd=2,relief=RIDGE)
        data_frame.place(x=0,y=40,width=735,height=175)

        scroll_x=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(data_frame,columns=('Cust Ref','Check In','Check Out','No. of days','Room type',
                                                                'Room no.'),
                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('Cust Ref',text='Cust Ref')
        self.room_table.heading('Check In',text='Check In')
        self.room_table.heading('Check Out',text='Check Out')
        self.room_table.heading('Room type',text='Room type')
        self.room_table.heading('Room no.',text='Room no.')
        self.room_table.heading('No. of days',text='No. of days')

        self.room_table['show']='headings'

        self.room_table.column('Cust Ref',width=50)
        self.room_table.column('Check In',width=80)
        self.room_table.column('Check Out',width=80)
        self.room_table.column('Room type',width=100)
        self.room_table.column('Room no.',width=60)
        self.room_table.column('No. of days',width=60)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind('<ButtonRelease-1>',self.get_data)
        self.fetch_data()

    #============ Fetching all details ==============================

    def fetch_details(self):
        if self.var_ref.get()=='':
            messagebox.showerror('Error','Please enter Ref ID',parent=self.root)
            
        else:
            con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
            cursor=con.cursor()
            query=('Select * from customers where Ref=%s')
            value=(self.var_ref.get(),)
            cursor.execute(query,value)
            row=cursor.fetchall()

            if row==[]:
                messagebox.showerror('Error',"Ref ID doesn't exist",parent=self.root)
            else:
                con.commit()
                con.close()

                showDf=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDf.place(x=370,y=52,width=370,height=180)
                for i in row:
                    lblname=Label(showDf,text='Name:',font=('Times New Roman',15,'bold'))
                    lblname.place(x=0,y=0)
                    lbl1=Label(showDf,text=i[1],font=('Times New Roman',15,'bold'))
                    lbl1.place(x=60,y=0)

                    lblgender=Label(showDf,text='Gender:',font=('Times New Roman',15,'bold'))
                    lblgender.place(x=0,y=25)
                    lbl2=Label(showDf,text=i[3],font=('Times New Roman',15,'bold'))
                    lbl2.place(x=80,y=25)

                    lblage=Label(showDf,text='Age:',font=('Times New Roman',15,'bold'))
                    lblage.place(x=0,y=50)
                    lbl3=Label(showDf,text=i[2],font=('Times New Roman',15,'bold'))
                    lbl3.place(x=80,y=50)

                    lblmobile=Label(showDf,text='Mobile No:',font=('Times New Roman',15,'bold'))
                    lblmobile.place(x=0,y=75)
                    lbl4=Label(showDf,text=i[4],font=('Times New Roman',15,'bold'))
                    lbl4.place(x=100,y=75)

                    lblmail=Label(showDf,text='Email:',font=('Times New Roman',15,'bold'))
                    lblmail.place(x=0,y=100)
                    lbl5=Label(showDf,text=i[5],font=('Times New Roman',15,'bold'))
                    lbl5.place(x=60,y=100)

                    lblnation=Label(showDf,text='Nationality:',font=('Times New Roman',15,'bold'))
                    lblnation.place(x=0,y=123)
                    lbl6=Label(showDf,text=i[6],font=('Times New Roman',15,'bold'))
                    lbl6.place(x=110,y=123)

                    lbladdress=Label(showDf,text='Address:',font=('Times New Roman',15,'bold'))
                    lbladdress.place(x=0,y=145)
                    lbl7=Label(showDf,text=i[9],font=('Times New Roman',15,'bold'))
                    lbl7.place(x=90,y=145)

    def date(self):
        if self.var_checkin.get=='' or self.var_checkout.get()=='':
            messagebox.showerror('Error','Entries are empty',parent=self.root)
        else:
            indate=self.var_checkin.get()
            outdate=self.var_checkout.get()
            indate=datetime.strptime(indate,"%d/%m/%Y")
            outdate=datetime.strptime(outdate,"%d/%m/%Y")
            self.var_noofdays.set(abs(outdate-indate).days)

    def add_detail(self):
        if self.var_ref.get()=='' or self.var_checkin.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
                cursor=con.cursor()
                # ========= creating table if not exists ===========
                cursor.execute('Create table if not exists rooms'
                            '('
                            'Ref int ,'
                            'Check_in varchar(20),'
                            'Check_out varchar(20),'
                            'No_of_days varchar(30),'
                            'Room_type varchar(20),'
                            'Room_no varchar(20) primary key)')
                # =========== inserting values =============================
                insert=("Insert into rooms values(%s,%s,%s,%s,%s,%s)")
                add=(self.var_ref.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_noofdays.get()
                     ,self.var_roomtype.get(),self.var_roomno.get())
                cursor.execute(insert,add)
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('Conguratlation','Room booked succesfully',parent=self.root)
            
            except Exception as es:
                messagebox.showwarning('Warning',f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
        cursor=con.cursor()
        cursor.execute('Select * from rooms')
        rows=cursor.fetchall()
        if len(rows):
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('',END,values=i)
            con.commit()
        con.close()
    
    def get_data(self,event=''):
        data_row=self.room_table.focus()
        content=self.room_table.item(data_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_noofdays.set(row[3]),
        self.var_roomtype.set(row[4]),
        self.var_roomno.set(row[5])

    def update(self):
        if self.var_ref.get()=='':
            messagebox.showerror('Error','No record has been selected',parent=self.root)
        else:
            con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
            cursor=con.cursor()
            cursor.execute('Update rooms set Check_in=%s,Check_out=%s,No_of_days=%s,Room_type=%s,Room_no=%s where Ref=%s',
                                                       (self.var_checkin.get(),
                                                       self.var_checkout.get(),
                                                       self.var_noofdays.get(),
                                                       self.var_roomtype.get(),
                                                       self.var_roomno.get(),
                                                       self.var_ref.get()))
            
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo('Updated','Details has been updated',parent=self.root)

            self.var_ref.set(''),
            self.var_checkin.set(''),
            self.var_checkout.set(''),
            self.var_roomtype.set('Single'),
            self.var_roomno.set(''),
            self.var_noofdays.set('')

    def Delete(self):
        if self.var_ref.get()=='':
            messagebox.showerror('Error','No record has been selected',parent=self.root)
        else:
            Delete=messagebox.askyesno('Alert','Do you want to delete this record',parent=self.root)
            if Delete>0:
                con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
                cursor=con.cursor()
                cursor.execute("delete from rooms where Ref=%s",(self.var_ref.get(),))
            else:
                if not Delete:
                    return
            con.commit()
            self.fetch_data()
            con.close()
            
            self.var_ref.set(''),
            self.var_checkin.set(''),
            self.var_checkout.set(''),
            self.var_roomtype.set('Single'),
            self.var_roomno.set(''),
            self.var_noofdays.set('')

    def reset(self):
        self.var_ref.set(''),
        self.var_checkin.set(''),
        self.var_checkout.set(''),
        self.var_roomtype.set('Single'),
        self.var_roomno.set(''),
        self.var_noofdays.set(''),
        self.var_amount.set(''),
        self.var_tax.set(''),
        self.var_total.set('')

    def total(self):
        if self.var_roomtype.get()=='Single':
            q1=float(800)
            q2=float(self.var_noofdays.get())
            q3=q1*q2
            amo='Rs.'+str('%.2f'%(q3))
            tax='Rs.'+str('%.2f'%((q3)*0.2))
            t='Rs.'+str('%.2f'%((q3)+((q3)*0.2)))
            self.var_amount.set(amo)
            self.var_tax.set(tax)
            self.var_total.set(t)
        elif self.var_roomtype.get()=='Double':
            q1=float(1200)
            q2=float(self.var_noofdays.get())
            q3=q1*q2
            amo='Rs.'+str('%.2f'%(q3))
            tax='Rs.'+str('%.2f'%((q3)*0.2))
            t='Rs.'+str('%.2f'%((q3)+((q3)*0.2)))
            self.var_amount.set(amo)
            self.var_tax.set(tax)
            self.var_total.set(t)
        elif self.var_roomtype.get()=='King':
            q1=float(1500)
            q2=float(self.var_noofdays.get())
            q3=q1*q2
            amo='Rs.'+str('%.2f'%(q3))
            tax='Rs.'+str('%.2f'%((q3)*0.2))
            t='Rs.'+str('%.2f'%((q3)+((q3)*0.2)))
            self.var_amount.set(amo)
            self.var_tax.set(tax)
            self.var_total.set(t)
        elif self.var_roomtype.get()=='Queen':
            q1=float(1400)
            q2=float(self.var_noofdays.get())
            q3=q1*q2
            amo='Rs.'+str('%.2f'%(q3))
            tax='Rs.'+str('%.2f'%((q3)*0.2))
            t='Rs.'+str('%.2f'%((q3)+((q3)*0.2)))
            self.var_amount.set(amo)
            self.var_tax.set(tax)
            self.var_total.set(t)
        elif self.var_roomtype.get()=='Twin':
            q1=float(1350)
            q2=float(self.var_noofdays.get())
            q3=q1*q2
            amo='Rs.'+str('%.2f'%(q3))
            tax='Rs.'+str('%.2f'%((q3)*0.2))
            t='Rs.'+str('%.2f'%((q3)+((q3)*0.2)))
            self.var_amount.set(amo)
            self.var_tax.set(tax)
            self.var_total.set(t)
        elif self.var_roomtype.get()=='Cabana':
            q1=float(1800)
            q2=float(self.var_noofdays.get())
            q3=q1*q2
            amo='Rs.'+str('%.2f'%(q3))
            tax='Rs.'+str('%.2f'%((q3)*0.2))
            t='Rs.'+str('%.2f'%((q3)+((q3)*0.2)))
            self.var_amount.set(amo)
            self.var_tax.set(tax)
            self.var_total.set(t)

    def search(self):
        con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
        cursor=con.cursor()
        cursor.execute('Select * from rooms where '+str(self.var_search.get())
                        +" like '%"+str(self.var_entry.get())+"%'")
        rows=cursor.fetchall()
        if len(rows):
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('',END,values=i)
            con.commit()
        con.close()


if __name__ == "__main__" :
    root=Tk()
    obj=room_window(root)
    root.mainloop()