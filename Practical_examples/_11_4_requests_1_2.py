import pprint

import requests
from threading import Thread

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

genre = requests.get(RANDOM_GENRE_API_URL).json()
data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre}).json()
# print(data)
# {'meta': {'status': 200}, 'response': {...}}

# Создаем адрес из GENIUS_URL + /songs + /ID по поиску в data по 'api_path' + /apple_music_player
# https://genius.com/songs/5101468/apple_music_player

# pprint.pprint(data)

song_data = data['response']['hits'][0]['result']['api_path']
# /songs/803606

song_id = f'{GENIUS_URL}{song_data}/apple_music_player'
print(song_id)
# https://genius.com/songs/4971103/apple_music_player


