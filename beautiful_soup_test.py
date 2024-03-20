# https://realpython.com/python-web-scraping-practical-introduction/
from bs4 import BeautifulSoup
from Game import *
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/dionysus' # Tutorial URL
url = 'https://www.espn.com/nhl/scoreboard/_/date/20240320' # NHL Scoreboard
url = 'https://www.espn.com/nba/scoreboard/_/date/20240320' # NBA Scoreboard
url = 'https://www.espn.com/mlb/scoreboard/_/date/20240320' # MLB Scoreboard
urls = ['https://www.espn.com/nhl/scoreboard/_/date/20240320', 'https://www.espn.com/nba/scoreboard/_/date/20240320', 'https://www.espn.com/mlb/scoreboard/_/date/20240320']

def main():
    games = dict()
    for url in urls:
        page = urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        game_ct = len(soup.find_all(class_='Scoreboard'))
        league = url.split('/')[3]
        games[league] = soup.find_all(class_='Scoreboard')
        print(f'League: {league.upper()} has {game_ct} games today.')
    #print(soup.find_all(class_='Scoreboard'))
    #print(soup.prettify())
    print(games.keys())
main()