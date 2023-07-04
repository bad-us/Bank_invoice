import os
from tkinter import *
from tkinter import filedialog as fd
import re


def selectDir():
    return fd.askdirectory() + '/'


# Выбор пути до папки
def FolderPath(directory):
    global files
    global directory_path_file
    directory_path_file = directory
    fileDir = directory.replace('/', '\\')
    fileExt = r".pdf"
    files = [os.path.join(fileDir, _) for _ in os.listdir(fileDir) if _.endswith(fileExt)]
    # print(files)
    return files


# Выбор пути до файла
def FilePath(directory):
    global file
    fileDir = directory.replace('/', '\\')
    fileExt = r"path.txt"
    file = [os.path.join(fileDir, _) for _ in os.listdir(fileDir) if _.endswith(fileExt)]
    print(file)
    return file


# Начало переноса файлов
def StartCopy(files, file):
    path_string = os.path.pathsep.join(file)
    mydict = {}
    # Рвзбираем файл с ключами и папками
    with open(path_string, encoding="utf8") as f:
        for line in f:
            if not line.strip():
                continue
            k, v = [word.strip() for word in line.split(" - ")]
            mydict[k] = v
    print(mydict)

    i = 0

    while files:
        path = files[0]
        id_invoice = re.findall('(\d+)', files[0])
        id_path = get_key(mydict, id_invoice[0])  # путь по значению
        # print(id_invoice[0])
        id_path = str(id_path)
        if id_path == 'None':
            del files[0]
        else:
            copy_path = id_path
            # print(type(id_path))
            if not os.path.isfile(f'{directory_path_file}{i}.pdf'):
                #name = f'{i}.pdf'
                name = f'{name_invoice(id_invoice)}.pdf'
                print(name)
                os.rename(path, copy_path + name)  # 1111
                del files[0]
            i += 1


# выбор пути к папке из списка
def get_key(mydict, value):
    for k, v in mydict.items():
        if k == value:
            return v


def name_invoice(id_invoice):
    if id_invoice[1] == id_invoice[4]:
        name_file_invoice = f'{id_invoice[3]}_{id_invoice[2]}_{id_invoice[1]}'
    else:
        name_file_invoice = f'{id_invoice[3]}_{id_invoice[2]}_{id_invoice[1]}-{id_invoice[4]}'
    return (name_file_invoice)


# Создание окна
root = Tk()
root.geometry('350x75')

# Создание кнопок и присваивания команд
b1 = Button(text='1.Выбрать папку со счетами', command=lambda: FolderPath(selectDir()))
b1.grid(row=0, column=1)

b2 = Button(text='2.Выбрать папку с файлом', command=lambda: FilePath(selectDir()))
b2.grid(row=0, column=2)

b3 = Button(text='Начать перенос', command=lambda: StartCopy(files, file))
b3.grid(row=2, column=1)

b4 = Button(root, text='Закрыть окно', command=lambda: root.destroy())
b4.grid(row=2, column=2)

root.mainloop()
