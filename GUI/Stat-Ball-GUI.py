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

homeTab = ttk.Frame(tabControl)
tabControl.add(homeTab, text = "Home")

footballTab = ttk.Frame(tabControl)
GUIhelper.generate_season_input_field(footballTab)
tabControl.add(footballTab, text = "Football")

basketballTab = ttk.Frame(tabControl)
GUIhelper.generate_season_input_field(basketballTab)
tabControl.add(basketballTab, text = "Basketball")

tabControl.pack(expand = True, fill = tk.BOTH)

tkRoot.mainloop()

def season_entered():
    return