import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_result(value):
    reply_entry.delete(first=0, last='end')
    reply_entry.insert(index=0, string=value)


def add():
    num1, num2 = get_values()
    res = str(num1 + num2)
    insert_result(res)


def sub():
    num1, num2 = get_values()
    res = str(num1 - num2)
    insert_result(res)


def mul():
    num1, num2 = get_values()
    res = str(num1 * num2)
    insert_result(res)


def div():
    num1, num2 = get_values()
    res = str(num1 / num2)
    insert_result(res)


window = tk.Tk()
window.title('Калькуляртр')
window.geometry('350x350')
window.resizable(width=False, height=False)

button_add = tk.Button(
    window,
    text='+',
    width=2,
    height=2,
    command=add,
)
button_sub = tk.Button(
    window,
    text='-',
    width=2,
    height=2,
    command=sub,
)
button_mul = tk.Button(
    window,
    text='*',
    width=2,
    height=2,
    command=mul,
)
button_div = tk.Button(
    window,
    text='/',
    width=2,
    height=2,
    command=div,
)
button_add.place(x=100, y=200)
button_sub.place(x=125, y=200)
button_mul.place(x=100, y=250)
button_div.place(x=125, y=250)

number1_entry = tk.Entry(window, width=25)
number2_entry = tk.Entry(window, width=25)
reply_entry = tk.Entry(window, width=25)
number1_entry.place(x=100, y=75)
number2_entry.place(x=100, y=125)
reply_entry.place(x=100, y=175)

number1 = tk.Label(
    window,
    text='Введите первое число:'
)
number1.place(x=100, y=50)

number2 = tk.Label(
    window,
    text='Введите второе число:'
)
number2.place(x=100, y=100)

reply = tk.Label(
    window,
    text='Ответ:'
)
reply.place(x=100, y=150)

window.mainloop()
