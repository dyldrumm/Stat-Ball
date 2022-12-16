import tkinter as tk
from tkinter import ttk
from tkinter import *

def generate_season_input(tab):
    season = tk.StringVar()
    seasonInputLabel = tk.Label(tab, text = "Enter the season you want to view:")
    seasonInput = tk.Entry(tab, fg = "white", bg = "gray", width = 12, textvariable = season)
    seasonInputButton = tk.Button(tab, width = 12, relief = RAISED, text = "Get season stats")
    seasonInputLabel.pack()
    seasonInput.pack()
    seasonInputButton.pack()