import tkinter as tk

root = tk.Tk()
root.title("Always on top")
root.geometry("600x400+50-90")
root.resizable(0,0)
root.attributes("-topmost",1)

root.mainloop()
