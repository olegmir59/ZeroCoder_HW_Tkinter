"""
ОР07. Изучение работы с модулем Tkinter
Напишите программу на Python с использованием модуля tkinter,
которая позволяет пользователю ввести свое имя в окно ввода, а затем выводит
на экран сообщение "Привет, [имя]!".

***** ПРОЕКТ ПИШЕТСЯ БЕЗ ИСПОЛЬЗОВАНИЯ  ИИ !!!   *****
"""
import tkinter as tk
def hello():
    name = entry.get()
    label.config(text=f"Привет,  {name}!")


root = tk.Tk()
root.title("Приветствие")

label = tk.Label(root, text="Введите свое имя")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Получить ответ", command=hello)
button.config(text="тест")
button.pack()

root.mainloop()
