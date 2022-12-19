from functools import partial
from itertools import islice
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import csv
import os

localSeason = (str)

# Generate default tab template
def load_tab_base(root):
    panel = PanedWindow(root, bd = 1, relief = "sunken", bg = "lightgrey", orient = HORIZONTAL)
    
    return panel

def generate_csv_manager(root, sport):
    panel = PanedWindow(root, bd = 1, relief = "raised", bg = "lightgrey", orient = VERTICAL)
    
    # Get list of already generated seasons
    seasons = list()
    direct = os.fsencode("CSVs/football/players/")
    for file in os.listdir(direct):
        filename = os.fsdecode(file)
        seasons.append(filename[0:4])
    # Generate button for each season
    for season in seasons:
        tempButton = tk.Button(panel, width = 8, relief = RAISED, text = season + " season player stats", command = partial(display_csv, root, season))
        panel.add(tempButton)
    
    return panel

# Generate Label, Field and Button to enter season and load stats
def generate_season_input_field(root):
    season = tk.StringVar()

    panel = PanedWindow(root, bd = 1, relief = "raised", bg = "grey", orient = VERTICAL)

    seasonInputLabel = tk.Label(panel, text = "Enter the season you want to view:")
    seasonInputField = tk.Entry(panel, text = "black", bg = "lightgrey", width = 15, textvariable = season)
    seasonInputButton = tk.Button(panel, width = 12, relief = RAISED, text = "Get season stats")

    seasonInputLabel.pack(side = TOP)
    seasonInputField.pack(side = TOP)
    seasonInputButton.pack(side = TOP)

    return panel

# Generate table containing stats for selected season (Generated from stored CSV)
def display_csv(root, season):
    panel = PanedWindow(root, bd = 1, relief = "sunken", bg = "grey", orient = VERTICAL, borderwidth = 1)
    fileName = "CSVs/football/players/" + season + "footballplayerstats.csv"
    headers = list()
    headers.append("Rank")

    with open(fileName, newline = '') as file:
        reader = csv.reader(file)
        first = next(reader)
        for head in first:
            if(head != ''):
                headers.append(head)

        labels = PanedWindow(panel, bd = 1, relief = "sunken", bg = "grey", orient = VERTICAL, borderwidth = 1)
    
        for i, head in enumerate(headers, start = 0):
            label = tk.Label(labels, text = head, height = 2, width = 13, font=("Arial", 8))
            label.pack(side = LEFT)

        values = PanedWindow(panel, bd = 1, relief = "sunken", bg = "grey", orient = VERTICAL, borderwidth = 1)
        data = list(reader)
        
        for entry in islice(data, 30):
            temp = PanedWindow(panel, bd = 1, relief = "sunken", bg = "grey", orient = HORIZONTAL, borderwidth = 1)
            for val in entry:
                label = tk.Label(temp, text = val, height = 1, width = 13, font=("Arial", 8))
                label.pack(side = LEFT)
            values.add(temp)

    labels.pack()
    values.pack(fill = tk.BOTH)
    root.add(panel)
    return panel

    #margin = PanedWindow(root)
    #scrollbarX = Scrollbar(margin, orient = HORIZONTAL)
    #scrollbarY = Scrollbar(margin, orient = VERTICAL)
    #tree = ttk.Treeview(margin, selectmode = "extended", yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)
    
    #scrollbarX.config(command = tree.xview)
    #scrollbarY.config(comman = tree.yview)
    
    #scrollbarX.pack(side = BOTTOM, fill = X)
    #scrollbarY.pack(side = RIGHT, fill = Y)
    
    #headTitles = list()
    #playerValues = list()