import os
from tkinter import *
from tkinter import filedialog as fd

def selectDir():
    return fd.askdirectory()+'/'

def startRename(directory):
    directory1=directory.replace('/', '\\')
    files=sorted([path for path in os.listdir(directory) if os.path.isfile(directory+path)])
    i=0

    while files:
        file=files[0]
        ext=file.split('.')[-1]
        if not os.path.isfile(f'{directory}{i}.{ext}'):
            name = f'{i}.{ext}'
            os.rename(directory1+file, directory1+name)
            del files[0]
        i+=1

def FilePath(directory):
    #directory1 = directory.replace('/', '\\')
    files = sorted([path for path in os.listdir(directory) if os.path.isfile(directory + path)])
    #print(files)

root = Tk()
root.geometry('350x75')

# Создание кнопок и присваивания команд
b1 = Button(text='Выбрать папку со счетами', command=lambda: startRename(selectDir()))
b1.grid(row=0,column=1)

b2 = Button(text='Выбрать папку с файлом', command=lambda: FilePath(selectDir()))
b2.grid(row=0,column=3)

#b3 = Button(text='ОК', command=Close())
#b3.grid(row=2,column=3)

root.mainloop()