import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk


cap = None
detect_corners = False

def start_camera():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(3, 960) 
    cap.set(4, 480)  
    update_frame()

def stop_camera():
    global cap
    if cap:
        cap.release()
    cap = None
    canvas.delete("all")

def toggle_corner_detection():
    global detect_corners
    detect_corners = not detect_corners

def update_frame():
    global cap
    if cap and cap.isOpened():
        ret, frame = cap.read()
        if ret:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if detect_corners:
                corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
                if corners is not None:
                    corners = np.int8(corners)
                    for corner in corners:
                        x, y = corner.ravel()
                        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img_tk = ImageTk.PhotoImage(image=img)
            canvas.create_image(0, 0, anchor=NW, image=img_tk)
            canvas.img_tk = img_tk  # Referansı sakla
            

        root.after(10, update_frame)

root = Tk()
root.title("Köşe Algılama Uygulaması")


canvas = Canvas(root, width=960, height=480)
canvas.pack()


btn_start = Button(root, text="Kamerayı Başlat", command=start_camera)
btn_start.pack(side=LEFT, padx=10, pady=10)

btn_stop = Button(root, text="Kamerayı Durdur", command=stop_camera)
btn_stop.pack(side=LEFT, padx=10, pady=10)

btn_toggle_corners = Button(root, text="Köşe Algılamayı Aç/Kapat", command=toggle_corner_detection)
btn_toggle_corners.pack(side=LEFT, padx=10, pady=10)


root.mainloop()


if cap:
    cap.release()
cv2.destroyAllWindows()