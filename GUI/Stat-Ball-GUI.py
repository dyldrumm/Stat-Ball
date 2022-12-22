import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv
import os
import GUIhelper

tkRoot = tk.Tk()
tkRoot.geometry("1200x800")
tkRoot.resizable(width = True, height = True)
tkRoot.title("Stat-Ball")

tabControl = ttk.Notebook(tkRoot)

# -- Generate Home tab
homeTab = ttk.Frame(tabControl)
homePanel = GUIhelper.load_tab_base(homeTab)
# Add Home tab
homePanel.pack(expand = True, fill = tk.BOTH)
tabControl.add(homeTab, text = "Home")

# -- Generate Football tab
footballTab = ttk.Frame(tabControl)
footballPanel = GUIhelper.load_tab_base(footballTab)
# Generate CSV manager (left side)
footballCSVPanel = GUIhelper.generate_csv_manager(footballPanel, "football")
footballCSVPanel.add(GUIhelper.generate_season_input_field(footballCSVPanel))
# Add CSV manager to panel
footballPanel.add(footballCSVPanel)
# Add Football tab
footballPanel.pack(expand = True, fill = tk.BOTH)
tabControl.add(footballTab, text = "Football")

# -- Generate Basketball tab
basketballTab = ttk.Frame(tabControl)
basketballPanel = GUIhelper.load_tab_base(basketballTab)
# Add Basketball tab
basketballPanel.pack(expand = True, fill = tk.BOTH)
tabControl.add(basketballTab, text = "Basketball")

tabControl.pack(expand = True, fill = tk.BOTH)

def season_entered():
    return

tkRoot.mainloop()