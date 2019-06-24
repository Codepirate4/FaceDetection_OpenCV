import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('C:\\Users\\hp\\Desktop\\imageprocessing\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h )in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
        roi_color = frame[y:y + h, x:x + w]
        img_item = "myFace.png"
        cv2.imwrite(img_item, roi_color)

        color = (255, 0, 0)  # BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)



    cv2.imshow('FRAME',frame)

    k= cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
