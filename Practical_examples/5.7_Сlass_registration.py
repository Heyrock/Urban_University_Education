def validate_password(user_str):
    """
    Проверка пароля на надежность
    :param user_str:
    :return: bool
    """
    length = False
    capital = False
    digit = False

    if len(user_str) >= 8:
        length = True

    for i in user_str:
        if i.isupper():
            capital = True
            break

    for i in user_str:
        if i.isdigit():
            digit = True
            break

    return length and capital and digit


class Database:
    """
    База данных пользователей
    """

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    # строка документирования
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(
            self,
            username,
            password,
            password_confirm
    ):
        self.username = username
        # присваиваем пароль, только если совпадают
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()

    while True:
        # 1234567F
        choice = int(input(
            '\nПриветствуем! Выберите действие:\n'
            '1 - Вход\n'
            '2 - Регистрация\n'
            'Ваш выбор: ')
                     )

        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вы вошли в систему, {login}!')
                    break
                else:
                    print('Неверный пароль.')
            else:
                print('Пользователь не найден')

        if choice == 2:
            user = User(
                input('Введите логин: '),
                # морж-операторы, создаем и сразу к ним обращаемся
                password := input('Введите пароль: '),
                # морж-операторы, создаем и сразу к ним обращаемся
                password2 := input('Введите пароль еще раз: '),
            )

            # проверяем пароль на надежность
            if not validate_password(password):
                print('Пароль недостаточно надежный')
                exit()
            else:
                if password != password2:
                    print('Пароли не совпадают, попробуйте еще раз')
                    continue

            # user = User('Eugen', 'password', 'password')
            database.add_user(user.username, user.password)
            # Обращение к строке документирования
            # print(User.__doc__)
        print(database.data)  # {'Eugen': 'password'}
