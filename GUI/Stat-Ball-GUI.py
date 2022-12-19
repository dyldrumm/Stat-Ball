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
homePanel = GUIhelper.load_tab_base(homeTab)
GUIhelper.generate_csv_input_field(homePanel)
tabControl.add(homeTab, text = "Home")

footballTab = ttk.Frame(tabControl)
footballPanel = GUIhelper.load_tab_base(footballTab)
GUIhelper.generate_season_input_field(footballPanel)
tabControl.add(footballTab, text = "Football")

basketballTab = ttk.Frame(tabControl)
basketballPanel = GUIhelper.load_tab_base(basketballTab)
GUIhelper.generate_season_input_field(basketballPanel)
tabControl.add(basketballTab, text = "Basketball")

tabControl.pack(expand = True, fill = tk.BOTH)

def season_entered():
    return

tkRoot.mainloop()

with open('CSVs/2022playerstats.csv') as f:
        csvReader = csv.reader(f, delimiter = ',')
        for row in csvReader:
            if(csvReader.line_num < 1):
                print(row)