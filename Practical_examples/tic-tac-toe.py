def greeting():
    greeting_msg = 'Добро пожаловать в крестики-нолики!'
    print(greeting_msg)
    print('-' * len(greeting_msg))


def draw_area():
    print()
    for i in area:
        print(*i)
    print()


def announce_user(cur_turn):
    print(f'Ход: {cur_turn}')
    if cur_turn % 2 == 0:
        turn_char = 'O'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        'Ходят крестики'
    return turn_char


def ask_raw_and_column():
    user_row = int(input('Введите номер строки (1, 2, 3): ')) - 1
    user_column = int(input('Введите номер столбца (1, 2, 3): ')) - 1
    return user_row, user_column


def apply_turn(cur_char):
    user_raw, user_column = ask_raw_and_column()
    if area[user_raw][user_column] == '*':
        area[user_raw][user_column] = cur_char
    else:
        print('\nЯчейка уже занята, выберите другую')
        apply_turn(cur_char=cur_char)


def check_winner(cur_char):
    winner_name = 'крестики'
    if cur_char == 'O':
        winner_name = 'нолики'

    for i in area:
        if i[0] == i[1] == i[2] == cur_char:
            print(f'Победили {winner_name}!')
            return False

    for i in range(3):
        if area[0][i] == area[1][i] == area[2][i] == cur_char:
            print(f'Победили {winner_name}!')
            return False

    if area[0][0] == area[1][1] == area[2][2] == cur_char:
        print(f'Победили {winner_name}!')
        return False

    if area[2][0] == area[1][1] == area[0][2] == cur_char:
        print(f'Победили {winner_name}!')
        return False

    return True


area = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]
greeting()
draw_area()
game_continues = True
turn = 1

while game_continues:
    cur_user = announce_user(cur_turn=turn)
    apply_turn(cur_char=cur_user)
    draw_area()
    game_continues = check_winner(cur_char=cur_user)

    turn += 1
    if turn == 10:
        print('Ничья')
        break
