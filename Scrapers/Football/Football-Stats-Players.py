from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

season = 2019

def player_csv(season):
    url = "https://www.pro-football-reference.com/years/{}/fantasy.htm".format(season)
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    headers = headers[1:]

    rows = soup.findAll('tr', class_ = lambda
        table_rows: table_rows != "thead")
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    player_stats = player_stats[2:]

    stats = pd.DataFrame(player_stats, columns = headers)
    stats = stats.replace(r'', 'N/A', regex=True)
    stats['Season'] = season
    stats.to_csv('CSVs/{}playerstats.csv'.format(season))

    print("Player stats for  {} season created.".format(season))
    soup.decompose

player_csv(season)
