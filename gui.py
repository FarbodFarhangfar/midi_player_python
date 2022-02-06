import tkinter as tk

screen = tk.Tk()



screen.configure(background='grey')
b = tk.Button(screen, activebackground='white', text='hello there ', width=20, height=20, command=new_window)
b.pack()

screen.mainloop()
