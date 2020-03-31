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
            info.append([episode['id'], episode['name'], episode['air_date'], episode['episode'], str(episode['id'])])

        first = False

    return info

@app.route('/episode/<id_>')
def episode(id_):
    print('---------------')
    url = 'https://rickandmortyapi.com/api/episode/' + id_
    print(url)
    response = requests.get(url).json()
    for x in response['characters']:
        print(x)

    print(response)

    episode_ = [response['id'], response['air_date'], response['episode'],
               response['url'], response['created']]

    urls = response['characters']

    characters = []

    for url in urls:
        resp = requests.get(url).json()

        characters.append([str(resp['id']), resp['name']])


    return render_template('episode.html', name=response['name'],
                           episode=episode_, characters=characters)


@app.route('/location/<id_>')
def location(id_):
    print('---------------')
    url = 'https://rickandmortyapi.com/api/location/' + id_
    print(url)
    response = requests.get(url).json()
    for x in response['residents']:
        print(x)

    print(response)

    location = [response['name'], response['type'],
                response['dimension']]

    urls = response['residents']

    characters = []

    for url in urls:
        resp = requests.get(url).json()

        characters.append([str(resp['id']), resp['name']])


    return render_template('location.html', name=response['name'],
                           location=location, characters=characters)





@app.route('/character/<id_>')
def character(id_):
    print('---------------')
    url = 'https://rickandmortyapi.com/api/character/' + id_
    print(url)
    response = requests.get(url).json()

    for k, v in response.items():
        print(k, v)
        print()
    episodes = []
    episodes_ = response['episode']
    for x in episodes_:
        episodes.append(x)


    character_ = [response['status'], response['species'], response['type'],
               response['gender'],
          [response['origin']['name'], response['origin']['url'].split('/')[-1]],
        [response['location']['name'], response['location']['url'].split('/')[-1]]]

    urls = response['episode']

    episodes = []

    for url in urls:
        resp = requests.get(url).json()

        episodes.append([str(resp['id']), resp['name']])


    return render_template('character.html', name=response['name'],
                           char=character_, img=response['image'], episodes=episodes)





@app.route('/')
def run():
    episodes_list = capitulos()
    return render_template('index.html', list=episodes_list)



if __name__ == '__main__':
    app.run(debug=True)