from cProfile import label
from ctypes import alignment
from email import contentmanager
from json.tool import main
from re import L
from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from turtle import bgcolor
from unicodedata import name
from PIL import Image,ImageTk
from colorama import Style
import pymysql
import cv2
import os
import csv
from tkinter import filedialog


global_data=[]

class attendance_details():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Attendance Details")


        #variables
        self.time=StringVar()
        self.date=StringVar()
        self.enr=StringVar()
        self.name=StringVar()
        self.status=StringVar()



        

        #main_frame
        main_frame=Label(self.root,width=878, height=722, bd=2, relief=RIDGE, bg='#EEF9FF')
        main_frame.place(x=0, y=0, width=1920, height=1080)

        #title
        my_label = Label(main_frame, text="Attendance Details", font=("Quicksand",36,"bold"), bg='#EEF9FF', fg="#05A6F0")
        my_label.place(x=673,y=83)



        combostyle = ttk.Style()

        combostyle.theme_create('combostyle', parent='alt',settings = {'TCombobox':{'configure':{'selectbackground': 'grey','fieldbackground': 'white','background': 'white'}}})
        # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
        combostyle.theme_use('combostyle') 



        #   l           lllllllll   lllllllll   lllllllllllllllll
        #   l           l           l                   l
        #   l           l           l                   l
        #   l           llll        llll                l
        #   l           l           l                   l
        #   l           l           l                   l
        #   llllllll    lllllllll   l                   l



        #left_frame
        left_frame=LabelFrame(main_frame,width=878, height=722, bd=2, relief=RIDGE, bg='white')
        left_frame.place(x=40, y=236, width=878, height=722)


        #student information
        student_info_frame=LabelFrame(left_frame, bd=2, width=832, height=343, relief=RIDGE, text="Student Information", font=("times new roman",16,"bold", "italic"), bg='white')
        student_info_frame.place(x=23, y=24, width=832, height=325)

        #input values

        #1. Enrollment Number
        enr_num_label=Label(student_info_frame, text="Enrollment Number",font=("times new roman",16),bg='white', fg="red")
        enr_num_label.place(x=18, y=31)
        
        enr_num_label = Entry(student_info_frame, textvariable=self.enr, font=("times new roman",16), width=15)
        enr_num_label.place(x=201, y=31, width=180, height=30)

        #2. Name
        name_label=Label(student_info_frame, text="Name",font=("times new roman",16),bg='white', fg="red")
        name_label.place(x=438, y=31)
        
        name_label = Entry(student_info_frame, textvariable=self.name, font=("times new roman",16), width=15)
        name_label.place(x=601, y=31, width=180, height=30)

        #3. Date
        date_label=Label(student_info_frame, text="Date",font=("times new roman",16),bg='white', fg="red")
        date_label.place(x=18, y=92)
        
        date_label = Entry(student_info_frame, textvariable=self.date, font=("times new roman",16), width=15)
        date_label.place(x=201, y=92, width=180, height=30)

        #4. Time
        time_label=Label(student_info_frame, text="Time",font=("times new roman",16),bg='white', fg="red")
        time_label.place(x=438, y=92)
        
        time_label = Entry(student_info_frame, textvariable=self.time, font=("times new roman",16), width=15)
        time_label.place(x=601, y=92, width=180, height=30)

        #5. Status
        status_label=Label(student_info_frame, text="Status",font=("times new roman",16),bg='white', fg="red")
        status_label.place(x=18, y=153)
        
        status_label = Entry(student_info_frame, textvariable=self.status, font=("times new roman",16), width=15)
        status_label.place(x=201, y=153, width=180, height=30)

        button_frame=LabelFrame(student_info_frame,highlightthickness = 0, bd=0, relief=RIDGE,  bg='white', width = 832, height=151)
        button_frame.place(x=0, y=210, width = 820, height=65)

        #Import button
        import_button=Button(button_frame, command=self.import_csv, text="Import CSV", font=("times new roman",16,"bold"),bg='#F35325', fg="white")
        import_button.place(x=20, y=0, width = 187, height=65)

        #Export button
        Export_button=Button(button_frame, command=self.export_csv, text="Export CSV", font=("times new roman",16,"bold"),bg='#FFBA08', fg="white")
        Export_button.place(x=221, y=0, width = 187, height=65)

        #Update button
        Update_button=Button(button_frame, command=self.get_value, text="Update Data", font=("times new roman",16,"bold"),bg='#05A6F0', fg="white")
        Update_button.place(x=421, y=0, width = 187, height=65)

        #Reset button
        Reset_button=Button(button_frame, command=self.reset, text="Reset Data",  font=("times new roman",16,"bold"),bg='#81BC06', fg="white")
        Reset_button.place(x=622, y=0, width = 187, height=65)


        hand_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/hand.png")
        hand_icon=hand_icon.resize((832,349),Image.ANTIALIAS)
        self.hand_icon=ImageTk.PhotoImage(hand_icon)
        
        hand_img=Label(left_frame,image=self.hand_icon,)
        hand_img.place(x=23,y=370,width=832,height=349)



        #   lllllll    l    lllllllll   l       l   llllllllllllll
        #   l     l    l    l           l       l         l                   
        #   l     l    l    l           l       l         l     
        #   lllllll    l    l   lllll   lllllllll         l    
        #   lll        l    l       l   l       l         l
        #   l  ll      l    l       l   l       l         l
        #   l    ll    l    lllllllll   l       l         l






        #right_frame
        right_frame=LabelFrame(main_frame,bd=2, relief=RIDGE,bg='white', width=878, height=722)
        right_frame.place(x=930, y=236, width=878, height=722)


        table_frame=Frame(right_frame, bd=2, relief=RIDGE, width=832, height=579)
        table_frame.place(x=23, y=20, width=832, height=678)

        scrollx = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        scrolly = ttk.Scrollbar(table_frame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        

        self.details_table=ttk.Treeview(table_frame,column=("Enrollment number", "Name", "Date", "Time", "Status"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        
        scrollx.config(command=self.details_table.xview) 
        scrolly.config(command=self.details_table.yview)

        

        self.details_table.heading("Enrollment number",text="Enrollment number")
        self.details_table.heading("Name",text="Name")
        self.details_table.heading("Date",text="Date")
        self.details_table.heading("Time",text="Time")
        self.details_table.heading("Status",text="Status")

        self.details_table["show"]="headings"

        self.details_table.pack(fill=BOTH,expand=1)

        self.details_table.bind("<ButtonRelease>",self.get_value)



    def get_data(self,rows):
        self.details_table.delete(*self.details_table.get_children())
        for i in rows:
            self.details_table.insert("",END,values=i)

    def import_csv(self):
        global global_data
        global_data.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open records",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(file_name) as my_file:
            read_csv=csv.reader(my_file,delimiter=",")
            for i in read_csv:
                global_data.append(i)

            self.get_data(global_data)

    def export_csv(self):
        try:
            if len(global_data)<1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save records",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as my_file:
                write_csv=csv.writer(my_file,delimiter=",")
                for i in global_data:
                    write_csv.writerow(i)
                messagebox.showinfo("Export", "Your data exported to "+os.path.basename(file_name)+" successfully", parent=self.root)


        except EXCEPTION as es:
            messagebox.showerror("Error",f"Error occured due to:{str(es)}", parent=self.root)


    def get_value(self,event=""):
        data_row=self.details_table.focus()
        content=self.details_table.item(data_row)
        row_data=content['values']
        self.enr.set(row_data[0])
        self.name.set(row_data[1])
        self.date.set(row_data[2])
        self.time.set(row_data[3])
        self.status.set(row_data[4])

    def reset(self):
        self.enr.set("")
        self.name.set("")
        self.date.set("")
        self.time.set("")
        self.status.set("")









if __name__ == "__main__":
        root=Tk()
        object1=attendance_details(root)
        
        root.mainloop()