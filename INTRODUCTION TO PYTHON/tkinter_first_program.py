from tkinter import Tk,Label,Message

ventana = Tk()
ventana.title("Bienvenidos a tkinter")
lbl = Label(ventana, text="Un mensaje:", font=("Arial Bold", 36)).pack(side="left")
msg = Message(ventana, text="""Whatever you do will be insignificant, but it is very
important that you do it.\n(Mahatma Gandhi)""", font=("Times", 24))
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
ventana.mainloop()