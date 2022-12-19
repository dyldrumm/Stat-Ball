import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import csv

localSeason = (str)

# Generate default tab template
def load_tab_base(root):
    panel = PanedWindow(root, bd = 1, relief = "sunken", bg = "lightgrey")
    panel.pack(expand = True, fill = tk.BOTH)
    
    return panel

# Generate Label, Field and Button to enter season and load stats
def generate_season_input_field(root):    
    season = tk.StringVar()
    
    seasonInputLabel = tk.Label(root, text = "Enter the season you want to view:")
    seasonInput = tk.Entry(root, text = "black", bg = "lightgrey", width = 15, textvariable = season)
    seasonInputButton = tk.Button(root, width = 12, relief = RAISED, text = "Get season stats", command = load_season_stats)
    
    seasonInputLabel.pack(side = TOP, anchor = "w")
    seasonInput.pack(side = TOP, anchor = "w")
    seasonInputButton.pack(side = TOP, anchor = "w")
    
# Generate table containing stats for selected season (Generated from stored CSV)
def load_season_stats(root, season):    
    print(season.get() + " Football season loaded")
    margin = Frame(root)
    scrollbarX = Scrollbar(margin, orient = HORIZONTAL)
    scrollbarY = Scrollbar(margin, orient = VERTICAL)
    tree = ttk.Treeview(margin, selectmode = "extended", yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)
    
    scrollbarX.config(command = tree.xview)
    scrollbarY.config(comman = tree.yview)
    
    scrollbarX.pack(side = BOTTOM, fill = X)
    scrollbarY.pack(side = RIGHT, fill = Y)
    
    headTitles = list()
    playerValues = list()
    
# Generate imput
def generate_csv_input_field(root):    
    season = tk.StringVar()
    csvInputLabel = tk.Label(root, text = "Find the CSV you want to view:")
    csvInput = tk.Entry(root, text = "black", bg = "lightgrey", width = 15, textvariable = season)
    csvInputButton = tk.Button(root, width = 12, relief = RAISED, text = "Get CSV", command = load_csv)
    
    csvInputLabel.pack(side = TOP, anchor = "w")
    csvInput.pack(side = TOP, anchor = "w")
    csvInputButton.pack(side = TOP, anchor = "w")
    
# Load & visualize CSV
def load_csv(root):    
    print(localSeason + " Football season loaded")
    margin = Frame(root)
    scrollbarX = Scrollbar(margin, orient = HORIZONTAL)
    scrollbarY = Scrollbar(margin, orient = VERTICAL)
    tree = ttk.Treeview(margin, selectmode = "extended", yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)
    
    scrollbarX.config(command = tree.xview)
    scrollbarY.config(comman = tree.yview)
    
    scrollbarX.pack(side = BOTTOM, fill = X)
    scrollbarY.pack(side = RIGHT, fill = Y)
    
    headTitles = list()
    playerValues = list()