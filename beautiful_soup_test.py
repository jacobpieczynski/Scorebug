# https://realpython.com/python-web-scraping-practical-introduction/

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/dionysus' # Tutorial URL
url = 'https://www.espn.com/nhl/scoreboard/_/date/20240320' # NHL Scoreboard
url = 'https://www.espn.com/nba/scoreboard/_/date/20240320' # NBA Scoreboard
url = 'https://www.espn.com/mlb/scoreboard/_/date/20240320' # MLB Scoreboard
urls = ['https://www.espn.com/nhl/scoreboard/_/date/20240320', 'https://www.espn.com/nba/scoreboard/_/date/20240320', 'https://www.espn.com/mlb/scoreboard/_/date/20240320']

def main():

    for url in urls:
        page = urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        games = len(soup.find_all(class_="Scoreboard"))
        league = url.split('/')[3]
        print(f'League: {league.upper()} has {games} games today.')
    #print(soup.find_all(class_="Scoreboard"))
    #print(soup.prettify())

main()