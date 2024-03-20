from bs4 import BeautifulSoup

class Game:
    def __init__(self, league, game_html):
        teams = game_html.find_all(class_='ScoreCell__TeamName')
        self.away = teams[0].get_text()
        self.home = teams[1].get_text()
        self.league = league
        #print(teams)
        print(self.__repr__())
        

    def __repr__(self):
        return f'{self.away} at {self.home} in the {self.league.upper()}'