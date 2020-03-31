from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

def capitulos():
    response = requests.get('https://rickandmortyapi.com/api/episode/')
    pages = response.json()['info']['pages']
    info = []
    first = True

    for pag in range(1, pages + 1):
        if not first:
            response = requests.get('https://rickandmortyapi.com/api/episode/?page=' + str(pag))

        for episode in response.json()['results']:
            info.append([episode['id'], episode['name'], episode['air_date'], episode['episode'], episode['url']])

        first = False
   
    return info



@app.route('/')
def hello_world():
    episodes_list = [[1, 2, 3, 4], [1, 3, 4, 5], [5, 5, 6, 7]]

    episodes_list = capitulos()
    return render_template('index.html', list=episodes_list)

if __name__ == '__main__':
    app.run()