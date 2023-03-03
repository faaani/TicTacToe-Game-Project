def choose_position():
    p = ' 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 '
    while True:
        ask_inp = input('Enter X to choose X and O to choose O: ')
        if ask_inp == 'X' or ask_inp == 'O':
            break
    lstx = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    lsto = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    i = 0
    while True:
        if ask_inp == 'X':
            mark = lstx[i]
        elif ask_inp == 'O':
            mark = lsto[i]
        else:
            continue
        pos = input('Choose your position b/w 1-9: ')
        if pos not in p or pos == '':
            print('Wrong position, try again.')
            continue
        else:
            p = p.replace(pos, mark)
            i += 1
            print(p)
            if p[1] == p[5] == p[9] or p[25] == p[29] == p[33] or p[49] == p[53] == p[57] or p[1] == p[25] == p[
                49] or p[5] == p[29] == p[53] or p[9] == p[33] == p[57] or p[9] == p[29] == p[49] or p[1] == p[29] == p[
                57]:
                print('You win')
                play_again = input('Play again: enter Y or N ')
                while True:
                    if play_again == 'Y':
                        p = ' 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 '
                        i = 0
                        if ask_inp == 'X':
                            ask_inp = 'O'
                        else:
                            ask_inp = 'X'
                        break
                    elif play_again == 'N':
                        return 'Game Over'
            else:
                # LINE COPIED
                if any(char.isdigit() for char in p):
                    pass
                else:
                    print('Draw')
                    play_again = input('Play again: enter Y or N ')
                    while True:
                        if play_again == 'Y':
                            p = ' 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 '
                            i = 0
                            if ask_inp == 'X':
                                ask_inp = 'O'
                            else:
                                ask_inp = 'X'
                            break
                        elif play_again == 'N':
                            return 'Game Over'


print(choose_position())
