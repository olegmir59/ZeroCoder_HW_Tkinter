"""
ОР08. Разработка приложения Tkinter
Напишите приложение на Python с использованием модуля Tkinter
для управления задачами, таск-трекер;
оформить его, прописать функционал для добавления, удаления и
отметки выполненных задач.

Дополнительно сделано чтение списка задач предыдущей сессии из
файла "tasks.txt"    и  возможность записи списка задач в этот файл.

***** ПРОЕКТ ПИШЕТСЯ БЕЗ ИСПОЛЬЗОВАНИЯ  ИИ !!!   *****
"""

import tkinter as tk

def load_tasks_from_file():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                task_listBox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass  # Если файл не существует, ничего не делаем

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="chartreuse1")

def save_tasks_to_file():
    tasks = task_listBox.get(0, tk.END)
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Задачи успешно сохранены в файл tasks.txt")

# Интерфейс графического окна
root = tk.Tk()
root.title("Список задач")
root.configure(background="CadetBlue")

# Надпись и поле для ввода задачи
text1 = tk.Label(root, text="Введите вашу задачу:", bg="aquamarine")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="azure3")
task_entry.pack(pady=10)

# Кнопка для добавления задачи
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

# Кнопка для удаления задачи
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

# Кнопка для отметки выполненной задачи
mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

# Кнопка для сохранения задач в файл
save_button = tk.Button(root, text="Записать задачи в текстовый файл", command=save_tasks_to_file)
save_button.pack(pady=5)

# Надпись для списка задач
text2 = tk.Label(root, text="Список задач:", bg="aquamarine")
text2.pack(pady=5)

# Сам список задач
task_listBox = tk.Listbox(root, height=10, width=50, bg="CadetBlue1")
task_listBox.pack(pady=10)

# Здесь вызываем функцию load_tasks_from_file(), чтобы считать задачи из файла
load_tasks_from_file()

# Главный цикл программы
root.mainloop()
