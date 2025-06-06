from tkinter import*
from tkinter import messagebox

def func_open() :
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택했습니다")

def func_exit() :
    root.quit()
    root.destroy()

root = Tk()

mainMenu = Menu(root)
root.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

root.mainloop()
