# 1.
# У файлі task1.txt знаходиться текст субтитрів взятий з відео на ютубі. Текст
# складається з міток часу і репліки яка була сказана в той момент часу.
# Причому репліка знаходиться в наступному рядку після мітки часу.
# Прочитайте вміст файлу
# Результатом виконнання завдання повинно бути:
# 1. словник елементами якого буде пара ключ:значення де ключ - мітка часу,
# значення - репліка в даний момент часу
# 2. файл в якому знаходиться текст з якого видалені всі мітки часу. всі
# субтитри повинні мати вигляд простого тексту.
# Це означає що окрім видалення міток часу, вам потрібно видалити переноси
# рядків.
#    Undertask 1.
file = open('task_1.txt', 'rt')
list_comp = file.readlines()
# # A definition data types
# print(type(list_comp))
# # To read file 'task_1.txt'
print(list_comp)
# Building function conversion list to dict
def Convert(list_comp):
    it = iter(list_comp)
    res_dct = dict(zip(it, it))
    return res_dct
print(Convert(list_comp))
# To created variable for comfortable perform the task.
dict_comp = Convert(list_comp)

print(dict_comp.keys())
print(dict_comp.values())
file.close()

#    Undertask 2.
file = open('task_1.txt', 'rb')
list_comp = file.read()
# print(list_comp)
a = str(list_comp)
print(type(a))
def remove_spaces(a):
    a = a.replace("\n", "")
    return a
# print(remove_spaces(a))

file.close()


#2.
# В файлі task2 збережений список, відкрийте цей файл, прочитайте вміст, і
# знайдіть середнє арифметичне чисел що знаходяться в списку.


# read file 'task_2.txt' in as byte file
file = open('task_2.txt', 'rb')
b = file.read()
print(b)
file.close()

# change byte file on int
change_on_int = int.from_bytes(b, 'little')
print(change_on_int)

# definition lenght file
print(len([change_on_int]))

# definition average value divided on 1, according with lenght
average = change_on_int / 1
print(average)


# 3. Використовуючи openpyxl (або будь-яку іншу зручну для вас бібліотеку),
# напишіть контекстний менеджер для роботи з ексель.
# Даний менеджер повинен бути аналогом методу open()
from openpyxl import Workbook
import datetime

wb = Workbook()

class Task:
    def __init__(self, path):
        self.file = open(path)
    def __enter__(self):
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return True
        elif exc_val is Exception:
            print("Exception")
            return True
        else:
            return False
task = Task

with open('task_3.xlsx', 'r') as file:
    # grab the active worksheet
    ws = wb.active

# Data can be assigned directly to cells
    ws['A1'] = 'Performed a three task.'

# Rows can also be appended
    file.write = ws.append([1])
    file.write = ws.append([2])
    file.write = ws.append([3])

# Python types will automatically be converted
    ws['A7'] = datetime.datetime.now()

# Save the file
    wb.save("task_3.xlsx")
    print(file)