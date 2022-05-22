from cProfile import label
from ctypes import alignment
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from colorama import Style

class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("")
        self.root.title("Attendance Management System")

        Grid.columnconfigure(root,0,weight=1)

        Grid.rowconfigure(root,1,weight=0)
        Grid.rowconfigure(root,2,weight=3)
        Grid.rowconfigure(root,3,weight=3)
        Grid.rowconfigure(root,4,weight=0)
        Grid.columnconfigure(root,1,weight=1)
        Grid.columnconfigure(root,2,weight=1)
        
        #title
        my_label = Label(text="Attendance Management System", font=("times new roman",36,"bold", "italic"), bg='white', fg="red")
        my_label.grid(row=1, columnspan=3, ipadx=30, ipady=30, sticky="EW")
        #my_label.pack(side="top")

        

        #student button
        student_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/student icon.png")
        student_icon=student_icon.resize((300,200),Image.ANTIALIAS)
        self.photo_student_icon=ImageTk.PhotoImage(student_icon)
        
        student_button=Button(image=self.photo_student_icon,highlightthickness = 0, bd = 0, text="Student Details", font=("times new roman",24,"bold"),  bg="white", fg="darkblue",compound="top",cursor="hand2")
        student_button.place(x=200,y=200,width=80,height=70)
        student_button.grid(row=2,column=0,padx=20, pady=20, sticky="NSEW")

        #detect face button
        face_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/face icon.jpg")
        face_icon=face_icon.resize((300,200),Image.ANTIALIAS)
        self.photo_face_icon=ImageTk.PhotoImage(face_icon)
        
        face_button=Button(image=self.photo_face_icon,highlightthickness = 0, bd = 0,text="Detect Face",font=("times new roman",24,"bold"),bg='white', fg="darkblue",compound="top",cursor="hand2")
        face_button.place(x=200,y=200,width=80,height=70)
        face_button.grid(row=2,column=1,padx=20, pady=20, sticky="NSEW")

        #attendance button
        attendance_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/attendance icon.png")
        attendance_icon=attendance_icon.resize((300,200),Image.ANTIALIAS)
        self.photo_attendance_icon=ImageTk.PhotoImage(attendance_icon)
        
        attendance_button=Button(image=self.photo_attendance_icon,highlightthickness = 0, bd = 0,text="Attendance Details",font=("times new roman",24,"bold"),bg='white', fg="darkblue",compound="top",cursor="hand2")
        attendance_button.place(x=200,y=200,width=80,height=70)
        attendance_button.grid(row=2,column=2,padx=20, pady=20, sticky="NSEW")

        #train data button
        train_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/train icon.jpg")
        train_icon=train_icon.resize((300,200),Image.ANTIALIAS)
        self.photo_train_icon=ImageTk.PhotoImage(train_icon)
        
        train_button=Button(image=self.photo_train_icon,highlightthickness = 0, bd = 0,text="Train Data",font=("times new roman",24,"bold"),bg='white', fg="darkblue",compound="top",cursor="hand2")
        train_button.place(x=200,y=200,width=80,height=70)
        train_button.grid(row=3,column=0,padx=20, pady=20, sticky="NSEW")

        #help button
        help_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/help icon.jpg")
        help_icon=help_icon.resize((300,200),Image.ANTIALIAS)
        self.photo_help_icon=ImageTk.PhotoImage(help_icon)
        
        help_button=Button(image=self.photo_help_icon,highlightthickness = 0, bd = 0,text="Help",font=("times new roman",24,"bold"), bg='white',fg="darkblue",compound="top",cursor="hand2")
        help_button.place(x=200,y=200,width=80,height=70)
        help_button.grid(row=3,column=1,padx=20, pady=20, sticky="NSEW")

        #exit button
        exit_icon=Image.open("/home/sky/Attendance Management Using Face Recognition/Images/exit icon.png")
        exit_icon=exit_icon.resize((300,200),Image.ANTIALIAS)
        self.photo_exit_icon=ImageTk.PhotoImage(exit_icon)
        
        exit_button=Button(image=self.photo_exit_icon,highlightthickness = 0, bd = 0,text="Exit",font=("times new roman",24,"bold"), bg='white',fg="darkblue",compound="top",cursor="hand2")
        exit_button.place(x=200,y=200,width=80,height=70)
        exit_button.grid(row=3,column=2,padx=20, pady=20, sticky="NSEW")

        my_endlabel = Label(text="Microsoft Engage", font=("times new roman",24,"bold", "italic"),bg='white', fg="red")
        my_endlabel.grid(row=4, columnspan=3, ipadx=20, ipady=20, sticky="NSE")
        

if __name__ == "__main__":
    root=Tk()
    object1=face_recognition(root)

    root.configure(bg='white') 
    #root.style = ttk.Style(root)
    #root.style.configure('TButton',font=("times new roman",24,"bold"))
    root.mainloop()