def insert_str(string, index, mark):
    return string[:index] + mark + string[index + 1:]  # method copied


def choose_position():
    print('Index Sample of TicTacToe')
    print(' 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ')

    p1 = '   |   |   '
    p2 = '-----------'
    p3 = '   |   |   '
    p4 = '-----------'
    p5 = '   |   |   '
    score_dict = {'player_x': 0, 'player_o': 0}
    while True:
        try:
            match = int(input('Enter the number of game you would like to play: '))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        if match == 1:
            print('Single match')
        elif match % 2 != 0:
            print(f'Best of {match}')
        else:
            print('Enter correct number')
            continue
        while True:
            ask_inp = input('Enter X to choose X and O to choose O: ')
            if ask_inp == 'X' or ask_inp == 'O':
                break

        lst_x = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        lst_o = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
        i = 0
        pos_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        while i < 9:
            if ask_inp == 'X':
                mark = lst_x[i]
            elif ask_inp == 'O':
                mark = lst_o[i]
            else:
                continue
            pos = input('Choose your position b/w 1-9: ')
            if pos.isdigit():
                pos = int(pos)
            else:
                continue

            if pos in pos_lst and len(pos_lst) > 0:
                if pos == 1:
                    p1 = insert_str(p1, 1, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                elif pos == 2:
                    p1 = insert_str(p1, 5, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                elif pos == 3:
                    p1 = insert_str(p1, -2, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                elif pos == 4:
                    p3 = insert_str(p3, 1, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                elif pos == 5:
                    p3 = insert_str(p3, 5, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                elif pos == 6:
                    p3 = insert_str(p3, -2, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                elif pos == 7:
                    p5 = insert_str(p5, 1, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                elif pos == 8:
                    p5 = insert_str(p5, 5, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                elif pos == 9:
                    p5 = insert_str(p5, -2, mark)
                    pos_lst.remove(pos)
                    print(f'{p1}\n{p2}\n{p3}\n{p4}\n{p5}')
                else:
                    continue
                i += 1
            else:
                print('Wrong position, try again.')
                continue

            if p1[1] == p1[5] == p1[-2] == 'X' or p3[1] == p3[5] == p3[-2] == 'X' or p5[1] == p5[5] == p5[-2] == 'X' or \
                    p1[1] == p3[1] == p5[1] == 'X' or p1[3] == p3[3] == p5[3] == 'X' or p1[-2] == p3[-2] == p5[
                -2] == 'X' or \
                    p1[1] == p3[5] == p5[-2] == 'X' or p1[-2] == p3[5] == p5[1] == 'X':
                print('Player X win')
                score_dict['player_x'] += 1
                print(score_dict)

                while match > 0:
                    match -= 1
                    p1 = '   |   |   '
                    p3 = '   |   |   '
                    p5 = '   |   |   '
                    i = 0
                    pos_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    if ask_inp == 'X':
                        ask_inp = 'O'
                    else:
                        ask_inp = 'X'
                    if match == 1:
                        print(f'{match} game left')
                        break
                    elif match > 1:
                        print(f'{match} games left')
                        break
                    elif match == 0:
                        print('Turns finished')
                        if score_dict['player_o'] > score_dict['player_x']:
                            print('player O is a winner')
                        elif score_dict['player_x'] > score_dict['player_o']:
                            print('Player_x is winner')
                        else:
                            print('Draw!')
                    while True:
                        play_again = input('Play again: enter Y or N ')
                        if play_again == 'Y':
                            score_dict = {'player_x': 0, 'player_o': 0}
                            while True:
                                try:
                                    match = int(input('Enter the number of game you would like to play: '))
                                except ValueError:
                                    print("Invalid input. Please enter an integer.")
                                if match == 1:
                                    print('Single match')
                                elif match % 2 != 0:
                                    print(f'Best of {match}')
                                else:
                                    print('Enter correct number')
                                    continue
                                ask_inp = input('Enter X to choose X and O to choose O: ')
                                if ask_inp == 'X' or ask_inp == 'O':
                                    break
                            break
                        elif play_again == 'N':
                            return 'Game Over'
                        else:
                            continue

            elif p1[1] == p1[5] == p1[-2] == 'O' or p3[1] == p3[5] == p3[-2] == 'O' or p5[1] == p5[5] == p5[
                -2] == 'O' or \
                    p1[1] == p3[1] == p5[1] == 'O' or p1[3] == p3[3] == p5[3] == 'O' or p1[-2] == p3[-2] == p5[
                -2] == 'O' or \
                    p1[1] == p3[5] == p5[-2] == 'O' or p1[-2] == p3[5] == p5[1] == 'O':
                print('Player O win')
                score_dict['player_o'] += 1
                print(score_dict)

                while match > 0:
                    match -= 1
                    p1 = '   |   |   '
                    p3 = '   |   |   '
                    p5 = '   |   |   '
                    i = 0
                    pos_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    if ask_inp == 'X':
                        ask_inp = 'O'
                    else:
                        ask_inp = 'X'
                    if match == 1:
                        print(f'{match} game left')
                        break
                    elif match > 1:
                        print(f'{match} games left')
                        break
                    elif match == 0:
                        print('Turns finished')
                        if score_dict['player_o'] > score_dict['player_x']:
                            print('player_o is winner')
                        elif score_dict['player_x'] > score_dict['player_o']:
                            print('Player_x is winner')
                        else:
                            print('Draw!')
                    while True:
                        play_again = input('Play again: enter Y or N ')
                        if play_again == 'Y':
                            score_dict = {'player_x': 0, 'player_o': 0}
                            while True:
                                try:
                                    match = int(input('Enter the number of game you would like to play: '))
                                except ValueError:
                                    print("Invalid input. Please enter an integer.")
                                if match == 1:
                                    print('Single match')
                                elif match % 2 != 0:
                                    print(f'Best of {match}')
                                else:
                                    print('Enter correct number')
                                    continue
                                ask_inp = input('Enter X to choose X and O to choose O: ')
                                if ask_inp == 'X' or ask_inp == 'O':
                                    break
                            break
                        elif play_again == 'N':
                            return 'Game Over'
                        else:
                            continue

            elif len(pos_lst) == 0:
                print('Draw')

                while match > 0:
                    match -= 1
                    p1 = '   |   |   '
                    p3 = '   |   |   '
                    p5 = '   |   |   '
                    i = 0
                    pos_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    if ask_inp == 'X':
                        ask_inp = 'O'
                    else:
                        ask_inp = 'X'
                    if match == 1:
                        print(f'{match} game left')
                        break
                    elif match > 1:
                        print(f'{match} games left')
                        break
                    elif match == 0:
                        print('Turns finished')
                        if score_dict['player_o'] > score_dict['player_x']:
                            print('player_o is winner')
                        elif score_dict['player_x'] > score_dict['player_o']:
                            print('Player_x is winner')
                        else:
                            print('Draw!')
                    while True:
                        play_again = input('Play again: enter Y or N ')
                        if play_again == 'Y':
                            score_dict = {'player_x': 0, 'player_o': 0}
                            while True:
                                try:
                                    match = int(input('Enter the number of game you would like to play: '))
                                except ValueError:
                                    print("Invalid input. Please enter an integer.")
                                if match == 1:
                                    print('Single match')
                                elif match % 2 != 0:
                                    print(f'Best of {match}')
                                else:
                                    print('Enter correct number')
                                    continue
                                ask_inp = input('Enter X to choose X and O to choose O: ')
                                if ask_inp == 'X' or ask_inp == 'O':
                                    break
                            break
                        elif play_again == 'N':
                            return 'Game Over'
                        else:
                            continue


print(choose_position()) 
