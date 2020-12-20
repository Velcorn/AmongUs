from itertools import cycle
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

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
def change_map():
	img = ImageTk.PhotoImage(Image.open(next(imgs)).resize((1280, 720), Image.ANTIALIAS))
	maps_label.img = img
	maps_label["image"] = img


# Untick all checkboxes.
def reset_cbs():
	var1.set(False)
	var2.set(False)
	var3.set(False)
	var4.set(False)
	var5.set(False)
	var6.set(False)
	var7.set(False)
	var8.set(False)
	var9.set(False)
	var10.set(False)
	var11.set(False)
	var12.set(False)
	var13.set(False)
	var14.set(False)
	var15.set(False)
	var16.set(False)
	var17.set(False)
	var18.set(False)
	var19.set(False)
	var20.set(False)
	var21.set(False)
	var22.set(False)
	var23.set(False)
	var24.set(False)


# Create root window.
root = tk.Tk()
root.title("Among Us Helper")
root.configure(bg="#424242")
style = ThemedStyle(root)
style.set_theme("black")
'''root.bind("<Button-3>", next_img)
root.bind("<Button-2>", reset_cbs)'''
for row in range(3):
	root.grid_rowconfigure(row, weight=1)
for col in range(3):
	root.grid_columnconfigure(col, weight=1)

# Create stopwatch frame and buttons.
stopwatch = ttk.Frame(root)
stopwatch.grid(row=0, column=0, sticky="ew", columnspan=2)
stopwatch_label = ttk.Label(stopwatch, text="Stopwatch", font="Arial 20 bold")
stopwatch_label.pack()
start = ttk.Button(stopwatch, text='Start', width=15, command=lambda: Start(stopwatch_label))
start.pack()
stop = ttk.Button(stopwatch, text='Stop', width=15, state='disabled', command=Stop)
stop.pack()
reset = ttk.Button(stopwatch, text='Reset', width=15, state='disabled', command=lambda: Reset(stopwatch_label))
reset.pack()

# Create variables for the checkboxes.
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()
var5 = tk.BooleanVar()
var6 = tk.BooleanVar()
var7 = tk.BooleanVar()
var8 = tk.BooleanVar()
var9 = tk.BooleanVar()
var10 = tk.BooleanVar()
var11 = tk.BooleanVar()
var12 = tk.BooleanVar()
var13 = tk.BooleanVar()
var14 = tk.BooleanVar()
var15 = tk.BooleanVar()
var16 = tk.BooleanVar()
var17 = tk.BooleanVar()
var18 = tk.BooleanVar()
var19 = tk.BooleanVar()
var20 = tk.BooleanVar()
var21 = tk.BooleanVar()
var22 = tk.BooleanVar()
var23 = tk.BooleanVar()
var24 = tk.BooleanVar()

# Create suslist frame and checkboxes.
suslist = ttk.Frame(root)
suslist.grid(row=1, column=0, padx=30, sticky="ew")
suslist_label = ttk.Label(suslist, text="Sus", font="Arial 20 bold")
suslist_label.pack()
black = ttk.Checkbutton(suslist, text="black", variable=var1)
black.pack(anchor="w")
blue = ttk.Checkbutton(suslist, text="blue", variable=var2)
blue.pack(anchor="w")
brown = ttk.Checkbutton(suslist, text="brown", variable=var3)
brown.pack(anchor="w")
cyan = ttk.Checkbutton(suslist, text="cyan", variable=var4)
cyan.pack(anchor="w")
green = ttk.Checkbutton(suslist, text="green", variable=var5)
green.pack(anchor="w")
lime = ttk.Checkbutton(suslist, text="lime", variable=var6)
lime.pack(anchor="w")
orange = ttk.Checkbutton(suslist, text="orange", variable=var7)
orange.pack(anchor="w")
pink = ttk.Checkbutton(suslist, text="pink", variable=var8)
pink.pack(anchor="w")
purple = ttk.Checkbutton(suslist, text="purple", variable=var9)
purple.pack(anchor="w")
red = ttk.Checkbutton(suslist, text="red", variable=var10)
red.pack(anchor="w")
white = ttk.Checkbutton(suslist, text="white", variable=var11)
white.pack(anchor="w")
yellow = ttk.Checkbutton(suslist, text="yellow", variable=var12)
yellow.pack(anchor="w")

# Create innolist and checkboxes
innolist = ttk.Frame(root)
innolist.grid(row=1, column=1, padx=30, sticky="ew")
innolist_label = ttk.Label(innolist, text="Inno", font="Arial 20 bold")
innolist_label.pack()
black2 = ttk.Checkbutton(innolist, text="black", variable=var13)
black2.pack(anchor="w")
blue2 = ttk.Checkbutton(innolist, text="blue", variable=var14)
blue2.pack(anchor="w")
brown2 = ttk.Checkbutton(innolist, text="brown", variable=var15)
brown2.pack(anchor="w")
cyan2 = ttk.Checkbutton(innolist, text="cyan", variable=var16)
cyan2.pack(anchor="w")
green2 = ttk.Checkbutton(innolist, text="green", variable=var17)
green2.pack(anchor="w")
lime2 = ttk.Checkbutton(innolist, text="lime", variable=var18)
lime2.pack(anchor="w")
orange2 = ttk.Checkbutton(innolist, text="orange", variable=var19)
orange2.pack(anchor="w")
pink2 = ttk.Checkbutton(innolist, text="pink", variable=var20)
pink2.pack(anchor="w")
purple2 = ttk.Checkbutton(innolist, text="purple", variable=var21)
purple2.pack(anchor="w")
red2 = ttk.Checkbutton(innolist, text="red", variable=var22)
red2.pack(anchor="w")
white2 = ttk.Checkbutton(innolist, text="white", variable=var23)
white2.pack(anchor="w")
yellow2 = ttk.Checkbutton(innolist, text="yellow", variable=var24)
yellow2.pack(anchor="w")

# Create maps frame.
imgs = ["Polus.jpg", "The Skeld.jpg"]  # "Mira HQ.jpg",
imgs = cycle(imgs)
maps = ttk.Frame(root)
maps.grid(row=0, column=2, rowspan=3, sticky="ew")
maps_label = ttk.Label(maps)
maps_label.pack()
change_map()

# Create reset and change map button.
button_zone = ttk.Frame(root)
button_zone.grid(row=2, column=0, columnspan=2)
reset_button = ttk.Button(button_zone, text="Reset Lists", width=15, command=reset_cbs)
reset_button.pack()
map_button = ttk.Button(button_zone, text="Change Map", width=15, command=change_map)
map_button.pack()

root.mainloop()
