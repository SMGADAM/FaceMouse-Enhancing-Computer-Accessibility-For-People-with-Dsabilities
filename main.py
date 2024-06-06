import tkinter as tk;
import movements
import time
import threading
import speechRec
from PIL import ImageTk, Image
import os


def track(x) :
    time.sleep(0.5)
    thread_a = threading.Thread(target=movements.startTracking)
    thread_b = threading.Thread(target=speechRec.Listen)
    thread_b.start()
    thread_a.start()


window = tk.Tk('Genova App')

 
back = tk.Frame(master=window,bg='black')
back.pack()
back = tk.Frame(master=window,bg='#333')
back.pack(fill=tk.BOTH, expand=1)

def margin(x,y):
    return (
        tk.Label(
            text= '',
            bg='#333',
            pady= y,
            padx= x,
            master=back
        ).pack()
    )
 
def text(text , x ,y ):
    T = tk.Label(
        master=back,
        text=text,
        fg='white',
        bg='#333',
        font=x
        
    )
    T.pack()

img = ImageTk.PhotoImage(Image.open("l.png"))
panel = tk.Label(
    master=back,
    background='#333',
    image = img
    )
panel.pack()

button = tk.Button(
    master=back,
    borderwidth=0,
    text="Start Traking",
    width=10,
    padx=40,
    font='105px',
    pady=2,
    bg="#444",
    fg="#fff",
)

button.bind('<Button-1>', track)


button.config(font=("Cairo", 20))
button.pack()

margin(0,5)

# text('For better experience please rest your laptop on a desk ',('20px'),1)

margin(0,10)

developedBy = tk.Label(
    master=back,
    text='GenuTeens ©',
    fg='white',
    bg='#333',    
)
developedBy.pack()

window.resizable(0,0)
window.minsize(600,400)
window.mainloop()
