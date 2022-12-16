import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv
import os
import GUIhelper

tkRoot = tk.Tk()
tkRoot.geometry("1000x650")
tkRoot.resizable(width = True, height = True)
tkRoot.title("Stat-Ball")

tabControl = ttk.Notebook(tkRoot)
footballTab = ttk.Frame(tabControl)
basketballTab = ttk.Frame(tabControl)
tabControl.add(footballTab, text = "Football")
tabControl.add(basketballTab, text = "Basketball")
tabControl.pack(expand = True, fill = tk.BOTH)

GUIhelper.generate_season_input(footballTab)

tkRoot.mainloop()

def season_entered():
    return