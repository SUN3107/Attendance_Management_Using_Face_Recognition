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

class student_details:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Student Details")


        #variables
        self.dept=StringVar()
        self.year=StringVar()
        self.degree=StringVar()
        self.semester=StringVar()
        self.enr=StringVar()
        self.name=StringVar()
        self.sbatch=StringVar()
        self.mail=StringVar()

        self.photo=StringVar()


        

        #main_frame
        main_frame=Label(width=878, height=722, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=0, y=0, width=1920, height=1080)

        #title
        my_label = Label(main_frame, text="Student Details", font=("Quicksand",36,"bold"), bg='white', fg="#05A6F0")
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


        #course information
        current_course_frame=LabelFrame(left_frame, width=832, height=194 ,bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman",16,"bold", "italic"), bg='white')
        current_course_frame.place(x=23, y=24, width=832, height=194)

        #input values
        #1. Department
        department_label=Label(current_course_frame, text="Department",font=("times new roman",16),bg='white', fg="red")
        department_label.place(x=18, y=31)
        
        department_input = ttk.Combobox(current_course_frame, textvariable=self.dept, font=("times new roman",16), width=15, state="readonly")
        department_input["values"]=("Select Department","C.S.E.","C.E.","M.E.","E.C.E.","Architecture","M.N.C.")
        department_input.current(0)
        department_input.place(x=201, y=31, width=193, height=30)

        #2. Degree
        Degree_label=Label(current_course_frame, text="Degree",font=("times new roman",16),bg='white', fg="red")
        Degree_label.place(x=438, y=31)
        
        Degree_label = ttk.Combobox(current_course_frame,textvariable=self.degree,font=("times new roman",16), width=15,  state="readonly", background='white')
        Degree_label["values"]=("Select Degree","B.Tech","M.Tech","PhD")
        Degree_label.current(0)
        Degree_label.place(x=601, y=31, width=193, height=30)

        #3. Year
        year_label=Label(current_course_frame, text="Year",font=("times new roman",16),bg='white', fg="red")
        year_label.place(x=18, y=103)
        
        year_label = ttk.Combobox(current_course_frame,textvariable=self.year, font=("times new roman",16), width=15,  state="readonly")
        year_label["values"]=("Select Year","First year","Second year","Third year","Fourth year","Fifth year")
        year_label.current(0)
        year_label.place(x=201, y=103, width=193, height=30)

        #4. Semester
        sem_label=Label(current_course_frame,  text="Semester",font=("times new roman",16),bg='white', fg="red")
        sem_label.place(x=438, y=103)
        
        sem_label = ttk.Combobox(current_course_frame,textvariable=self.semester, font=("times new roman",16), width=15, state="readonly")
        sem_label["values"]=("Select Semester","Autumn Semester","Spring Semester")
        sem_label.current(0)
        sem_label.place(x=601, y=103, width=193, height=30)





        #class information
        class_frame=LabelFrame(left_frame, bd=2, width=832, height=281, relief=RIDGE, text="Class Information", font=("times new roman",16,"bold", "italic"), bg='white')
        class_frame.place(x=23, y=244, width=832, height=281)

        #input values

        #1. Enrollment Number
        enr_num_label=Label(class_frame, text="Enrollment Number",font=("times new roman",16),bg='white', fg="red")
        enr_num_label.place(x=18, y=31)
        
        enr_num_label = Entry(class_frame, textvariable=self.enr,font=("times new roman",16), width=15)
        enr_num_label.place(x=201, y=31, width=180, height=30)

        #2. Name
        name_label=Label(class_frame,  text="Name",font=("times new roman",16),bg='white', fg="red")
        name_label.place(x=438, y=31)
        
        name_label = Entry(class_frame,textvariable=self.name, font=("times new roman",16), width=15)
        name_label.place(x=601, y=31, width=180, height=30)

        #3. Sub-Batch
        sub_batch_label=Label(class_frame,  text="Sub-Batch",font=("times new roman",16),bg='white', fg="red")
        sub_batch_label.place(x=18, y=92)
        
        sub_batch_label = Entry(class_frame,textvariable=self.sbatch,font=("times new roman",16), width=15)
        sub_batch_label.place(x=201, y=92, width=180, height=30)

        #4. Year
        year_label=Label(class_frame, text="Year",font=("times new roman",16),bg='white', fg="red")
        year_label.place(x=438, y=92)
        
        year_label = Entry(class_frame, textvariable=self.year, font=("times new roman",16), width=15)
        year_label.place(x=601, y=92, width=180, height=30)

        #5. Semester
        sem_label=Label(class_frame, text="Semester",font=("times new roman",16),bg='white', fg="red")
        sem_label.place(x=18, y=153)
        
        sem_label = Entry(class_frame,textvariable=self.semester, font=("times new roman",16), width=15)
        sem_label.place(x=201, y=153, width=180, height=30)

        #6. E-Mail
        mail_label=Label(class_frame, text="E-Mail",font=("times new roman",16),bg='white', fg="red")
        mail_label.place(x=438, y=153)
        
        mail_label = Entry(class_frame,textvariable=self.mail, font=("times new roman",16), width=15)
        mail_label.place(x=601, y=153, width=180, height=30)

        


        #Radio-Buttons
        photo_button=Radiobutton(class_frame, variable=self.photo,text="Take Sample Photo",value="Yes")
        photo_button.place(x=38, y=215)

        no_photo_button=Radiobutton(class_frame, variable=self.photo,text="No Sample Photo",value="No")
        no_photo_button.place(x=284, y=215)



        button_frame=LabelFrame(left_frame,highlightthickness = 0, bd=0, relief=RIDGE,  bg='white', width = 832, height=151)
        button_frame.place(x=23, y=547, width = 832, height=151)

        #Save button
        save_button=Button(button_frame, command=self.enter_value, text="Save Data", font=("times new roman",16,"bold"),bg='#F35325', fg="white")
        save_button.place(x=0, y=0, width = 187, height=65)

        #Update button
        Update_button=Button(button_frame, command=self.update, text="Update Data", font=("times new roman",16,"bold"),bg='#05A6F0', fg="white")
        Update_button.place(x=215, y=0, width = 187, height=65)

        #Delete button
        Delete_button=Button(button_frame, command=self.delete_value, text="Delete Data", font=("times new roman",16,"bold"),bg='#FFBA08', fg="white")
        Delete_button.place(x=430, y=0, width = 187, height=65)

        #Reset button
        Reset_button=Button(button_frame, text="Reset Data", command=self.reset_value, font=("times new roman",16,"bold"),bg='#81BC06', fg="white")
        Reset_button.place(x=645, y=0, width = 187, height=65)

        #Take Photo button
        photo_button=Button(button_frame, command=self.generate_dataset, text="Take Sample Photo", font=("times new roman",16,"bold"),bg='#001C8E', fg="white")
        photo_button.place(x=0, y=86, width = 402, height=65)

        #Update Photo button
        update_photo_button=Button(button_frame, text="Update Sample Photo", font=("times new roman",16,"bold"),bg='#001C8E', fg="white")
        update_photo_button.place(x=430, y=86, width = 402, height=65)



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

        #search
        search_frame=LabelFrame(right_frame, width=832, height=84, bd=2, relief=RIDGE, text="Search", font=("times new roman",16,"bold", "italic"), bg='white', fg="red")
        search_frame.place(x=23, y=24, width=832, height=84)

        #search criteria
        search_label=Label(search_frame, text="Search Criteria",font=("times new roman",16),bg='white', fg="red")
        search_label.place(x=22, y=10)
        
        search_label = ttk.Combobox(search_frame,font=("times new roman",16), width=15,  state="readonly", background='white')
        search_label["values"]=("Select Criteria","Enrollment number","Name","Sub-Batch")
        search_label.current(0)
        search_label.place(x=215, y=10, width=162, height=30)

        entry_label = Entry(search_frame,font=("times new roman",16), width=15)
        entry_label.place(x=390, y=10, width=162, height=30)

        search_button=Button(search_frame, text="Search", font=("times new roman",16),bg='#001C8E', fg="white")
        search_button.place(x=565, y=10, width=118, height=30)

        show_all_button=Button(search_frame, text="Show All", font=("times new roman",16),bg='#001C8E', fg="white")
        show_all_button.place(x=703, y=10, width=118, height=30)


        table_frame=Frame(right_frame, bd=2, relief=RIDGE, width=832, height=579)
        table_frame.place(x=23, y=119, width=832, height=579)

        scrollx = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        scrolly = ttk.Scrollbar(table_frame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        

        self.details_table=ttk.Treeview(table_frame,column=("Enrollment number", "Name", "Degree", "Department", "Year", "Semester", "Sub-Batch", "E-mail"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        
        scrollx.config(command=self.details_table.xview) 
        scrolly.config(command=self.details_table.yview)

        

        self.details_table.heading("Enrollment number",text="Enrollment number")
        self.details_table.heading("Name",text="Name")
        self.details_table.heading("Degree",text="Degree")
        self.details_table.heading("Department",text="Department")
        self.details_table.heading("Year",text="Year")
        self.details_table.heading("Semester",text="Semester")
        self.details_table.heading("Sub-Batch",text="Sub-Batch")
        self.details_table.heading("E-mail",text="E-mail")

        self.details_table["show"]="headings"

        self.details_table.pack(fill=BOTH,expand=1)

        self.details_table.bind("<ButtonRelease>",self.to_update)

        self.get_value() 



        #   ############    ##        #
        #   #               # #       #
        #   #               #  #      #
        #   #######         #   #     #
        #   #               #    #    #
        #   #               #     #   #
        #   #               #      #  #
        #   #               #       # #
        #   #               #        ##


    def enter_value(self):
        if self.dept.get()=="Select Department" or self.year.get()=="Select Year" or self.degree.get()=="Select Degree" or self.semester.get()=="Select Semester" or self.enr.get()=="" or self.name.get()=="" or self.sbatch.get()=="" or self.mail.get()=="":
            messagebox.showerror("ERROR","Input in All Fields Required")
        else:
            try:
                connection = pymysql.connect(host="localhost",user="root",passwd="Surnidhi@99",database="face_recognition")
                cursor = connection.cursor()

                cursor.execute('INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                                                                        (self.enr.get(),
                                                                                        self.name.get(),
                                                                                        self.degree.get(),
                                                                                        self.dept.get(),
                                                                                        self.year.get(),
                                                                                        self.semester.get(),
                                                                                        self.sbatch.get(),
                                                                                        self.mail.get(),
                                                                                        self.photo.get()))

                connection.commit()
                self.get_value()
                connection.close()

                messagebox.showinfo("Success","Details added successfully", parent=self.root)

            except EXCEPTION as es:
                messagebox.showerror("Error",f"Error occured due to:{str(es)}", parent=self.root)


    def get_value(self):
        connection = pymysql.connect(host="localhost",user="root",passwd="Surnidhi@99",database="face_recognition")
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM student')
        data=cursor.fetchall()

        if len(data)!=0:
            self.details_table.delete(*self.details_table.get_children())
            for i in data:
                self.details_table.insert("",END,values=i)
            
            connection.commit()
        
        connection.close()


    def to_update(self,event=""):
        user_focus=self.details_table.focus()
        entered_data=self.details_table.item(user_focus)
        data=entered_data["values"]

        self.enr.set(data[0])
        self.name.set(data[1])
        self.degree.set(data[2])
        self.dept.set(data[3])
        self.year.set(data[4])
        self.semester.set(data[5])
        self.sbatch.set(data[6])
        self.mail.set(data[7])
        self.photo.set(data[8])

    def update(self):
        if self.dept.get()=="Select Department" or self.year.get()=="Select Year" or self.degree.get()=="Select Degree" or self.semester.get()=="Select Semester" or self.enr.get()=="" or self.name.get()=="" or self.sbatch.get()=="" or self.mail.get()=="":
            messagebox.showerror("ERROR","Input in All Fields Required")
        else:
            try:
                tryupdate=messagebox.askyesno("Update","Update Data?", parent=self.root)
                if tryupdate>0:
                    connection = pymysql.connect(host="localhost",user="root",passwd="Surnidhi@99",database="face_recognition")
                    cursor = connection.cursor()

                    cursor.execute('UPDATE student SET name=%s, degree=%s, department=%s, year=%s, semester=%s, subbatch=%s, mail=%s, photo=%s where enr_no=%s',(
                                                                                                                                                                self.name.get(),
                                                                                                                                                                self.degree.get(),
                                                                                                                                                                self.dept.get(),
                                                                                                                                                                self.year.get(),
                                                                                                                                                                self.semester.get(),
                                                                                                                                                                self.sbatch.get(),
                                                                                                                                                                self.mail.get(),
                                                                                                                                                                self.photo.get(),
                                                                                                                                                                self.enr.get()))

                else:
                    if not tryupdate:
                        return

                messagebox.showinfo("Success","Update Successful", parent=self.root)

                connection.commit()
                self.get_value()
                connection.close()

            except EXCEPTION as es:
                messagebox.showerror("Error",f"Error occured due to:{str(es)}", parent=self.root)


    def delete_value(self):
        if self.enr.get()=="":
            messagebox.showerror("Error","No data found", parent=self.root)

        else:
                try:
                    trydelete=messagebox.askyesno("Delete","Delete Data?", parent=self.root)
                    if trydelete>0:
                        connection = pymysql.connect(host="localhost",user="root",passwd="Surnidhi@99",database="face_recognition")
                        cursor = connection.cursor()

                        cursor.execute('DELETE FROM student WHERE enr_no=%s',self.enr.get())
                        

                    else:
                        if not trydelete:
                            return

                    messagebox.showinfo("Success","Delete Successful", parent=self.root)

                    connection.commit()
                    self.get_value()
                    connection.close()

                except EXCEPTION as es:
                    messagebox.showerror("Error",f"Error occured due to:{str(es)}", parent=self.root)




    def reset_value(self):
        self.enr.set("")
        self.name.set("")
        self.degree.set("Select Degree")
        self.dept.set("Select Department")
        self.year.set("Select Year")
        self.semester.set("Select Semester")
        self.sbatch.set("")
        self.mail.set("")
        self.photo.set("")



    def generate_dataset(self):
        if self.dept.get()=="Select Department" or self.year.get()=="Select Year" or self.degree.get()=="Select Degree" or self.semester.get()=="Select Semester" or self.enr.get()=="" or self.name.get()=="" or self.sbatch.get()=="" or self.mail.get()=="":
            messagebox.showerror("ERROR","Input in All Fields Required")
        else:
            try:
                connection = pymysql.connect(host="localhost",user="root",passwd="Surnidhi@99",database="face_recognition")
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM student')
                data=cursor.fetchall()
                id=0
                for i in data:
                    id+=1

                cursor.execute('UPDATE student SET name=%s, degree=%s, department=%s, year=%s, semester=%s, subbatch=%s, mail=%s, photo=%s where enr_no=%s',(
                                                                                                                                                                self.name.get(),
                                                                                                                                                                self.degree.get(),
                                                                                                                                                                self.dept.get(),
                                                                                                                                                                self.year.get(),
                                                                                                                                                                self.semester.get(),
                                                                                                                                                                self.sbatch.get(),
                                                                                                                                                                self.mail.get(),
                                                                                                                                                                self.photo.get(),
                                                                                                                                                                self.enr.get()==id+1))
                connection.commit()
                self.get_value()
                self.reset_value()
                connection.close()

                face_classification=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cr(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    #scaling factor=1.3
                    #minimum neighbour=5
                    faces=face_classification.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cr=img[y:y+h,x:x+w]
                        return face_cr


                cam_capture=cv2.VideoCapture(0)
                image_id=0
                while True:
                    return_back,img_frame=cam_capture.read()
                    if face_cr(img_frame) is not None:
                        image_id+=1
                    face_var=cv2.resize(face_cr(img_frame),(600,600))
                    face_var=cv2.cvtColor(face_var,cv2.COLOR_BGR2GRAY)
                    file_path="face_data/user."+str(id)+"."+str(image_id)+".jpg"
                    cv2.imwrite(file_path,face_var)
                    cv2.putText(face_var,str(image_id),(100,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,255),2)
                    cv2.imshow("Face",face_var)

                    if cv2.waitKey(1)==13 or int(image_id)==250:
                        break

                cam_capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success","Data set generated", parent=self.root)

            except EXCEPTION as es:
                    messagebox.showerror("Error",f"Error occured due to:{str(es)}", parent=self.root)

            

            





 


if __name__ == "__main__":
        root=Tk()
        object1=student_details(root)
        

        root.configure(bg='white') 
        root.mainloop()