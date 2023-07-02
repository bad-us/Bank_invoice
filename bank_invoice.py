import os
from tkinter import *
from tkinter import filedialog as fd
from collections import defaultdict

def selectDir():
    return fd.askdirectory()+'/'

# Выбор пути до папки
def FolderPath(directory):
    global files
    global directory_path_file
    directory_path_file = directory
    fileDir=directory.replace('/', '\\')
    fileExt = r".pdf"
    files = [os.path.join(fileDir, _) for _ in os.listdir(fileDir) if _.endswith(fileExt)]
    #print(files)
    return files

# Выбор пути до файла
def FilePath(directory):
    global file
    fileDir = directory.replace('/', '\\')
    fileExt = r"path.txt"
    file = [os.path.join(fileDir, _) for _ in os.listdir(fileDir) if _.endswith(fileExt)]
    #print(file)
    return file

# Начало переноса файлов
def StartCopy(files,file):
    #print(files)
    #print(file)
    #print(directory_path_file)
    path_string = os.path.pathsep.join(file)
    mydict={}
    with open(path_string, encoding="utf8") as f:
        for line in f:
            if not line.strip():
                continue
            k, v = [word.strip() for word in line.split("-")]
            mydict[k] = v
    print(mydict)

    i = 0
    directory2 = "C:\\Users\\v.panin\\Desktop\\test2\\"
    while files:
        path = files[0]
        if not os.path.isfile(f'{directory_path_file}{i}.pdf'):
            name = f'{i}.pdf'
            os.rename(path, directory2 + name)
            del files[0]
        i += 1


# Создание окна
root = Tk()
root.geometry('350x75')

# Создание кнопок и присваивания команд
b1 = Button(text='1.Выбрать папку со счетами', command=lambda: FolderPath(selectDir()))
b1.grid(row=0,column=1)

b2 = Button(text='2.Выбрать папку с файлом', command=lambda: FilePath(selectDir()))
b2.grid(row=0,column=2)

b3 = Button(text='Начать перенос', command=lambda: StartCopy(files,file))
b3.grid(row=2,column=1)

b4 = Button(root, text='Закрыть окно', command=lambda: root.destroy())
b4.grid(row=2,column=2)

root.mainloop()
