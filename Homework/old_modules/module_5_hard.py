# Цель: Применить знания полученные в модуле, решив задачу повышенного
# уровня сложности.
#
# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут
# размещаться дополнительные полезные ролики на тему IT
# (юмористические, интервью и т.д.).
# Конечно же для старта написания интернет ресурса требуются хотя бы
# базовые знания программирования.
#
# Именно вам выпала возможность продемонстрировать их, написав
# небольшой набор классов, которые будут выполнять похожий функционал на сайте.
#
# Всего будет 3 класса: UrTube, Video, User.
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых
# будет содержать методы добавления видео, авторизации и регистрации
# пользователя и т.д.
#
# Подробное ТЗ:
# Каждый объект класса User должен обладать следующими атрибутами и методами:
#
# 1. Атрибуты:
# nickname(имя пользователя, строка),
# password(в хэшированном виде, число),
# age(возраст, число)
#
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
#
# 1. Атрибуты:
# title(заголовок, строка),
# duration(продолжительность, секунды),
# time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))
#
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#
# 1. Атрибуты:
# users(список объектов User),
# videos(список объектов Video),
# current_user(текущий пользователь, User)
#
# 2. Метод log_in, который принимает на вход аргументы:
# nickname,
# password
# и пытается найти пользователя в users с такими же логином и паролем.
# Если такой пользователь существует, то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.
#
# 3. Метод register, который принимает три аргумента:
# nickname,
# password,
# age,
# и добавляет пользователя в список, если пользователя не существует
# (с таким же nickname).
# Если существует, выводит на экран: "Пользователь {nickname} уже существует".
# После регистрации, вход выполняется автоматически.
#
# 4. Метод log_out для сброса текущего пользователя на None.
#
# 5. Метод add, который принимает неограниченное кол-во объектов
# класса Video и все добавляет в videos, если с таким же названием видео ещё
# не существует. В противном случае ничего не происходит.
#
# 6. Метод get_videos, который принимает поисковое слово и возвращает список
# названий всех видео, содержащих поисковое слово.
# Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
# (не учитывать регистр).
#
# 7. Метод watch_video, который принимает название фильма, если не находит
# точного совпадения(вплоть до пробела), то ничего не воспроизводится,
# если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.
#
# Для метода watch_video так же учитывайте следующие особенности:
#
# 1. Для паузы между выводами секунд воспроизведения можно использовать функцию
# sleep из модуля time.
# 2. Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
# В противном случае выводить в консоль надпись:
# "Войдите в аккаунт, чтобы смотреть видео"
# 3. Если видео найдено, следует учесть, что пользователю может быть отказано
# в просмотре, т.к. есть ограничения 18+.
# Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# 4. После воспроизведения нужно выводить: "Конец видео"
#
#
# Код для проверки:
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
#
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
#
# Вывод в консоль:
# # Проверка поиска
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
#
# Проверка на вход пользователя и возрастное ограничение
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
#
# Примечания:
# 1. Не забывайте для удобства использовать dunder(магические) методы:
# __str__, __repr__, __contains__, __eq__ и др. (повторить можно здесь)
# 2. Чтобы не запутаться рекомендуется после реализации каждого метода
# проверять как он работает, тестировать разные вариации.


from time import sleep


class User:
    def __init__(
            self,
            nickname: str,
            password: str,
            age: int
    ):
        self.nickname = nickname
        self.password = hash(password)
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
        nicknames = [i.nickname for i in self.users]
        if nickname in nicknames:
            index = nicknames.index(nickname)
            if hash(password) == self.users[index].password:
                self.current_user = self.users[index].nickname

    def register(
            self,
            nickname: str,
            password: str,
            age: int,
    ):
        nicknames = [i.nickname for i in self.users]
        if nickname not in nicknames:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует ')

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
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            nicknames = [i.nickname for i in self.users]
            index = nicknames.index(self.current_user)
            if self.users[index].age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                film_names = [i.title for i in self.videos]
                if film_name in film_names:
                    index = film_names.index(film_name)
                    for i in range(
                            self.videos[index].time_now + 1,
                            self.videos[index].duration + 1
                    ):
                        sleep(0.05)
                        # print(f'Идет просмотр, {i} секунда')
                        print(i, end=' ')
                    print('Конец видео')
                    setattr(self, 'time_now', '0')


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
# ur.watch_video('Лучший язык программирования 2024 года')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

