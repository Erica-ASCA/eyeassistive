import tkinter as tk
from tkinter import Frame, ttk, LEFT, RIGHT, TOP, BOTTOM
from camera_movement import convert_to_keypress2
from webcam_classification import generate_predictions
import cv2
import time
from statistics import mode
from threading import Thread

def create_button_list():
    buttons = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0','<-',
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '´',
        'a', 's', 'd', 'f', 'g', 'h', 'j','k', 'l', 'ç','~',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.','^', 'Símbolos',
        'Espaço',
    ]
    return buttons

def keyboard():
    buttons = create_button_list()
    var_row = 2
    var_column = 0

    text_entry = ttk.Entry(keyboard_frame, state="readonly", textvariable=text_var,justify="center", font=("Helvetica", 30))
    text_entry.grid(row = 0, columnspan=80, ipadx=700, ipady=30)

    for button in buttons:
        if button != ("Espaço"):
            key = tk.Button(keyboard_frame, text=button, width=8, highlightthickness=4,
            relief="raised", padx=10, pady=14, bd=11, command=lambda x=button, i=var_row-1, j=var_column: select(x, i, j), font=("Helvetica", 20))
            button_list[var_row-2].append(key)
            key.grid(row = var_row - 1, column = var_column)

        if button == "Espaço":
            key = tk.Button(keyboard_frame, text=button, width=80, highlightthickness=4,
            relief="raised", padx=10, pady=14, bd=11, command=lambda x=button, i=var_row-1, j=var_column: select(x, i, j), font=("Helvetica", 20))
            button_list[var_row-2].append(key)
            key.grid(row = 6, columnspan=10)

        var_column += 1
        if var_column > 10:
            var_column = 0
            var_row += 1
            button_list.append([])

def enterKey(event):
    if current_frame == "Keyboard":
        buttons = create_button_list()
        column, row = selected_button
        position2d = column * 11 + row
        select(buttons[position2d], row, column)

def rightKey(event):
    if current_frame == "Keyboard":
        try:
            if selected_button == [-1, -1]:
                selected_button[:] = [0,0]
                button_list[0][0].configure(highlightbackground='red')
            elif selected_button[0] == 4:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [0,0]
                button_list[0][0].configure(highlightbackground='red')
            else:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [selected_button[0], (selected_button[1]+1)%11]
                button_list[selected_button[0]][selected_button[1]%11].configure(highlightbackground='red')
        except IndexError:
            print("Index Error")
    if current_frame == "Set1":
        show_symbols_set4()
    elif current_frame == "Set2":
        show_selected_symbol(dormir)
    elif current_frame == "Set3":
        show_selected_symbol(escovar)
    elif current_frame == "Set4":
        show_selected_symbol(sim)

def leftKey(event):
    if current_frame == "Keyboard":
        try:
            if selected_button == [-1, -1]:
                selected_button[:] = [0,0]
                button_list[0][0].configure(highlightbackground='red')
            elif selected_button[0] == 4:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [0,10]
                button_list[0][10].configure(highlightbackground='red')
            else:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [selected_button[0], (selected_button[1]-1)%11]
                button_list[selected_button[0]][selected_button[1]%11].configure(highlightbackground='red')
        except IndexError:
            print("Index Error")
    if current_frame == "Set1":
        show_symbols_set3()
    elif current_frame == "Set2":
        show_selected_symbol(divertir)
    elif current_frame == "Set3":
        show_selected_symbol(banheiro)
    elif current_frame == "Set4":
        show_selected_symbol(nao)

def downKey(event):
    if current_frame == "Keyboard":

        try:
            if selected_button == [-1, -1]:
                selected_button[:] = [0,0]
                button_list[0][0].configure(highlightbackground='red')
            elif selected_button[0] == 3:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [(selected_button[0]+1)%5, 0]
                button_list[0][0].configure(highlightbackground='red')
            elif selected_button[0] == 4:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [(selected_button[0]-1)%5, 5]
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='red')
            else:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [(selected_button[0]+1)%5, selected_button[1]]
                button_list[selected_button[0]][selected_button[1]%11].configure(highlightbackground='red')
        except IndexError:
            print("Index Error")

    if current_frame == "Set1":
        change_to_keyboard()
    if current_frame == "Set2":
        show_symbols_set1()
    if current_frame == "Set3":
        show_symbols_set1()
    if current_frame == "Set4":
        show_symbols_set1()
    if current_frame == "Selected_Symbol1":
        show_symbols_set2()
    elif current_frame == "Selected_Symbol2":
        show_symbols_set3()
    elif current_frame == "Selected_Symbol3":
        show_symbols_set4()

def backKey(event):
    if current_frame == "Keyboard":
        select("<-", 0, 0)
    if current_frame == "Set1":
        change_to_keyboard()
    if current_frame == "Set2":
        show_symbols_set1()
    if current_frame == "Set3":
        show_symbols_set1()
    if current_frame == "Set4":
        show_symbols_set1()
    if current_frame == "Selected_Symbol1":
        show_symbols_set2()
    if current_frame == "Selected_Symbol2":
        show_symbols_set3()
    if current_frame == "Selected_Symbol3":
        show_symbols_set4()

def upKey(event):
    if current_frame == "Keyboard":
        try:
            if selected_button == [-1, -1]:
                selected_button[:] = [0,0]
                button_list[0][0].configure(highlightbackground='red')
            elif selected_button[0] == 0:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [(selected_button[0]-1)%5, 0]
                button_list[selected_button[0]][selected_button[1]%11].configure(highlightbackground='red')
            elif selected_button[0] == 4:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [(selected_button[0]+1)%5, 5]
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='red')
            else:
                button_list[selected_button[0]][selected_button[1]].configure(highlightbackground='#d9d9d9')
                selected_button[:] = [(selected_button[0]-1)%5, selected_button[1]]
                button_list[selected_button[0]][selected_button[1]%11].configure(highlightbackground='red')
        except IndexError:
            print("Index Error")
    if current_frame == "Set1":
        show_symbols_set2()
    elif current_frame == "Set2":
        show_selected_symbol(comer)
    elif current_frame == "Set3":
        show_selected_symbol(banho)
    elif current_frame == "Set4":
        show_selected_symbol(naosei)

def select(value, x , y):
    global exp
    if value == "<-":
        exp = exp[:-1]
        text_var.set(exp)

    elif value == "Espaço":
        exp += " "
        text_var.set(exp)

    elif value == "Símbolos":
        change_to_symbols()

    else:
        exp += value
        text_var.set(exp)

def start_keyboard():
    keyboard()

def change_to_keyboard():
    global current_frame
    global keyboard_started
    current_frame = "Keyboard"
    if keyboard_started == False:
        start_keyboard()
        keyboard_started = True
    keyboard_frame.place(relx=0.5, rely=0.5, anchor="c")
    symbol_frame.place_forget()

def change_to_symbols():
    global current_frame
    current_frame = "Set1"
    symbol_frame.place(relx=0.5, rely=0.5, anchor="c")
    keyboard_frame.place_forget()

def clear_symbol_frame():
    try:
        for widget in symbol_frame.winfo_children():
            widget.destroy()
    except AttributeError:
        pass
    
def show_symbols_set1():
    global current_frame
    current_frame = "Set1"
    clear_symbol_frame()
    set1= Frame(symbol_frame, background="white")
    set1.pack()
    buttonUp = tk.Button(set1, text = "Up (Eat/Drink/Sleep)", image=set2_img, command=show_symbols_set2)
    buttonUp.pack(side=TOP)
    buttonDown = tk.Button(set1, text = "Down (Keyboard)", image=teclado, background="white",command=change_to_keyboard)
    buttonDown.pack(side=BOTTOM)
    buttonLeft = tk.Button(set1, text = "Left (Toilet/Bath/Something)", image=set1_img, command=show_symbols_set3)
    buttonLeft.pack(side=LEFT)
    buttonRight = tk.Button(set1, text = "Right(Something/Something/Something)", image=set3_img, command=show_symbols_set4)
    buttonRight.pack(side=RIGHT)

def show_symbols_set2():
    global current_frame
    current_frame = "Set2"
    clear_symbol_frame()
    set2= Frame(symbol_frame, background="white")
    set2.pack()
    buttonUp = tk.Button(set2, image=comer, background="white", command=lambda: show_selected_symbol(comer))
    buttonUp.pack(side=TOP)
    buttonDown = tk.Button(set2, image=voltar, background="white", command=show_symbols_set1)
    buttonDown.pack(side=BOTTOM)
    buttonLeft = tk.Button(set2, image=divertir, background="white", command=lambda: show_selected_symbol(divertir))
    buttonLeft.pack(side=LEFT)
    buttonRight = tk.Button(set2, image=dormir, background="white", command=lambda: show_selected_symbol(dormir))
    buttonRight.pack(side=RIGHT)

def show_symbols_set3():
    global current_frame
    current_frame = "Set3"
    clear_symbol_frame()
    set3= Frame(symbol_frame, background="white")
    set3.pack()
    buttonUp = tk.Button(set3, image=banho, background="white", command=lambda: show_selected_symbol(banho))
    buttonUp.pack(side=TOP)
    buttonDown = tk.Button(set3, image=voltar, background="white", command=show_symbols_set1)
    buttonDown.pack(side=BOTTOM)
    buttonLeft = tk.Button(set3, image=banheiro, background="white", command=lambda: show_selected_symbol(banheiro))
    buttonLeft.pack(side=LEFT)
    buttonRight = tk.Button(set3, image=escovar, background="white", command=lambda: show_selected_symbol(escovar))
    buttonRight.pack(side=RIGHT)

def show_symbols_set4():
    global current_frame
    current_frame = "Set4"
    clear_symbol_frame()
    set4= Frame(symbol_frame, background="white")
    set4.pack()
    buttonUp = tk.Button(set4, image=naosei, background="white", command=lambda: show_selected_symbol(naosei))
    buttonUp.pack(side=TOP)
    buttonDown = tk.Button(set4, image=voltar, background="white", command=show_symbols_set1)
    buttonDown.pack(side=BOTTOM)
    buttonLeft = tk.Button(set4, image=nao, background="white", command=lambda: show_selected_symbol(nao))
    buttonLeft.pack(side=LEFT)
    buttonRight = tk.Button(set4, image=sim, background="white", command=lambda: show_selected_symbol(sim))
    buttonRight.pack(side=RIGHT)

def show_selected_symbol(symbol_img):
    global current_frame
    if current_frame == "Set2":
        current_frame = "Selected_Symbol1"
    elif current_frame == "Set3":
        current_frame = "Selected_Symbol2"
    elif current_frame == "Set4":
        current_frame = "Selected_Symbol3"
    else:
        print("error")

    clear_symbol_frame()
    selected_symbol= Frame(symbol_frame, background="white")
    selected_symbol.pack()
    display = tk.Label(selected_symbol, image=symbol_img, background="white")
    display.pack(side=TOP)
    buttonDown = tk.Button(selected_symbol, image=voltar, background="white", command=show_symbols_set1)
    buttonDown.pack(side=BOTTOM)


def symbols():
    show_symbols_set1()

def run1():
    while True:
        if current_frame == "Keyboard":
            t_end = time.time() + 3
        else:
            t_end = time.time() + 2.5
        movements = []
        while time.time() < t_end:
            prediction = generate_predictions(cap)
            movements.append(prediction)
            print(mode(movements))
        convert_to_keypress2(mode(movements))

if __name__ == '__main__':

    print("aaaaa")
    import tensorflow as tf
    tf.test.is_gpu_available()
    
    app = tk.Tk()
    screensize = app.maxsize()
    #app.geometry('{}x{}+0+0'.format(*screensize))
    app.geometry("1920x1080")
    app.title('EYEASSiSTIVE')
    app.resizable(False, False)

    set1_img = tk.PhotoImage(file="./ui_images/set1.png")
    set2_img = tk.PhotoImage(file="./ui_images/set2.png")
    set3_img = tk.PhotoImage(file="./ui_images/set3.png")
    banho = tk.PhotoImage(file="./ui_images/banheira.png")
    banheiro = tk.PhotoImage(file="./ui_images/casa de banho.png")
    comer = tk.PhotoImage(file="./ui_images/comer.png")
    divertir = tk.PhotoImage(file="./ui_images/divertir.png")
    dormir = tk.PhotoImage(file="./ui_images/dormir.png")
    escovar = tk.PhotoImage(file="./ui_images/escovar os dentes.png")
    naosei = tk.PhotoImage(file="./ui_images/naosei.png")
    nao = tk.PhotoImage(file="./ui_images/nao.png")
    sim = tk.PhotoImage(file="./ui_images/sim.png")
    voltar = tk.PhotoImage(file="./ui_images/voltar.png")
    teclado = tk.PhotoImage(file="./ui_images/teclado.png")

    app.configure(background="white")
    
    keyboard_frame = Frame(app, background="white")
    keyboard_frame.place(relx=0.5, rely=0.5, anchor="c")

    text_var = tk.StringVar()

    symbol_frame = Frame(app, background="white")
    symbol_frame.place(relx=0.5, rely=0.5, anchor="c")

    selected_button = [-1, -1]
    button_list = [[]]

    keyboard_mode = True
    current_frame = " "

    exp = " "

    app.bind("<Left>", leftKey)
    app.bind("<Right>", rightKey)
    app.bind("<Up>", upKey)
    app.bind("<Down>", downKey)
    app.bind("<Return>", enterKey)
    app.bind("<BackSpace>", backKey)

    keyboard_started = False
    symbols()

    cap = cv2.VideoCapture(0)
    
    thread1 = Thread(target=run1)
    thread1.start()
    while True:
        app.update()