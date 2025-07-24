"""
ОР08. Разработка приложения Tkinter
Напишите приложение на Python с использованием модуля Tkinter
для управления задачами, таск-трекер;
оформить его, прописать функционал для добавления, удаления и
отметки выполненных задач.

***** ПРОЕКТ ПИШЕТСЯ БЕЗ ИСПОЛЬЗОВАНИЯ  ИИ !!!   *****
"""
import tkinter as tk

def add_task():
    task = task_entry.get()  # здесь мы получаем слова из поля для ввода
    if task:
        task_listBox.insert(tk.END, task) # здесь с помощью константы END вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END) # здесь очищаем поле для ввода, от нулевого индекса и до конца

def delete_task():
    selected_task = task_listBox.curselection() # с помощью функции **curselection** элемент, на который мы нажмём,   # будет передавать свой ID, индекс, в переменную  selected_task
    if selected_task:
        task_listBox.delete(selected_task) # удаляем выбранный элемент из списка


def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="chartreuse1")  # с помощью функции **itemconfig** выполненная задача изменит цвет заливки



root = tk.Tk()
root.title("Список задач")
root.configure(background="CadetBlue")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="aquamarine")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="azure3")
task_entry.pack(pady=10)

#  Создаём и позиционируем кнопку, которая будет добавлять задачу в список:
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

#  Создаём и позиционируем кнопку, которая будет удалять задачу из списка:
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

#  Создаём и позиционируем кнопку, которая будет отмечать задачу выполненной:
mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

#  Добавляем и позиционируем надпись, чтобы у списка задач был заголовок:
text2 = tk.Label(root, text="Список задач:", bg="aquamarine")
text2.pack(pady=5)

#  Используем новую команду, чтобы создать список, в который будут добавляться задачи:
task_listBox = tk.Listbox(root, height=10, width=50, bg="CadetBlue1")


#  Позиционируем список на экране:
task_listBox.pack(pady=10)








root.mainloop()
