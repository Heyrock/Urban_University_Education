# Продолждение развития кода из _11_4_threads_1_2.py
import datetime
import queue
from pprint import pprint
from threading import Thread, Event

import requests

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'


class GetGenre(Thread):
    def __init__(self, queue, stop_event):
        super().__init__()
        self.queue = queue
        self.stop_event = stop_event

    def run(self) -> None:
        while not stop_event.is_set():
            genre = requests.get(RANDOM_GENRE_API_URL).json()
            self.queue.put(genre)


class Genius(Thread):
    all_songs = []

    def __init__(
            self,
            queue,
            stop_event,
            counter
    ):
        super().__init__()
        self.queue = queue
        self.stop_event = stop_event
        self.counter = counter

    def run(self) -> None:
        genre = self.queue.get()
        # print(self.queue.qsize())
        data = requests.get(
            GENIUS_API_URL,
            params={
                'access_token': ACCESS_TOKEN,
                'q': genre,
            }
        )
        data = data.json()
        while not stop_event.is_set():
            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                self.all_songs.append(
                    {'genre': genre, 'song': f'{GENIUS_URL}{song_id}/apple_music_player'}
                )
                if self._list_is_filled():
                    self.stop_event.set()
            except IndexError as e:
                self.run()

    def _list_is_filled(self):
        return len(self.all_songs) > self.counter



queue = queue.Queue()
stop_event = Event()
counter = 5

genre_lst = []
genius_lst = []

start = datetime.datetime.now()

for _ in range(6):
    t = GetGenre(
        queue=queue,
        stop_event=stop_event
    )
    t.start()
    genre_lst.append(t)

for _ in range(10):
    t = Genius(
        queue=queue,
        stop_event=stop_event,
        counter=counter,
    )
    t.start()
    genius_lst.append(t)

for t in genius_lst:
    t.join()

stop_event.set()

for t in genre_lst:
    t.join()

for i in Genius.all_songs:
    pprint(i)

print(len(Genius.all_songs))

print('Количество неиспользованных жанров', queue.qsize())

end = datetime.datetime.now()
print(end - start)

# {'genre': 'grindnew wavebop',
#  'song': 'https://genius.com/songs/495377/apple_music_player'}
# {'genre': 'grindnew wavebop',
#  'song': 'https://genius.com/songs/495377/apple_music_player'}
# {'genre': 'grindnew wavebop',
#  'song': 'https://genius.com/songs/495377/apple_music_player'}
# {'genre': 'grindnew wavebop',
#  'song': 'https://genius.com/songs/495377/apple_music_player'}
# {'genre': 'grindnew wavebop',
#  'song': 'https://genius.com/songs/495377/apple_music_player'}
# {'genre': 'grindnew wavebop',
#  'song': 'https://genius.com/songs/495377/apple_music_player'}
# 6
# Количество неиспользованных жанров 1
# 0:00:02.669923