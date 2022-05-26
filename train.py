from re import L
from tkinter import*
from tkinter import messagebox
from PIL import Image
import cv2
import os
import numpy as np

class train_data:

    def train_classify(self):
        data_dir=("face_data")
        path = [ os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            img_np=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(img_np)
            ids.append(id)
            cv2.imshow("Training",img_np)
            cv2.waitKey(1)==13

        ids=np.array(ids)


        #Train the classifier

        classf=cv2.face.LBPHFaceRecognizer_create()
        classf.train(faces,ids)
        classf.write("Classifier_data.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Success","Training dataset completed")





if __name__ == "__main__":
    root=Tk()
    object1=train_data(root)

    root.configure(bg='white') 
    root.mainloop()