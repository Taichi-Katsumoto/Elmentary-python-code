'''
Created on 2018/04/11

@author: Taichi
'''
#指定のフォルダを選択
import tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()
filename=filedialog.askopenfiles(filetype= [("","*")])