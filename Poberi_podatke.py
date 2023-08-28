import requests

stran = requests.get(
    'https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/all/?page=1&sortcol=ppg&sortdir=descending'
)
with open('stran.html', 'w', encoding='utf-8') as dat:
    dat.write(stran.text)

for i in range(11):
    stran = requests.get(
        f"https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/all/?page={i}&sortcol=ppg&sortdir=descending"
    )
    with open(f'stran{i+1}.html', 'a', encoding='utf-8') as dat:
        dat.write(stran.text)