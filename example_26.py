
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

def get_img_path():
	global img_index
	img_path = filedialog.askopenfilename(title="open image", filetype=(("Image file", "*.png;*.jpg;*.jpeg"), ("All file", "*")))
	img_path = os.path.normpath(img_path)
	print("img path = ", img_path)
	folder_path = os.path.dirname(img_path)
	for i in os.listdir(folder_path):
		# print(i)
		if i.endswith((".png", ".jpg", ".jpeg")):
			# print(i)
			full_path = os.path.join(folder_path, i)
			print(full_path)
			images_path.append(full_path)

	img_index = images_path.index(img_path)
	print("Image index = ", img_index)
	# image_label.config(text=f"{images_path[img_index]}")
	show_image()

	btn_state()


def btn_state():
	print("Image index = ", img_index)
	if img_index == 0:
		btn_prev.config(state='disabled')
	else:
		btn_prev.config(state='normal')

	if img_index == len(images_path) - 1:
		btn_next.config(state='disabled')
	else:
		btn_next.config(state='normal')

def next_img():
	global img_index
	if img_index < len(images_path):
		img_index += 1
		# image_label.config(text=f"{images_path[img_index]}")
		show_image()
		btn_state()

def prev_img():
	global img_index
	if img_index > 0:
		img_index -= 1
		# image_label.config(text=f"{images_path[img_index]}")
		show_image()
		btn_state()

def show_image():
	global img_index #, photo
	img = Image.open(images_path[img_index])
	img.thumbnail((900, 600))
	photo = ImageTk.PhotoImage(img)
	image_label.imgtk = photo # global photo မရေးလို့ ရ 
	image_label.config(image=photo)



root = tk.Tk()
root.title("ဓာတ်ပုံ")
root.geometry("900x650")
root.minsize(900, 650)
images_path = []
img_index = 0

image_label = tk.Label(root, bg="gray")
image_label.pack(expand=True, fill="both", padx=3)

frame = tk.Frame(root)
frame.pack(side="bottom", pady=10)

btn_open = tk.Button(frame, text="Open Image", width=15, command=get_img_path, )
btn_open.grid(row=0, column=0, padx=5)

btn_prev = tk.Button(frame, text="Previous", width=15, state="disabled", command=prev_img)
btn_prev.grid(row=0, column=1, padx=5)

btn_next = tk.Button(frame, text="Next", width=15, state="disabled", command=next_img)
btn_next.grid(row=0, column=2, padx=5)

root.mainloop()