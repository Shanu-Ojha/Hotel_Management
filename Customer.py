from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
import random
import mysql.connector as msql
from tkinter import messagebox


class Cust_window():
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1120x480+220+200')
        self.root.resizable(0,0)

        # ==================== varible ====================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationatity=StringVar()
        self.var_id=StringVar()
        self.var_idno=StringVar()
        self.var_address=StringVar()

        # ========== Title =============
        title=Label(self.root,text='ADD CUSTOMER DETAILS',font=('Times New Roman',18,'bold')
                    ,bg='black',fg='gold',bd=4,relief=RIDGE)
        title.place(x=0,y=0,width=1120,height=40)

        # ========= Logo ===========
        img1=Image.open(r'logo.png')
        img1=img1.resize((100,40),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_img=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        label_img.place(x=4,y=4,width=60,height=30)

        # =========== label Frame =======
        label_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',
                                    font=('Times New Roman',15,'bold'),padx=2)
        label_frame_left.place(x=3,y=40,width=360,height=435)

        # ============= Labels and entry ============
        # Customer Ref
        lbl_cust_ref=Label(label_frame_left,text='Customer Ref',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        ent_ref=ttk.Entry(label_frame_left,width=17,textvariable=self.var_ref,
                          font=('MV Boli',11,'bold'),state='readonly')
        ent_ref.grid(row=0,column=1)

        # Customer name
        lbl_cust_name=Label(label_frame_left,text='Customer Name:',
                            font=('Times New Roman',13,'bold'),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        ent_name=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),
                           textvariable=self.var_name)
        ent_name.grid(row=1,column=1)

        # Customer Age
        lbl_cust_age=Label(label_frame_left,text='Age:',font=('Times New Roman',13,'bold')
                           ,padx=2,pady=6)
        lbl_cust_age.grid(row=2,column=0,sticky=W)

        ent_age=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),
                          textvariable=self.var_age)
        ent_age.grid(row=2,column=1)

        # Gender combobox
        lbl_cust_gender=Label(label_frame_left,text='Gender:',font=('Times New Roman',13,'bold')
                              ,padx=2,pady=6)
        lbl_cust_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(label_frame_left,font=('MV Boli',13,'bold'),
                                  textvariable=self.var_gender,width=14,state='readonly')
        combo_gender['values']=('Male','Female','Others')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # Mobile No.
        lbl_cust_mobile=Label(label_frame_left,text='Mobile No:',font=('Times New Roman',13,'bold')
                              ,padx=2,pady=6)
        lbl_cust_mobile.grid(row=4,column=0,sticky=W)

        ent_mobile=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),
                             textvariable=self.var_mobile)
        ent_mobile.grid(row=4,column=1)

        # Email
        lbl_cust_email=Label(label_frame_left,text='Email ID:',font=('Times New Roman',13,'bold')
                             ,padx=2,pady=6)
        lbl_cust_email.grid(row=5,column=0,sticky=W)

        ent_email=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),
                            textvariable=self.var_email)
        ent_email.grid(row=5,column=1)

        # Nationality combobox
        lbl_cust_nationality=Label(label_frame_left,text='Nationality:',
                                   font=('Times New Roman',13,'bold'),padx=2,pady=6)
        lbl_cust_nationality.grid(row=6,column=0,sticky=W)

        combo_nationality=ttk.Combobox(label_frame_left,textvariable=self.var_nationatity,
                                       font=('MV Boli',13,'bold'),width=14,state='readonly')
        combo_nationality['values']=('India','America','Canada','Germany','Sri Lanka','Japan','Nepal','China','Bhutan')
        combo_nationality.current(0)
        combo_nationality.grid(row=6,column=1)


        # ID combobox
        lbl_cust_id=Label(label_frame_left,text='ID Proof:',font=('Times New Roman',13,'bold'),
                          padx=2,pady=6)
        lbl_cust_id.grid(row=7,column=0,sticky=W)

        combo_id=ttk.Combobox(label_frame_left,textvariable=self.var_id,font=('MV Boli',13,'bold')
                              ,width=14,state='readonly')
        combo_id['values']=('Aadhar card','Passport','Driving licence','Other')
        combo_id.current(0)
        combo_id.grid(row=7,column=1)


        # ID No.
        lbl_cust_idno=Label(label_frame_left,text='ID Number:',font=('Times New Roman',13,'bold'),
                            padx=2,pady=6)
        lbl_cust_idno.grid(row=8,column=0,sticky=W)

        ent_idno=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),textvariable=self.var_idno)
        ent_idno.grid(row=8,column=1)

        # Address
        lbl_cust_address=Label(label_frame_left,text='Address:',font=('Times New Roman',13,'bold'),
                               padx=2,pady=6)
        lbl_cust_address.grid(row=9,column=0,sticky=W)

        ent_address=ttk.Entry(label_frame_left,width=17,font=('MV Boli',11,'bold'),textvariable=self.var_address)
        ent_address.grid(row=9,column=1)

        # ================= Buttons ======================
        button_frame=Frame(label_frame_left,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=350,width=350,height=50)

        butadd=Button(button_frame,text='ADD',command=self.add_detail,font=('arial',12,'bold'),
                      bg='black',fg='gold',width=7)
        butadd.grid(row=0,column=0,padx=3,pady=6)

        butupdate=Button(button_frame,text='UPDATE',command=self.update,font=('arial',12,'bold'),
                         bg='black',fg='gold',width=7)
        butupdate.grid(row=0,column=1,padx=3,pady=6)

        butdelete=Button(button_frame,text='DELETE',command=self.Delete,font=('arial',12,'bold'),
                         bg='black',fg='gold',width=7)
        butdelete.grid(row=0,column=2,padx=3,pady=6)

        butreset=Button(button_frame,text='RESET',command=self.reset,font=('arial',12,'bold'),
                        bg='black',fg='gold',width=7)
        butreset.grid(row=0,column=3,padx=3,pady=6)

        # ====================== table frame and search=========================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search',
                               font=('Times New Roman',15,'bold'),padx=2)
        table_frame.place(x=370,y=40,width=745,height=435)

        lbl_search=Label(table_frame,text='Search By:',font=('Times New Roman',12,'bold'),
                         bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W,padx=2)

        self.var_search=StringVar()
        combo_search=ttk.Combobox(table_frame,font=('MV Boli',12,'bold'),width=9,state='readonly',
                                  textvariable=self.var_search)
        combo_search['values']=('Mobile','Ref')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.var_entry=StringVar()
        ent_search=ttk.Entry(table_frame,width=15,font=('MV Boli',12,'bold'),textvariable=self.var_entry)
        ent_search.grid(row=0,column=3,padx=2)

        butsearch=Button(table_frame,text='Search',command=self.search,font=('arial',10,'bold'),
                         bg='black',fg='gold',width=10)
        butsearch.grid(row=0,column=4,padx=3)

        butshowall=Button(table_frame,text='Show All',command=self.fetch_data,font=('arial',10,'bold'),
                          bg='black',fg='gold',width=10)
        butshowall.grid(row=0,column=5,padx=6)

        # ======================== Table all Record ========================
        data_frame=Frame(table_frame,bd=2,relief=RIDGE)
        data_frame.place(x=0,y=40,width=735,height=330)

        scroll_x=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_frame,orient=VERTICAL)

        self.cust_detail_table=ttk.Treeview(data_frame,columns=('Cust Ref','Cust Name','Age','Gender',
                                                                'Mobile no.','Email ID','Nationality',
                                                                'ID Type','ID No.','Address'),
                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_detail_table.xview)
        scroll_y.config(command=self.cust_detail_table.yview)

        self.cust_detail_table.heading('Cust Ref',text='Cust Ref')
        self.cust_detail_table.heading('Cust Name',text='Cust Name')
        self.cust_detail_table.heading('Age',text='Age')
        self.cust_detail_table.heading('Gender',text='Gender')
        self.cust_detail_table.heading('Mobile no.',text='Mobile No.')
        self.cust_detail_table.heading('Email ID',text='Email ID')
        self.cust_detail_table.heading('Nationality',text='Nationality')
        self.cust_detail_table.heading('ID Type',text='ID Type')
        self.cust_detail_table.heading('ID No.',text='ID No.')
        self.cust_detail_table.heading('Address',text='Address')

        self.cust_detail_table['show']='headings'

        self.cust_detail_table.column('Cust Ref',width=60)
        self.cust_detail_table.column('Cust Name',width=100)
        self.cust_detail_table.column('Age',width=40)
        self.cust_detail_table.column('Gender',width=60)
        self.cust_detail_table.column('Mobile no.',width=100)
        self.cust_detail_table.column('Email ID',width=170)
        self.cust_detail_table.column('Nationality',width=80)
        self.cust_detail_table.column('ID Type',width=120)
        self.cust_detail_table.column('ID No.',width=150)
        self.cust_detail_table.column('Address',width=180)

        self.cust_detail_table.pack(fill=BOTH,expand=1)
        self.cust_detail_table.bind('<ButtonRelease-1>',self.get_data)
        self.fetch_data()

    def add_detail(self):
        if self.var_mobile.get()=='' or self.var_name.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
                cursor=con.cursor()
                # ========= creating database and table if not exists ===========
                cursor.execute('Create database if not exists Royal_Hotel;')
                cursor.execute('USE Royal_Hotel;')
                cursor.execute('Create table if not exists customers ('
                                'Ref int primary key,'
                                'Name varchar(20),'
                                'Age varchar(20),'
                                'Gender varchar(20),'
                                'Mobile varchar(20),'
                                'Email varchar(30),'
                                'Nation varchar(20),'
                                'id varchar(20),'
                                'idno varchar(20),'
                                'Address varchar(20));')
                con.commit()
                # =========== inserting values =============================
                insert=("Insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
                add=(self.var_ref.get(),self.var_name.get(),self.var_age.get(),self.var_gender.get()
                     ,self.var_mobile.get(),self.var_email.get(),self.var_nationatity.get(),self.var_id.get()
                     ,self.var_idno.get(),self.var_address.get())
                cursor.execute(insert,add)
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('Conguratlation','You have been registered',parent=self.root)
            
            except Exception as es:
                messagebox.showwarning('Warning',f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
        cursor=con.cursor()
        cursor.execute('Select * from customers')
        rows=cursor.fetchall()
        if len(rows):
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows:
                self.cust_detail_table.insert('',END,values=i)
            con.commit()
        con.close()

    def get_data(self,event=''):
        data_row=self.cust_detail_table.focus()
        content=self.cust_detail_table.item(data_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_age.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_nationatity.set(row[6]),
        self.var_id.set(row[7]),
        self.var_idno.set(row[8]),
        self.var_address.set(row[9])

    def update(self):
        if self.var_name.get()=='':
            messagebox.showerror('Error','No record has been selected',parent=self.root)
        else:
            con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
            cursor=con.cursor()
            cursor.execute('Update customers set Name=%s,Age=%s,Gender=%s,Mobile=%s,Email=%s,Nation=%s,id=%s,idno=%s,'
                            'Address=%s where Ref=%s',(self.var_name.get(),
                                                       self.var_age.get(),
                                                       self.var_gender.get(),
                                                       self.var_mobile.get(),
                                                       self.var_email.get(),
                                                       self.var_nationatity.get(),
                                                       self.var_id.get(),
                                                       self.var_idno.get(),
                                                       self.var_address.get(),
                                                       self.var_ref.get()))
            
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo('Updated','Customer details has been updated',parent=self.root)

            self.var_name.set(''),
            self.var_age.set(''),
            self.var_mobile.set(''),
            self.var_email.set(''),
            self.var_idno.set(''),
            self.var_address.set('')

            x=random.randint(1000,9999)
            self.var_ref.set(str(x))

    def Delete(self):
        if self.var_name.get()=='':
            messagebox.showerror('Error','No record has been selected',parent=self.root)
        else:
            Delete=messagebox.askyesno('Alert','Do you want to delete this customer',parent=self.root)
            if Delete>0:
                con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
                cursor=con.cursor()
                cursor.execute("delete from customers where Ref=%s",(self.var_ref.get(),))
            else:
                if not Delete:
                    return
            con.commit()
            self.fetch_data()
            con.close()
            
            self.var_name.set(''),
            self.var_age.set(''),
            self.var_mobile.set(''),
            self.var_email.set(''),
            self.var_idno.set(''),
            self.var_address.set('')

            x=random.randint(1000,9999)
            self.var_ref.set(str(x))

    def reset(self):
        self.var_name.set(''),
        self.var_age.set(''),
        self.var_mobile.set(''),
        self.var_email.set(''),
        self.var_idno.set(''),
        self.var_address.set('')

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        con=msql.connect(host='localhost',user='root',passwd='root',database='Royal_Hotel')
        cursor=con.cursor()
        cursor.execute('Select * from customers where '+str(self.var_search.get())
                       +" like '%"+str(self.var_entry.get())+"%'")
        rows=cursor.fetchall()
        if len(rows):
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows:
                self.cust_detail_table.insert('',END,values=i)
            con.commit()
        con.close()


if __name__ == "__main__" :
    root=Tk()
    obj=Cust_window(root)
    root.mainloop()
