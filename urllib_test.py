from urllib.request import urlopen
url = 'http://olympus.realpython.org/profiles/aphrodite'
#url = 'http://olympus.realpython.org/profiles/poseidon'
#url = 'https://www.espn.com/nba/scoreboard/_/date/20240315'

def main():
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    start_index = html.find('<title>') + len('<title>')
    end_index = html.find('</title>')
    title = html[start_index:end_index]
    print(title)

main()