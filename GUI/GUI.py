import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

if __name__ == "__main__":
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()
