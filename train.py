from cProfile import label
from ctypes import alignment
from json.tool import main
from re import L
from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image,ImageTk
from colorama import Style

class train_data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Train Data")


        #title
        my_label = Label(text="Train Data", font=("times new roman",36,"bold", "italic"), bg='white', fg="red")
        my_label.place(x=473,y=83)

        train_button=Button(self.root,highlightthickness = 0, bd = 0,text="Train Data",font=("Quicksand",16,"bold"),bg='white', fg="darkblue",compound="top",cursor="hand2")
        train_button.place(x=845,y=623,width=238,height=281)



    def train_classify(self):
        



if __name__ == "__main__":
    root=Tk()
    object1=train_data(root)

    root.configure(bg='white') 
    root.mainloop()