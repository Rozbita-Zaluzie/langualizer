from tkinter import *
from tkinterdnd2 import *
from list import *

def path_listbox(event):
    print(event.data)
    make_list(event.data)
    

window = TkinterDnD.Tk()
window.title('Delftstack')
window.geometry('400x800')
window.config(bg='#0D1117', padx=10, pady=10)
frame = Frame(window)
frame.pack()

label = Label(frame, text='Drop files here', pady=1,)
label.pack()

listbox = Listbox(
    frame,
    width=50,
    height=10,
    selectmode=SINGLE,
    background='grey',
    )
listbox.pack(fill=X, side=LEFT)



listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', path_listbox)



window.mainloop()


