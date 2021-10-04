'''Web scarping of IMDB Top 50 movies'''
'''Return a csv file of movie titles and durations'''

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.imdb.com/list/ls055386972/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
movies_html = soup.find_all('div',class_='lister-item-content')
movies = {}
for movie in movies_html:
    title = movie.find('h3').find('a').string
    duration = movie.find('span', class_='runtime').string.strip(' min')
    movies[title] = duration

f = open('imdbtop50movies.csv', 'w', newline='')
writer =  csv.writer(f)
writer.writerow(['Title', 'Duration'])
for key, value in movies.items():
    writer.writerow([key,value])
f.close()
