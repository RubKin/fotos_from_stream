import cv2
import os
import time


video = cv2.VideoCapture(0)

facedetect=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count= 0

name = input("which Images would you like to create?... ")
quantity = int(input("how many Images would you like?..."))

time.sleep(2)

dirname = f'images/{name}' 
try:
    os.makedirs(dirname, exist_ok=True)
except OSError:
    pass

time.sleep(1)

while True:
    ret, frame = video.read()
    faces=facedetect.detectMultiScale(frame,1.3, 4.5)
    
    
    for x,y,w,h in faces:
        time.sleep(0.1)
        count=count+1

        imgname = dirname +'/'+ name +str(count) + '.jpg'
        print("Creating Images........." +imgname)

        cv2.imwrite(os.path.join(imgname), frame[y:y+h,x:x+w])
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    
    cv2.imshow('frame', frame)

    if count>quantity:
        break   

    if cv2.waitKey(1) & 0xFF == ord('q'):   
        break

print("Images have been saved in your directory")

video.release()
cv2.destroyAllWindows()