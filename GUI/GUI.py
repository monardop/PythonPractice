import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.lSide = tk.Label(self, text="Today", bg="gray", width=30)
        self.lSide.pack()

        self.new_task = tk.Button(self, text="New task", padx=10, pady= 5, bg="navy")
        self.new_task.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    myapp = App(root)
    myapp.master.title("To Do App")
    myapp.mainloop()