from tkinter import *


def click():
    if a.get != '':
        lbl['text'] = f'Здравствуйте, {a.get()}'


root = Tk()
root.geometry('700x700')
root.title('Приветствие')
root.resizable(False, False)
canvas_width, canvas_height = 600, 600
canvas = Canvas(root, width=canvas_width - 100, height=canvas_height - 100)
canvas.pack()
lbl = Label(root, text='Введите ваше имя', font=('Consolas', 15), fg='black', bg='cyan')
lbl.place(relx=0.36, rely=0.25)
a = Entry(root, width=35, fg='black', bg='gray', font='Consolas')
a.place(relx=0.27, rely=0.3)
button = Button(root, text='Нажмите', width=20, font='Consolas', fg='black', bg='red', command=click)
button.place(relx=0.36, rely=0.35)
root.mainloop()
