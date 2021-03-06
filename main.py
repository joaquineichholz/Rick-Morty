import requests

response = requests.get('https://rickandmortyapi.com/api/episode/')

pages = response.json()['info']['pages']

if response.status_code == 200:
    print('Success!')

elif response.status_code == 404:
    print('Not Found.')

else:
    print('An error has occurred')


def capitulos():
    response = requests.get('https://rickandmortyapi.com/api/episode/')
    pages = response.json()['info']['pages']
    info = []
    first = True

    for pag in range(1, pages + 1):
        if not first:
            response = requests.get('https://rickandmortyapi.com/api/episode/?page=' + str(pag))

        for data in response.json()['results']:
            info.append([data['name'], data['air_date'], data['episode'], data['url']])

            print(episode['id'], episode['name'])

        first = False

    return info


for pag in range(1, pages + 1):
    if not first:
        response = requests.get('https://rickandmortyapi.com/api/episode/?page=' + str(pag))

    info = response.json()['results']

    for episode in info:
        print(episode['id'], episode['name'])

    first = False
