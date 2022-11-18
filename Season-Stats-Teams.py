from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

season = 2022
url = "https://www.pro-football-reference.com/years/{}/#all_team_stats.htm".format(season)
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
headers = headers[1:]
print(headers)