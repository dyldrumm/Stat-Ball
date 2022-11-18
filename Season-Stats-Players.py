from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

season = 2022
url = "https://www.pro-football-reference.com/years/{}/fantasy.htm".format(season)
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
headers = headers[1:]
print(headers)

rows = soup.findAll('tr', class_=lambda table_rows: table_rows != "thead")
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]
print(player_stats[2])

stats = pd.DataFrame(player_stats, columns = headers)
stats.head()
stats = stats.replace(r'', 0, regex=True)
stats['Year'] = season
stats.head()


def player_csv(year):
    url = "https://www.pro-football-reference.com/years/{}/fantasy.htm".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html)

    headers = [th.getText() for th in soup.findAll('tr')[1].findAll(
        'th')]
    headers = headers[1:]

    rows = soup.findAll('tr', class_=lambda
        table_rows: table_rows != "thead")
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    player_stats = player_stats[2:]

    stats = pd.DataFrame(player_stats, columns=headers)

    stats = stats.replace(r'', 'N/A', regex=True)
    stats['Year'] = year

    stats.to_csv('{}playerstats.csv'.format(year))

    print("Player stats for  {} season created.".format(year))