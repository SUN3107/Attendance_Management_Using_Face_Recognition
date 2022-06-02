from platform import release
from re import L
from tkinter import*
from tkinter import messagebox
from unicodedata import name
from PIL import Image
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np
import pymysql

class face_recog:

    def mark_attendance(self, n, j):
        with open("attendance.csv","r+",newline="\n") as f:
            my_data=f.readlines()
            name_list=[]
            n1 = 0
            for line in my_data:
                enter=line.split((","))
                name_list.append(enter[0])
                if(n):
                    n1+=1

            if((n not in name_list) and (j not in name_list)):
                now=datetime.now()
                that_date=now.strftime("%d/%m/%Y")
                time_string=now.strftime("%H:%M")
                f.writelines(f"\n{j},{n},{that_date},{time_string},Arrived")
            if(n1==2):
                now=datetime.now()
                that_date=now.strftime("%d/%m/%Y")
                time_string=now.strftime("%H:%M")
                f.writelines(f"\n{j},{n},{that_date},{time_string},Left")



    def face_recogi(self):
        def boundary(img,classifier,scaleFactor,minNeighbors,color,text,classf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            feature=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)

            coordinates=[]

            for(x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=classf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                connection = pymysql.connect(host="localhost",user="root",
                                                passwd="Surnidhi@99",database="face_recognition")
                cursor = connection.cursor()

                cursor.execute("SELECT name from student where enr_no="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("SELECT enr_no from student where enr_no="+str(id))
                j=cursor.fetchone()
                j="+".join(j)

                if confidence>75:
                    cv2.putText(img,f"Enrollment number:{j}",(x,y-40),cv2.FONT_HERSHEY_PLAIN,0.8,(0,255,0),2)
                    cv2.putText(img,f"Name:{n}",(x,y-20),cv2.FONT_HERSHEY_PLAIN,0.8,(0,255,0),2)
                    self.mark_attendance(n,j)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown person",(x,y-55),cv2.FONT_HERSHEY_PLAIN,0.8,(0,0,255),2)

                coordinates=[x,y,w,h] 

            return coordinates


        def recog(img,classf,face_cascade):
            coordinates=boundary(img,face_cascade,1.1,10,(255,255,255),"Face",classf)
            return img
        
        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        classf=cv2.face.LBPHFaceRecognizer_create()
        classf.read("Classifier_data.xml")

        video_capture=cv2.VideoCapture(0)

        while True:
            ret,img=video_capture.read()
            img=recog(img,classf,face_cascade)
            cv2.imshow("Face",img)

            if cv2.waitKey(1)==13:
                break

        video_capture,release()
        cv2.destroyAllWindows() 

        





if __name__ == "__main__":
    root=Tk()
    object1=face_recog(root)

    root.configure(bg='white') 
    root.mainloop()