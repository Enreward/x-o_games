from game_engine import *


def setup(size_map):
    """
        Предигровая инициализация. Выполнится при запуске один раз.
        :param size_map:
        :return:
            table - [int][int],
            turn - int,
            wrong_input - bool,
            dead_heat - bool,
            win - bool,
            possible_position - [(int, int)],
            winning_combinations - [[(int, int), (int, int), (int, int)]]
    """
    table = []
    for i in range(size_map):
        table.append(['-'] * size_map)
    
    turn = 0                # переменная определяет текущего игрока
    wrong_input = False     # Неправильный ход
    dead_heat = False       # Ничья
    win = False             # Победа
    possible_position = [(i, j) for i in range(size_map) for j in range(size_map)]
    winning_combinations = set_winning_combinations(size_map)
    return table, turn, wrong_input, dead_heat, win, possible_position, winning_combinations


def main():
    """
        Основной алгоритм игры
        :return: None
    """
    try:
        size_map = set_size_map()
        table, \
            turn, \
            wrong_input, \
            dead_heat, \
            win, \
            possible_position, \
            winning_combinations = setup(size_map)
        
        draw(table, size_map)       # начальная отрисовка
        player = PLAYERS[turn]      # устанавливаем первого игрока
    except KeyboardInterrupt:
        print("\nКонец игры.")
        return
    while not win and not dead_heat:
        try:
            if wrong_input:
                print("Вы ошиблись. Пожалуйста, повторите ход.")
            # Ход игрока
            position = player_input(player)
            # Проверка возможности хода
            possible_move = check_move(position, possible_position)
            if not possible_move:
                raise ValueError
            wrong_input = False
            # Фиксируем ход игрока
            table, possible_position = move(table, player, position, possible_position)
            # Рисуем
            draw(table, size_map)
            # Ничья, если некуда больше ходить
            if not possible_position:
                dead_heat = True
            win = winning(table, player, winning_combinations)
            # Проверка победы
            if win or dead_heat:
                print(outro(player, win, dead_heat))
            # Меняем игрока
            turn = (turn + 1) % 2
            player = PLAYERS[turn]
        except KeyboardInterrupt:
            # Сдача
            print(f"Игрок {player} сдался.")
            win = True
        except ValueError:
            # Недопустимый ход
            wrong_input = True
            draw(table, size_map)
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    input("Нажмите Enter для выхода.")
