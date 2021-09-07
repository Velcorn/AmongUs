from itertools import cycle
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle
import tkinter as tk
import tkinter.ttk as ttk

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


if __name__ == '__main__':
	# Create root window.
	root = tk.Tk()
	root.title("Among Us Helper")
	root.configure(bg="#424242")
	style = ThemedStyle(root)
	style.set_theme("black")
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

	# Create notepad boxes.
	notepad1 = ttk.Frame(root)
	notepad1.grid(row=2, column=0, columnspan=2)
	notepad1_label = ttk.Label(notepad1, text="Sus", font="Arial 20 bold")
	notepad1_label.pack()
	notes = tk.Text(notepad1, height=15, width=25, bg="#424242", fg="#ffffff", padx=10)
	notes.pack()

	notepad2 = ttk.Frame(root)
	notepad2.grid(row=3, column=0, columnspan=2)
	notepad2_label = ttk.Label(notepad2, text="Inno", font="Arial 20 bold")
	notepad2_label.pack()
	notes = tk.Text(notepad2, height=15, width=25, bg="#424242", fg="#ffffff", padx=10)
	notes.pack()

	# Create maps frame and change button.
	imgs = ["Polus.jpg", "The Skeld.jpg", "Mira HQ.jpg"]
	imgs = cycle(imgs)
	maps = ttk.Frame(root)
	maps.grid(row=0, column=2, rowspan=4, sticky="ew")
	maps_label = ttk.Label(maps)
	maps_label.pack()
	change_map()

	# Create reset and change map button.
	rb_zone = ttk.Frame(root)
	rb_zone.grid(row=4, column=0, columnspan=2, pady=10)

	cmb_zone = ttk.Frame(root)
	cmb_zone.grid(row=4, column=2, pady=10)
	map_button = ttk.Button(cmb_zone, text="Change Map", width=15, command=change_map)
	map_button.pack()

	root.mainloop()
