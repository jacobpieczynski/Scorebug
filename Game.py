from bs4 import BeautifulSoup

class Game:
    def __init__(self, league, game_html):
        teams = game_html.find_all(class_='ScoreCell__TeamName')
        records = game_html.find_all(class_='ScoreboardScoreCell__Record')
        self.away, self.home = teams[0].get_text(), teams[1].get_text()
        # Gets the records of the teams playing
        if len(records) <= 2:
            self.away_record, self.home_record = records[0].get_text(), records[1].get_text()
        else:
            self.away_record, self.home_record = records[0].get_text(), records[2].get_text()
        self.league = league
        #print(teams)
        print(self.__repr__())
        

    def __repr__(self):
        return f'{self.away} ({self.away_record}) at {self.home} ({self.home_record}) in the {self.league.upper()}'