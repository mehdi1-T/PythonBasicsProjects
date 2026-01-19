from tkinter import *
import time

root = Tk()
root.geometry("500x500")
root.config(bg="#662D91")

def update_time():
    current_time = time.strftime("%H:%M:%S")
    lbl.config(text=current_time)
    root.after(1000, update_time)  #

lbl = Label(
    root,
    bg="#662D91",
    fg="white",
    font=("Impact", 35, "bold")
)
lbl.pack(expand=True)


if __name__ == "__main__":
    update_time()
    root.mainloop()