'''
Created on 2018/04/11

@author: Taichi
'''
import tkinter as tk
from tkinter import ttk
import os
from PIL import Image
import sys

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        tk.Frame.__init__(self, master)
        self.pack(expand=1, fill=tk.BOTH, anchor=tk.NW)
        self.create_widgets()

        sys.stdout = self.StdoutRedirector(self.text)
        sys.stderr = self.StderrRedirector(self.text)
        
    def create_widgets(self):
        self.label = tk.Label(self, text=u'入力ファイル')
        self.canvas = tk.Canvas(self)

        self.text = tk.Text(self)
        self.text = tk.Text(self, wrap=tk.NONE)
        self.yscroll = tk.Scrollbar(self, command=self.text.yview)
        self.xscroll = tk.Scrollbar(self, command=self.text.xview,orient=tk.HORIZONTAL)
        self.text['yscrollcommand'] = self.yscroll.set
        self.text['xscrollcommand'] = self.xscroll.set
        self.text.grid(column=0, columnspan=3, row=2, rowspan=2, sticky=tk.NSEW)
        self.yscroll.grid(column=2, row=2, sticky=tk.NS + tk.E)
        self.xscroll.grid(column=0, columnspan=3, row=3, sticky=tk.EW + tk.S)

        self.var_entry = tk.StringVar()
        self.var_entry.trace('w', self.entry_changed)
        self.entry = tk.Entry(self, textvariable=self.var_entry)
        self.var_check = tk.BooleanVar()
        self.check = tk.Checkbutton(self, text=u'拡張子をtxtに限定',variable=self.var_check)
        self.button = tk.Button(self, text=u'開く', command=self.button_pushed)

        self.label.grid(column=0, row=0, sticky=tk.W)
        self.entry.grid(column=1, row=0, sticky=tk.EW)
        self.button.grid(column=2, row=0, sticky=tk.E)
        self.check.grid(column=0, columnspan=2, row=1, sticky=tk.W)
        self.text.grid(column=0, columnspan=3, row=2, sticky=tk.NSEW)
        self.canvas.grid(column=0, columnspan=3, row=4, sticky=tk.NSEW)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def button_pushed(self):
        self.var_entry.set(u'ボタンが押されました．')

    def entry_changed(self, *args):
        if os.path.exists(self.var_entry.get()):
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', open(self.var_entry.get()).read())

    def set_image(self):
        img = Image.open('foo.png')
        img.save('_tmp.gif')
        self.image_data = tk.PhotoImage(file='_tmp.gif')
        self.canvas.create_image(200, 100, image=self.image_data)
        
    class IORedirector(object):
        def __init__(self, text_area):
            self.text_area = text_area

    class StdoutRedirector(IORedirector):
        def write(self, st):
            self.text_area.insert(tk.INSERT, st)

    class StderrRedirector(IORedirector):
        def write(self, st):
            self.text_area.insert(tk.INSERT, st)
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
