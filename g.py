from tkinter import *
from tkinter import ttk
##from ttk import Treeview
import ttk

root=Tk()
tree=ttk.Treeview(root)
tree['columns']=('one','two')
tree.column('one',width=100)
tree.column('two',width=100)
tree.heading('one',text='column A')
tree.heading('two',text='column B')
##tree.insert(' ',0
