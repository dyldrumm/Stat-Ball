import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv
import os

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

season = tk.StringVar()

seasonInputLabel = tk.Label(footballTab, text = "Enter the season you want to view:")
seasonInput = tk.Entry(footballTab, fg = "white", bg = "gray", width = 12, textvariable = season)
seasonInputButton = tk.Button(footballTab, width = 12, relief = RAISED, text = "Get season stats")
seasonInputLabel.pack()
seasonInput.pack()
seasonInputButton.pack()

tkRoot.mainloop()

def season_entered():
    return