from tkinter import*
from tkinter.simpledialog import*
from tkinter.filedialog import*

root = Tk()
root.geometry('500x500')

label1 = Label(root, text="선택된 파일이름")
label1.pack()

extName = askstring("확장명", "확장명을 입력(예 : hwp, png, zip 등)")

filename = askopenfilename(parent=root, filetypes=(("입력 파일", "*." + extName), ("모든 파일", "*.*")))
label1.configure(text=str(filename))

root.mainloop()