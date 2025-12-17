
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox

def open_camera():
    global cap, camera_state
    if not camera_state:
        camera_state = True
        cap = cv2.VideoCapture(0)
        print(camera_state, cap)

        get_camera_frame()

def get_camera_frame():
    if camera_state and cap.isOpened():
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(img)

        camera_label.imgtk = img_tk
        camera_label.config(image=img_tk)

        window.after(15, get_camera_frame)

def close_camera():
    global camera_state, cap
    if camera_state:
        camera_state = False
        cap.release()
        cap = None
        camera_label.imgtk = no_image_tk
        camera_label.config(image=no_image_tk)


def take_photo():
    if camera_state and cap.isOpened():
        _, frame = cap.read()
        cv2.imwrite("my_camera_photo.jpg", frame)
        messagebox.showinfo("my camera", "successful to take photo....")

window = tk.Tk()
window.title("Simple Camera App")

cap = None
camera_state = False
frame_width, frame_height = 640, 480

no_img = Image.open("no_camera.png").resize((frame_width, frame_height))
no_image_tk = ImageTk.PhotoImage(no_img)

camera_label = tk.Label(window, image=no_image_tk)
camera_label.pack(pady=5)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Open Camera", width=20, command=open_camera).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Close Camera", width=20, command=close_camera).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="take photo", width=20, command=take_photo).grid(row=0, column=2, padx=10)

window.mainloop()



















'''
# import cv2
# import tkinter as tk
# from PIL import Image, ImageTk
# from tkinter import messagebox

# def open_camera():
#     global running, cap
#     if not running:
#         cap = cv2.VideoCapture(1)
#         print("open camera")
#         running = True
#         update_frame()


# def update_frame():
#     if running and cap.isOpened():
#         ret, frame = cap.read()
#         # print(f"ret = {ret}, frame = {frame.shape}, runnig = {running}")
#         if ret:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = Image.fromarray(frame)
#             imgtk = ImageTk.PhotoImage(img)
#             camera_label.imgtk = imgtk
#             camera_label.config(image=imgtk)

#             camera_label.after(15,update_frame)
#         else:
#             camera_label.imgtk = no_image_tk
#             camera_label.config(image=no_image_tk)   

# def close_camera():
#     global cap, running
#     if running:
#         running = False
#         print(running)
#         cap.release()
#         camera_label.imgtk = no_image_tk
#         camera_label.config(image=no_image_tk)

# def take_photo():
#     if not running:
#         return
#     ret, frame =cap.read()
#     if not ret:
#         return
#     cv2.imwrite('test_1.jpg', frame)
#     messagebox.showinfo("Saved", f"Snapshot saved....")

# #============== ui ================
# window = tk.Tk()
# window.title("Simple Camera App")

# running = False
# cap = None
# frame_width, frame_height = 640, 480

# no_img = Image.open("no_camera.png").resize((frame_width, frame_height))
# no_image_tk = ImageTk.PhotoImage(no_img)

# camera_label = tk.Label(window, image=no_image_tk)
# camera_label.pack(pady=5)

# btn_frame = tk.Frame(window)
# btn_frame.pack(pady=10)

# tk.Button(btn_frame, text="Open Camera", width=20, command=open_camera).grid(row=0, column=0, padx=10)
# tk.Button(btn_frame, text="Close Camera", width=20, command=close_camera).grid(row=0, column=1, padx=10)
# tk.Button(btn_frame, text="take photo", width=20, command=take_photo).grid(row=0, column=2, padx=10)

# window.mainloop()

'''