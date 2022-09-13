from tkinter import *
from tkinterdnd2 import *
from list import *
from PIL import ImageTk, Image



    

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
    )
listbox.pack(fill=X, side=LEFT)





frame1 = Frame(master=window, width=100, height=100, pady=10, bg='#0D1117')
frame1.pack()


def set_list(dict):
    for widget in frame1.winfo_children():
        widget.destroy()
    for key, value in dict.items():
        labell = Label(frame1, text=(key + " : " + str(round(value, 2)) + "%"), pady=1, bg='#0D1117', fg='#FFFFFF')
        labell.pack()


def path_listbox(event):
    print(event.data)
    set_list(make_list(event.data))


listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', path_listbox)



window.mainloop()


