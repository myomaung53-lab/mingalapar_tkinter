
import tkinter as tk

def my_draw():
	a = tk.Toplevel()
	a.title("add figure")
	a.geometry("320x160+0+0")

	f1 = tk.Frame(a,)
	f1.pack(pady=3)
	tk.Label(f1, text='x1').pack(side='left', padx=2)
	x1_entry = tk.Entry(f1, )
	x1_entry.pack(side='left', padx=2)
	tk.Label(f1, text='y1').pack(side='left', padx=2)
	y1_entry = tk.Entry(f1, )
	y1_entry.pack(side='left', padx=2)

	f2 = tk.Frame(a,)
	f2.pack(pady=3)
	tk.Label(f2, text='x2').pack(side='left', padx=2)
	x2_entry = tk.Entry(f2, )
	x2_entry.pack(side='left', padx=2)
	tk.Label(f2, text='y2').pack(side='left', padx=2)
	y2_entry = tk.Entry(f2, )
	y2_entry.pack(side='left', padx=2)

	f3 = tk.Frame(a,)
	f3.pack(pady=3)
	tk.Radiobutton(f3, text='Oval', width=10, anchor='w', variable=r_var, value=1).pack(pady=2)
	tk.Radiobutton(f3, text='Rectangle', width=10, anchor='w', variable=r_var, value=2).pack(pady=2)

	def my_draw_2():
		ans = r_var.get()
		x_start = int(x1_entry.get())
		y_start = int(y1_entry.get())
		x_end = int(x2_entry.get())
		y_end = int(y2_entry.get())
		if ans == 1:
			c.create_oval(x_start, y_start, x_end, y_end, outline='red')
		elif ans == 2:
			c.create_rectangle(x_start, y_start, x_end, y_end, outline='blue')

	tk.Button(a, text="ပုံဆွဲပါ ", width=10, command=my_draw_2).pack(pady=3)

window = tk.Tk()
window.geometry('820x570+0+0')
window.title("My drawing App")
r_var = tk.IntVar()
r_var.set(2)

c = tk.Canvas(window, width=800, height=500, bg='white')
c.pack(pady=3)

tk.Button(window, text="ပုံများထည့်ရန်", command=my_draw).pack(pady=5)

window.mainloop()









































'''
import tkinter as tk
def my_gometry_shape():
	fig = tk.Toplevel()
	fig.title("add figure")
	fig.geometry('320x160')
	f1 = tk.Frame(fig)
	f1.pack(pady=3)
	tk.Label(f1, text='x1').pack(side='left', padx=3)
	e1 = tk.Entry(f1, )
	e1.pack(side='left', padx=3)
	tk.Label(f1, text='y1').pack(side='left', padx=3)
	e2 = tk.Entry(f1, )
	e2.pack(side='left', padx=3)

	f2= tk.Frame(fig)
	f2.pack(pady=3)
	tk.Label(f2, text='x2').pack(side='left', padx=3)
	e3 = tk.Entry(f2, )
	e3.pack(side='left', padx=3)
	tk.Label(f2, text='y2').pack(side='left', padx=3)
	e4 = tk.Entry(f2, )
	e4.pack(side='left', padx=3)

	f3 = tk.Frame(fig)
	f3.pack(pady=3), 
	tk.Radiobutton(f3, text='Oval', width=10, anchor='w', variable=r_var, value=1).pack(pady=2)
	tk.Radiobutton(f3, text='Rectangle', width=10,anchor='w', variable=r_var, value=2).pack(pady=2)

	def my_draw():
		ans = r_var.get()
		x_start = int(e1.get())
		y_start = int(e2.get())
		x_end = int(e3.get())
		y_end = int(e4.get())
		if ans == 1:
			c.create_oval(x_start, y_start, x_end, y_end, width=3, outline='red')
		elif ans == 2:
			c.create_rectangle(x_start, y_start, x_end, y_end, width=3, outline='red', fill='lightblue')
		fig.destroy()
	tk.Button(fig, text='ပုံဆွဲပါ..', width=10, command=my_draw).pack(pady=3)
	

def my_pos(event):
	l1.config(text=f"x = {event.x}, y = {event.y}")

window = tk.Tk()
window.geometry('820x570+0+0')
window.title("My drawing App")
r_var = tk.IntVar()
r_var.set(1)
c = tk.Canvas(window, width=800, height=500, bg='white')
c.pack(pady=3)

tk.Button(window, text="ပုံများထည့်ရန်", command=my_gometry_shape).pack(pady=5)
l1 = tk.Label(window)
l1.pack(pady=3, fill='x')

c.bind("<Motion>", my_pos)

window.mainloop()
'''

