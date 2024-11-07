# версия 17:00
from time import sleep


class User:
    def __init__(
            self,
            nickname: str,
            password: int,
            age: int
    ):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(
            self,
            title: str,
            duration: int,
            time_now: int = 0,
            adult_mode: bool = False,
    ):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(
            self,
            nickname: str,
            password: str
    ):
        pass
        # if nickname in self.users:
        #     if hash(password) == User
        #         self.current_user = nickname

    def __contains__(self, item):
        return item in self

    def register(
            self,
            nickname: str,
            password: str,
            age: int,
    ):
        pass

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, user_str: str):
        return [i.title for i in self.videos
                if user_str.lower() in i.title.lower()]

    def watch_video(self, film_name):
        film_names = [i.title for i in self.videos]
        if film_name in film_names:
            index = film_names.index(film_name)
            for i in range(
                    self.videos[index].time_now + 1,
                    self.videos[index].duration + 1
            ):
                # sleep(0.2)
                # print(f'Идет просмотр, {i} секунда')
                print(i, end=' ')
            print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
# print(ur.watch_video('Для чего девушкам парень программист?'))
# print('Для чего девушкам парень программист?' )


