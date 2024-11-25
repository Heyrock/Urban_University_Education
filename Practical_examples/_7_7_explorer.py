import tkinter
import os
from tkinter import filedialog


def file_select():
    # путь до искомого файла
    filename = filedialog.askopenfilename(
        # корень диска C:
        # initialdir='/',
        initialdir=r'C:\Users\Ром\Documents\Urban_1',
        title='Выберите файл',
        filetypes=(
            ('Текстовый файл','.txt'),
            ('Все файлы', '*')
        ),
    )
    # изменить текст лэйбла
    text['text'] = text['text'] + ' ' + filename
    # запустить найденный файл
    os.startfile(filename)



window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.resizable(
    width=False,
    height=False
)
window.configure(bg='black')

# надпись
text = tkinter.Label(
    window,
    text='Файл: ',
    height='5',
    width='65',
    background='silver',
    foreground='blue',
)
text.grid(column=1, row=1)

# кнопка
button_select = tkinter.Button(
    window,
    text='Выбрать файл',
    height=3,
    width=20,
    background='silver',
    foreground='blue',
    command=file_select,
)
button_select.grid(
    column=1,
    row=2,
    pady=5,
)

window.mainloop()