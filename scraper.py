import requests
from bs4 import BeautifulSoup

def get_text(url, s, e):
	URL = url
	try:
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, "html.parser")
		results = soup.find(id="content").findAll('p')
		x = [str(a) for a in results]
		y = " ".join(x)
		z = y.replace('\n', '').replace('<p>','').replace('</p>','').replace('<br>','')
		file_name = str(s) + '-' + str(e) + ".txt"
		with open(file_name, 'w') as f:
		    f.write(z)
	except requests.exceptions.MissingSchema:
		print("Skipping " + str(s) + ' ' + str(e))


# URL = "https://reality-tv-transcripts.fandom.com/wiki/Reality_TV_Transcripts_Wiki"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")
# mydivs = soup.find_all("table", {"class": "fandom-table"})
# survivor = mydivs[1]
# seasons = survivor.findAll('td')
# for i in range(len(seasons)):
# 	season = seasons[i]
# 	episodes = season.findAll('p')
# 	for j in range(len(episodes)):
# 		episode = episodes[j]
# 		episode_div = episode.findAll('a')
# 		if episode_div:
# 			href = episode_div[0]['href']
# 			get_text(href, i+1, j+1)
# 			print(i, j)

get_text('https://reality-tv-transcripts.fandom.com/wiki/Friends%3F', 2, 8)

