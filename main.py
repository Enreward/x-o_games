from game_engine import *

def setup():
    size_map = intro()
    table = [['-' for j in range(size_map)] for i in range(size_map)]
    turn = 0
    wrong_input = False
    dead_heat = False
    win = False
    possible_position = [(i, j) for i in range(size_map) for j in range(size_map)]
    winning_combinations = set_winning_combinations(size_map)
    return table, turn, wrong_input, dead_heat, win, possible_position, winning_combinations

def main():
    try:
        table, \
        turn, \
        wrong_input, \
        dead_heat, \
        win, \
        possible_position, \
        winning_combinations = setup()
    except KeyboardInterrupt:
        print("\n")
        print("Конец игры.")
        return
    draw(table)
    player = PLAYERS[turn]
    while not win:
        try:
            if wrong_input:
                print("Вы ошиблись. Пожалуйста, повторите ход.")
            position = player_input(player)
            possible_move = check_move(position, possible_position)
            if not possible_move:
                raise ValueError
            wrong_input = False
            
            table, possible_position = move(table, player, position, possible_position)
            draw(table)
            if not possible_position:
                dead_heat = True
            if winning(player, table, winning_combinations, dead_heat):
                print(outro(player, dead_heat))
                win = True
            
            turn = (turn + 1) % 2
            player = PLAYERS[turn]
        except KeyboardInterrupt:
            print(f"Игрок {player} сдался.")
            win = True
        except ValueError:
            wrong_input = True
            draw(table)
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    input("Нажмите Enter для выхода.")
