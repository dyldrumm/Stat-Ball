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
        tempButton = tk.Button(panel, width = 8, relief = RAISED, text = season + " season player stats", command = partial(display_csv, root, season, sport))
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

def display_csv(root, season, sport):
    fileName = "CSVs/" + sport + "/players/" + season + "footballplayerstats.csv"
    headers = list()
    
    def closeCSV(window):
        window.destroy()

    canvas = Canvas(root)
    seasonLabel = Label(canvas, text = season + " Stats")
    closeButton = Button(canvas, text = "Close", command = partial(closeCSV, canvas))
    yScroll = ttk.Scrollbar(canvas, orient = VERTICAL)
    xScroll = ttk.Scrollbar(canvas, orient = HORIZONTAL)
    tree = ttk.Treeview(canvas, yscrollcommand = yScroll.set, xscrollcommand = xScroll.set, height = 600)
    yScroll.configure(command = tree.yview)
    xScroll.configure(command = tree.xview)
    
    # Read CSV
    with open(fileName, newline = '') as file:
        reader = csv.reader(file)
        first = next(reader)
        for head in first:
            if(head == ''):
                headers.append("Rank")
            else:
                headers.append(head)
        
        tree.configure(columns = headers)
        
        # Generate Headers & Columns
        i = 0
        tree.heading("#0", text = "", anchor = W)
        tree.column("#0", stretch = NO, width = 0)
        for head in headers:
            if(head == "Rank"):
                tree.heading(i, text = "Rank", anchor = W)
                tree.column(i, stretch = NO, minwidth = 1, width = 35)
            if(head == "Player"):
                tree.heading(i, text = head, anchor = W)
                tree.column(i, stretch = NO, minwidth = 1, width = 100)
            else:
                tree.heading(i, text = head, anchor = W)
                tree.column(i, stretch = NO, minwidth = 1, width = 50)
            i += 1
        
        # Load CSV data
        data = list(reader)
        
        i = 0
        for entry in islice(data, 120):
            tree.insert(parent = '', index = i, values = entry)
            i += 1
            
    xScroll.pack(side = BOTTOM, fill = X, expand = False, anchor = S)
    yScroll.pack(side = RIGHT, fill = Y, expand = False, anchor = E)
    seasonLabel.pack(side = TOP, expand = False, anchor = NW)
    closeButton.pack(side = TOP, expand = False, anchor = NE)
    tree.pack(side = LEFT, fill = BOTH, anchor = W)
    root.add(canvas)
    return