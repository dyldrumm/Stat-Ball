from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

season = 2022

def season_csv(season):
    url = "https://www.pro-football-reference.com/years/{}/#all_team_stats.htm".format(season)
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    headers = headers[1:]

    rows = soup.findAll('tr', class_=lambda
        table_rows: table_rows != "thead")
    season_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    season_stats = season_stats[2:]

    stats = pd.DataFrame(season_stats, columns = headers)

    stats = stats.replace(r'', 'N/A', regex=True)
    stats['Season'] = season

    stats.to_csv('Football-CSVs/{}seasonstats.csv'.format(season))

    print("Season stats for  {} season created.".format(season))
    soup.decompose

season_csv(season)
