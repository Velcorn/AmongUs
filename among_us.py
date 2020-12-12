from itertools import cycle
from PIL import ImageTk, Image
import tkinter as tk

# Set the counter and running state/bool.
counter = 0
running = False


# Set the stopwatch time.
def counter_label(label):
	def count():
		if running:
			global counter
			display = str(counter)
			label['text'] = display
			label.after(1000, count)
			counter += 1
	count()


# Start the counter.
def Start(label):
	global running
	running = True
	counter_label(label)
	start['state'] = 'disabled'
	stop['state'] = 'normal'
	reset['state'] = 'normal'


# Stop the counter.
def Stop():
	global running
	start['state'] = 'normal'
	stop['state'] = 'disabled'
	reset['state'] = 'normal'
	running = False


# Reset the counter.
def Reset(label):
	global counter
	counter = 1
	if not running:
		reset['state'] = 'disabled'
		label['text'] = 'Stopwatch'
	else:
		label['text'] = '0'


# Display next image.
def next_img(event):
	img = ImageTk.PhotoImage(Image.open(next(imgs)).resize((1280, 720), Image.ANTIALIAS))
	maps_label.img = img
	maps_label["image"] = img


# Create root window.
root = tk.Tk()
root.title("Among Us Helper")
for row in range(2):
	root.grid_rowconfigure(row, weight=1)
for col in range(2):
	root.grid_columnconfigure(col, weight=1)

# Create stopwatch frame and buttons.
stopwatch = tk.Frame(root)
stopwatch.grid(row=0, column=0, sticky="ew", columnspan=2)
stopwatch_label = tk.Label(stopwatch, text="Stopwatch", font="Arial 20 bold")
stopwatch_label.pack()
start = tk.Button(stopwatch, text='Start', width=15, command=lambda: Start(stopwatch_label))
start.pack()
stop = tk.Button(stopwatch, text='Stop', width=15, state='disabled', command=Stop)
stop.pack()
reset = tk.Button(stopwatch, text='Reset', width=15, state='disabled', command=lambda: Reset(stopwatch_label))
reset.pack()


# Create suslist frame and checkboxes.
suslist = tk.Frame(root)
suslist.grid(row=1, column=0, padx=30, sticky="ew")
suslist_label = tk.Label(suslist, text="Sus", font="Arial 20 bold")
suslist_label.pack()
black = tk.Checkbutton(suslist, text="black")
black.pack(anchor="w")
blue = tk.Checkbutton(suslist, text="blue")
blue.pack(anchor="w")
brown = tk.Checkbutton(suslist, text="brown")
brown.pack(anchor="w")
cyan = tk.Checkbutton(suslist, text="cyan")
cyan.pack(anchor="w")
green = tk.Checkbutton(suslist, text="green")
green.pack(anchor="w")
lime = tk.Checkbutton(suslist, text="lime")
lime.pack(anchor="w")
orange = tk.Checkbutton(suslist, text="orange")
orange.pack(anchor="w")
pink = tk.Checkbutton(suslist, text="pink")
pink.pack(anchor="w")
purple = tk.Checkbutton(suslist, text="purple")
purple.pack(anchor="w")
red = tk.Checkbutton(suslist, text="red")
red.pack(anchor="w")
white = tk.Checkbutton(suslist, text="white")
white.pack(anchor="w")
yellow = tk.Checkbutton(suslist, text="yellow")
yellow.pack(anchor="w")

# Create innolist and checkboxes
innolist = tk.Frame(root)
innolist.grid(row=1, column=1, padx=30, sticky="ew")
innolist_label = tk.Label(innolist, text="Inno", font="Arial 20 bold")
innolist_label.pack()
black2 = tk.Checkbutton(innolist, text="black")
black2.pack(anchor="w")
blue2 = tk.Checkbutton(innolist, text="blue")
blue2.pack(anchor="w")
brown2 = tk.Checkbutton(innolist, text="brown")
brown2.pack(anchor="w")
cyan2 = tk.Checkbutton(innolist, text="cyan")
cyan2.pack(anchor="w")
green2 = tk.Checkbutton(innolist, text="green")
green2.pack(anchor="w")
lime2 = tk.Checkbutton(innolist, text="lime")
lime2.pack(anchor="w")
orange2 = tk.Checkbutton(innolist, text="orange")
orange2.pack(anchor="w")
pink2 = tk.Checkbutton(innolist, text="pink")
pink2.pack(anchor="w")
purple2 = tk.Checkbutton(innolist, text="purple")
purple2.pack(anchor="w")
red2 = tk.Checkbutton(innolist, text="red")
red2.pack(anchor="w")
white2 = tk.Checkbutton(innolist, text="white")
white2.pack(anchor="w")
yellow2 = tk.Checkbutton(innolist, text="yellow")
yellow2.pack(anchor="w")


# Create maps frame and change button.
imgs = ["Mira HQ.jpg", "Polus.jpg", "The Skeld.jpg"]
imgs = cycle(imgs)
maps = tk.Frame(root)
maps.grid(row=0, column=2, rowspan=2, sticky="ew")
maps_label = tk.Label(maps)
maps_label.pack()
root.bind("<Button-2>", next_img)
next_img("<Button-2>")

root.mainloop()
