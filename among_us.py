from itertools import cycle
from tkinter import *
from PIL import ImageTk, Image

counter = -1
num = 0
running = False


def counter_label(label):
	def count():
		if running:
			global counter
			if counter == -1:
				display = "Starting..."
			else:
				display = str(counter)
			label['text'] = display
			label.after(1000, count)
			counter += 1
	count()


def Start(label):
	global running
	running = True
	counter_label(label)
	start['state'] = 'disabled'
	stop['state'] = 'normal'
	reset['state'] = 'normal'


def Stop():
	global running
	start['state'] = 'normal'
	stop['state'] = 'disabled'
	reset['state'] = 'normal'
	running = False


def Reset(label):
	global counter
	counter = -1
	if not running:
		reset['state'] = 'disabled'
		label['text'] = 'Stopwatch'
	else:
		label['text'] = 'Starting...'


def next_img():
	img = ImageTk.PhotoImage(Image.open(next(imgs)).resize((1080, 608), Image.ANTIALIAS))
	maps_label.img = img
	maps_label["image"] = img


root = Tk()
root.title("Among Us Helper")


stopwatch = Frame(root)
stopwatch.grid(row=0, column=0, padx=20, pady=50)
stopwatch_label = Label(stopwatch, text="Stopwatch", fg="black", font="Verdana 30 bold")
stopwatch_label.pack()
start = Button(stopwatch, text='Start', width=15, command=lambda: Start(stopwatch_label))
start.pack()
stop = Button(stopwatch, text='Stop', width=15, state='disabled', command=Stop)
stop.pack()
reset = Button(stopwatch, text='Reset', width=15, state='disabled', command=lambda: Reset(stopwatch_label))
reset.pack()

checkboxes = Frame(root)
checkboxes.grid(row=1, column=0, padx=20)
checkboxes_label = Label(checkboxes, text="Sus/Inno List", fg="black", font="Verdana 30 bold")
checkboxes_label.pack()
black = Checkbutton(checkboxes, text="black")
black.pack()
blue = Checkbutton(checkboxes, text="blue")
blue.pack()
brown = Checkbutton(checkboxes, text="brown")
brown.pack()
cyan = Checkbutton(checkboxes, text="cyan")
cyan.pack()
green = Checkbutton(checkboxes, text="green")
green.pack()
lime = Checkbutton(checkboxes, text="lime")
lime.pack()
orange = Checkbutton(checkboxes, text="orange")
orange.pack()
pink = Checkbutton(checkboxes, text="pink")
pink.pack()
purple = Checkbutton(checkboxes, text="purple")
purple.pack()
red = Checkbutton(checkboxes, text="red")
red.pack()
white = Checkbutton(checkboxes, text="white")
white.pack()
yellow = Checkbutton(checkboxes, text="yellow")
yellow.pack()

imgs = ["Polus.jpg", "The Skeld.jpg"]  # "Mira HQ".jpg
imgs = cycle(imgs)
maps = Frame(root)
maps.grid(row=0, column=1, rowspan=2, padx=50, pady=50)
maps_label = Label(maps, text="Map", fg="black", font="Verdana 30 bold")
maps_label.pack()
btn = Button(maps, text="Change map", command=next_img)
btn.pack(pady=20)
next_img()

root.mainloop()
