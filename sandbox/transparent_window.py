import tkinter as tk

root = tk.Tk()
root.title("Transparent window")
root.geometry("600x400-50-10")
root.resizable(False,False)
root.attributes('-alpha', 0.5)


root.mainloop()