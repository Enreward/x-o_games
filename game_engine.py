import os

PLAYERS = ['Х', 'O']


def intro():
    '''
        Функция выбора размера карты
        :return: размер карты
    '''
    try:
        replay = False
        while True:
            os.system("cls")
            print("Добро пожаловать в крестики-нолики!\n")
            if replay:
                print("Вы выбрали слишком маленький размер карты.")
            count = int(input("Введите размер карты.\nПо-умолчанию - 3: "))
            if count < 3:
                replay = True
                continue
            break
        return count
    except ValueError:
        return 3
    

def instruction(size_map):
    # os.system("cls")
    text_intro = f"""Крестики-Нолики.
Правила:
1) Игроки ходят по очереди. Первым ходит игрок, ставящий крестик (X).
2) Ходить можно только в пустую клетку. За раз можно сделать только один ход.
3) На каждом ходу игроку нужно ввести две цифры без пробела:
   первая: номер по горизонтали
   вторая: номер по вертикали
4) Побеждает тот, кто раньше выстроит свои символы в линию длины {size_map}:
   по горизонтали,
   по вертикали,
   по диоганали.
   Удачной игры!
    """
    return text_intro


def outro(player, dead_heat):
    if dead_heat:
        text_outro = "Ничья!"
    else:
        text_outro = f"""
Пободитель - игрок, ставящий {player}.
Поздравляем!
    """
    return text_outro


def draw(table):
    os.system("cls")
    length = len(table)

    print(instruction(length))
    
    head_line = " "
    for i in range(length):
        head_line += f" {i}"
    print(head_line)

    for i in range(length):
        main_lines = f"{i}"
        for j in range(length):
            main_lines += f" {table[i][j]}"
        print(main_lines)


def player_input(player):
    _input = input(f"Ходит {player}: ")
    _input = tuple(map(int, _input))
    return _input


def check_move(position, possible_position):
    return position in possible_position


def move(table, player_turn, position, possible_position):
    possible_position.remove(position)
    table[position[0]][position[1]] = player_turn
    return table, possible_position


def winning(player, table, combinations, dead_heat):
    if dead_heat:
        return True
    win = False
    for comb in combinations:
        check_comb = []
        for i, j in comb:
            check = True if table[i][j] == player else False
            check_comb.append(check)
        if False in check_comb:
            continue
        else:
            win = True
            break
    if win:
        return True
    return False


def set_winning_combinations(size_map):
    winning_combinations = [[(i, j) for j in range(size_map)] for i in range(size_map)]
    winning_combinations += [[(i, j) for i in range(size_map)] for j in range(size_map)]
    winning_combinations += [[(i, i) for i in range(size_map)]]
    winning_combinations += [[(i, size_map - 1 - i) for i in range(size_map)]]
    return winning_combinations


def computer_algorithm():
    pass
