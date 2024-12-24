import pprint
import queue
import requests
from threading import Thread

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

all_songs = []


class GetGenre(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self) -> None:
        genre = requests.get(RANDOM_GENRE_API_URL).json()
        self.queue.put(genre)

class Genius(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self) -> None:
        genre = self.queue.get()
        data = requests.get(
            GENIUS_API_URL,
            params={
                'access_token': ACCESS_TOKEN,
                'q': genre,
            }
        )
        data = data.json()
        try:
            song_id = data['response']['hits'][0]['result']['api_path']
            all_songs.append(f'{GENIUS_URL}{song_id}/apple_music_player')
        except IndexError as e:
            self.run()


queue = queue.Queue()

genre_lst = []
genius_lst = []

for _ in range(20):
    t = GetGenre(queue=queue)
    t.start()
    genre_lst.append(t)

for _ in range(10):
    t = Genius(queue=queue)
    t.start()
    genius_lst.append(t)

for t in genius_lst:
    t.join()

for i in all_songs:
    print(i)
print(len(all_songs))