import requests
import json
searches = ['Hulk','Superman','spiderman']
for search in searches:
    r = requests.get('http://omdbapi.com/?s='+ search +'&apikey=BanMePlz')
    data = json.loads(r.text)
    for movie in data['Search']:
        if movie['Poster'] != "N/A":
            r = requests.get(movie['Poster'])
            open(movie['imdbID']+".jpg", 'wb').write(r.content)
