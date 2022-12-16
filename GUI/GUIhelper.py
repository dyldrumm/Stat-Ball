import tkinter as tk
from tkinter import ttk
from tkinter import *

#Generate Label, Field and Button to enter season and load stats
def generate_season_input_field(tab):
    season = tk.StringVar()
    seasonInputLabel = tk.Label(tab, text = "Enter the season you want to view:")
    seasonInput = tk.Entry(tab, fg = "white", bg = "gray", width = 12, textvariable = season)
    seasonInputButton = tk.Button(tab, width = 12, relief = RAISED, text = "Get season stats", command = load_season_stats(seasonInput.get()))
    
    seasonInputLabel.pack()
    seasonInput.pack()
    seasonInputButton.pack()
    
def load_season_stats():
    tkSeasonRoot = tk.Tk()