from os import link
from tkinter import *
import tkinter
import webbrowser
from PIL import Image,ImageTk
from colorama import Style
from Student import student_details
from train import train_data
from Face_recognition import face_recog
from attendance import attendance_details

class face_recognition(train_data,face_recog):
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Attendance Management System")

        main_frame=LabelFrame(width=878, height=722, bd=2, relief=RIDGE, bg='#EEF9FF')
        main_frame.place(x=0, y=0, width=1920, height=1080)
        

        #title
        my_label = Label(main_frame, text="Attendance Management System", 
                        font=("Quicksand",36,"bold"), 
                        bg='#EEF9FF', fg="#05A6F0")
        my_label.place(x=473,y=83)

        

        #student button
        student_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/student_icon.png")
        student_icon=student_icon.resize((238,238),Image.ANTIALIAS)
        self.photo_student_icon=ImageTk.PhotoImage(student_icon)
        
        student_button=Button(main_frame,image=self.photo_student_icon, 
                                command=self.student_details, 
                                highlightthickness = 0, bd = 0, 
                                text="Student Details", font=("Quicksand",16,"bold"),  
                                bg="#D1EACD", fg="darkblue",compound="top",cursor="hand2")
        student_button.place(x=845,y=232,width=238,height=281)





        #detect face button
        face_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/face_icon.png")
        face_icon=face_icon.resize((238,238),Image.ANTIALIAS)
        self.photo_face_icon=ImageTk.PhotoImage(face_icon)
        
        face_button=Button(main_frame,
                            command=self.face_recogi,
                            image=self.photo_face_icon,
                            highlightthickness = 0, bd = 0,
                            text="Mark Attendance",font=("Quicksand",16,"bold"),
                            bg='#EAE9CE', fg="darkblue",compound="top",cursor="hand2")
        face_button.place(x=1202,y=232,width=238,height=281)





        #attendance button
        attendance_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/attendance icon.png")
        attendance_icon=attendance_icon.resize((238,238),Image.ANTIALIAS)
        self.photo_attendance_icon=ImageTk.PhotoImage(attendance_icon)
        
        attendance_button=Button(main_frame, 
                                    command=self.att_details, 
                                    image=self.photo_attendance_icon,
                                    highlightthickness = 0, bd = 0,
                                    text="Attendance Details",font=("Quicksand",16,"bold"),
                                    bg="#D1EACD", fg="darkblue",compound="top",cursor="hand2")
        attendance_button.place(x=1559,y=232,width=238,height=281)





        #train data button
        train_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/train_icon.png")
        train_icon=train_icon.resize((220,220),Image.ANTIALIAS)
        self.photo_train_icon=ImageTk.PhotoImage(train_icon)
        
        train_button=Button(main_frame,
                            command=self.train_classify,
                            image=self.photo_train_icon,
                            highlightthickness = 0, bd = 0,
                            text="Train Data",font=("Quicksand",16,"bold"),
                            bg='#EAE9CE', fg="darkblue",compound="top",cursor="hand2")
        train_button.place(x=845,y=623,width=238,height=281)





        #help button
        help_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/help icon.png")
        help_icon=help_icon.resize((220,220),Image.ANTIALIAS)
        self.photo_help_icon=ImageTk.PhotoImage(help_icon)
        
        help_button=Button(main_frame,
                            image=self.photo_help_icon,
                            command=self.help, 
                            highlightthickness = 0, bd = 0,
                            text="Help",font=("Quicksand",16,"bold"), 
                            bg="#D1EACD",fg="darkblue",compound="top",cursor="hand2")
        help_button.place(x=1202,y=623,width=238,height=281)





        #exit button
        exit_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/exit icon.png")
        exit_icon=exit_icon.resize((220,220),Image.ANTIALIAS)
        self.photo_exit_icon=ImageTk.PhotoImage(exit_icon)
        
        exit_button=Button(main_frame,
                            image=self.photo_exit_icon, 
                            command=self.exit, 
                            highlightthickness = 0, bd = 0,
                            text="Exit",font=("quicksand",16,"bold"),
                            bg='#EAE9CE',fg="darkblue",compound="top",cursor="hand2")
        exit_button.place(x=1559,y=623,width=238,height=281)




        #engage label
        engage_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/logo.png")
        engage_icon=engage_icon.resize((76,76),Image.ANTIALIAS)
        self.photo_engage_icon=ImageTk.PhotoImage(engage_icon)
        
        engage_button=Label(main_frame,
                            image=self.photo_engage_icon,
                            highlightthickness = 0, padx=10, bd = 0,
                            text="Microsoft Engage",font=("quicksand",20,"bold"), 
                            bg='#EEF9FF',fg="darkblue",compound="left",cursor="hand2")
        engage_button.pack
        engage_url= 'https://acehacker.com/microsoft/engage2022/'
        engage_button.bind("<Button-1>", lambda e:open_url(engage_url))
        engage_button.place(x=58,y=846,width=395,height=76)
        


        T_app = Text(main_frame, height = 5,
                        font =("Quicksand", 20), 
                        foreground="#001C8E",bg='#EEF9FF', 
                        width = 52,highlightthickness = 0, padx=10,bd = 0)
        T_dev = Text(main_frame, height = 5,
                        font =("Quicksand", 19), 
                        width = 52, bg='#EEF9FF', 
                        highlightthickness = 0, padx=10,bd = 0)
        T_contact = Text(main_frame, height = 5,
                            font =("Quicksand", 19, "bold"), 
                            width = 52, bg='#EEF9FF', 
                            highlightthickness = 0, padx=10,bd = 0)
        
        AppInfo = """Application Details-
    This application has 6 options-
    1. Student details: View Details of students
    2. Mark Attendance: Mark your attendance 
    by showing your face in webcam
    3. Attendance Details: See the attendance 
    details recorded for the day
    4. Train data: Train the dataset
    5. Help: Reach out to dev in case of any 
    problem
    6. Exit: Leave the application"""

        DevInfo="""Developer Information-
    Hello, I am Sunidhi Yadav, currently in 
    B.Tech. C.S.E. at IIT Roorkee. This is 
    my first Python based ML project."""  

        Contact="Contact-"  
               

        T_app.place(x=122,y=232,width=628,height=400)

        T_app.insert('end', AppInfo)

        T_dev.place(x=122,y=600,width=628,height=150)

        T_dev.insert('end', DevInfo)

        T_contact.place(x=157,y=760,width=628,height=60)

        T_contact.insert('end', Contact)



        
        #github 
        github=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/github.png")
        github=github.resize((50,50),Image.ANTIALIAS)
        self.photo_github=ImageTk.PhotoImage(github)

        github_label = Label(main_frame, image=self.photo_github, bg="#EEF9FF", cursor= "hand2")
        github_label.pack
        github_url= 'https://github.com/SUN3107'
        github_label.bind("<Button-1>", lambda e:open_url(github_url))
        github_label.place(x=315,y=750)


        #linkedin 
        linkedin=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/linkedin.png")
        linkedin=linkedin.resize((50,50),Image.ANTIALIAS)
        self.photo_linkedin=ImageTk.PhotoImage(linkedin)

        linkedin_label = Label(main_frame, image=self.photo_linkedin, bg="#EEF9FF", cursor= "hand2")
        linkedin_label.pack
        linkedin_url= 'https://www.linkedin.com/in/sunidhi-yadav-3b7636231/'
        linkedin_label.bind("<Button-1>", lambda e:open_url(linkedin_url))
        linkedin_label.place(x=400,y=750)


    def student_details(self):
        self.new_window=Toplevel(root)
        app=student_details(self.new_window)

    def att_details(self):
        self.new_window=Toplevel(root)
        app=attendance_details(self.new_window)



    def help(self):
        help=tkinter.messagebox.showinfo("Help","You can reach the developer at sunidhiyadav99@gmail.com", 
                                            parent=self.root)

    

    def exit(self):
        exit=tkinter.messagebox.askyesno("Exit","Are you sure?", parent=self.root)

        if exit>0:
            self.root.destroy()
        else:
            return




if __name__ == "__main__":
    root=Tk()
    object1=face_recognition(root)

    def open_url(url):
        webbrowser.open_new_tab(url)

    root.configure(bg='white')
    root.mainloop()
