# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import random
# import sys
# sys.setrecursionlimit(5000)

vCubeSide = '.YYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWW'
# vCubeSide = '.000000000111111111222222222333333333444444444555555555'
vSide = {'up': 0, 'left': 1, 'front': 2, 'right': 3, 'back': 4, 'down': 5}
vCubeState = '.0000X00000000X00000000X00000000X00000000X00000000X0000'
vDone = False
recurse = 0


vCubes = [(7, 12, 19), (18, 25, 46), (1, 10, 39), (45, 16, 52),
          (21, 28, 9), (27, 34, 48), (3, 30, 37), (54, 36, 43),
          (24, 31), (20, 8), (22, 15), (26, 47),
          (2, 38), (33, 40), (13, 42), (53, 44),
          (6, 29), (4, 11), (35, 51), (17, 49)]
# vTurn = ['R', 'L', 'F', 'B', 'U', 'D',
#          'R"', 'L"', 'F"', 'B"', 'U"', 'D"',
#          'R2', 'L2', 'F2', 'B2', 'U2', 'D2',
#          'M', 'E', 'S', 'M"', 'E"', 'S"', 'M2', 'E2', 'S2', 'M"2', 'E"2', 'S"2']

vTurn = ['R', 'L', 'F', 'B', 'U', 'D', 'R"', 'L"', 'F"', 'B"', 'U"', 'D"', 'R2', 'L2', 'F2', 'B2', 'U2', 'D2']
vTurns = 'R L F B U D R" L" F" B" U" D" R2 L2 F2 B2 U2 D2'
vTurnsNext = {'R':'L F B U D L" F" B" U" D" L2 F2 B2 U2 D2',
              'L':'R F B U D R" F" B" U" D" R2 F2 B2 U2 D2',
              'F':'R L B U D R" L" B" U" D" R2 L2 B2 U2 D2',
              'B':'R L F U D R" L" F" U" D" R2 L2 F2 U2 D2',
              'U':'R L F B D R" L" F" B" D" R2 L2 F2 B2 D2',
              'D':'R L F B U R" L" F" B" U" R2 L2 F2 B2 U2',
              'R"':'L F B U D L" F" B" U" D" L2 F2 B2 U2 D2',
              'L"':'R F B U D R" F" B" U" D" R2 F2 B2 U2 D2',
              'F"':'R L B U D R" L" B" U" D" R2 L2 B2 U2 D2',
              'B"':'R L F U D R" L" F" U" D" R2 L2 F2 U2 D2',
              'U"':'R L F B D R" L" F" B" D" R2 L2 F2 B2 D2',
              'D"':'R L F B U R" L" F" B" U" R2 L2 F2 B2 U2',
              'R2':'L F B U D L" F" B" U" D" L2 F2 B2 U2 D2',
              'L2':'R F B U D R" F" B" U" D" R2 F2 B2 U2 D2',
              'F2':'R L B U D R" L" B" U" D" R2 L2 B2 U2 D2',
              'B2':'R L F U D R" L" F" U" D" R2 L2 F2 U2 D2',
              'U2':'R L F B D R" L" F" B" D" R2 L2 F2 B2 D2',
              'D2':'R L F B U R" L" F" B" U" R2 L2 F2 B2 U2'}

def show_sides(v_cube_side: str):
    fside = get_side(v_cube_side, 'front')
    bside = get_side(v_cube_side, 'back')
    lside = get_side(v_cube_side, 'left')
    rside = get_side(v_cube_side, 'right')
    dside = get_side(v_cube_side, 'down')
    uside = get_side(v_cube_side, 'up')
    print('front     back      left      right     down      up')
    print(fside[0], fside[1], fside[2], '   ', bside[0], bside[1], bside[2], '   ',
          lside[0], lside[1], lside[2], '   ', rside[0], rside[1], rside[2], '   ',
          dside[0], dside[1], dside[2], '   ', uside[0], uside[1], uside[2])
    print(fside[3], fside[4], fside[5], '   ', bside[3], bside[4], bside[5], '   ',
          lside[3], lside[4], lside[5], '   ', rside[3], rside[4], rside[5], '   ',
          dside[3], dside[4], dside[5], '   ', uside[3], uside[4], uside[5])
    print(fside[6], fside[7], fside[8], '   ', bside[6], bside[7], bside[8], '   ',
          lside[6], lside[7], lside[8], '   ', rside[6], rside[7], rside[8], '   ',
          dside[6], dside[7], dside[8], '   ', uside[6], uside[7], uside[8])


def show_text(v_cube: str):
    for iside in ('up', 'left', 'front', 'right', 'back', 'down'):
        vside = v_cube[vSide[iside] * 9 + 1: vSide[iside] * 9 + 10]
        print(iside, vside, end=' ')
    print('-')


def init_cube() -> str:
    global vCubeSide
    return vCubeSide


def init_state() -> str:
    return '.000010000000010000000010000000010000000010000000010000'


def check_solve(v_cube) -> bool:
    res = (v_cube == '.YYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWW')
    return res


def get_side(v_cube, side: str) -> str:
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        res = v_cube[vSide[side] * 9 + 1:vSide[side] * 9 + 10]
        return res
    else:
        print('get_side: error: set side: front, back, left, right, down, top')
        exit(1)


def _change_elements(v_cube: str, ind1, ind2, ind3, ind4: int) -> str:
    v_cube_list = list(v_cube)
    ind4str = v_cube_list[ind4]
    v_cube_list[ind4] = v_cube_list[ind3]
    v_cube_list[ind3] = v_cube_list[ind2]
    v_cube_list[ind2] = v_cube_list[ind1]
    v_cube_list[ind1] = ind4str
    return _to_str(v_cube_list)


def _to_str(v_list: list) -> str:
    res = ''
    for ind in range(0, len(v_list)):
        res = res + str(v_list.__getitem__(ind))
    return res

def _to_str_split(v_list: list) -> str:
    res = ''
    for ind in range(0, len(v_list)):
        if res == '':
            res = str(v_list.__getitem__(ind))
        else:
            res = res + ' ' + str(v_list.__getitem__(ind))
    return res


# front
def move_f(v_cube: str, count: int) -> str:
    for i in range(0
            , count):
        v_cube = _change_elements(v_cube, 19, 21, 27, 25)
        v_cube = _change_elements(v_cube, 20, 24, 26, 22)
        v_cube = _change_elements(v_cube, 7, 28, 48, 18)
        v_cube = _change_elements(v_cube, 8, 31, 47, 15)
        v_cube = _change_elements(v_cube, 9, 34, 46, 12)
    return v_cube


def move_f_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 19, 25, 27, 21)
        v_cube = _change_elements(v_cube, 20, 22, 26, 24)
        v_cube = _change_elements(v_cube, 7, 18, 48, 28)
        v_cube = _change_elements(v_cube, 8, 15, 47, 31)
        v_cube = _change_elements(v_cube, 9, 12, 46, 34)
    return v_cube


# back
def move_b(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 37, 39, 45, 43)
        v_cube = _change_elements(v_cube, 38, 42, 44, 40)
        v_cube = _change_elements(v_cube, 1, 16, 54, 30)
        v_cube = _change_elements(v_cube, 2, 13, 53, 33)
        v_cube = _change_elements(v_cube, 3, 10, 52, 36)
    return v_cube


def move_b_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 37, 43, 45, 39)
        v_cube = _change_elements(v_cube, 38, 40, 44, 42)
        v_cube = _change_elements(v_cube, 1, 30, 54, 16)
        v_cube = _change_elements(v_cube, 2, 33, 53, 13)
        v_cube = _change_elements(v_cube, 3, 36, 52, 10)
    return v_cube


# left
def move_l(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 10, 12, 18, 16)
        v_cube = _change_elements(v_cube, 11, 15, 17, 13)
        v_cube = _change_elements(v_cube, 1, 19, 46, 45)
        v_cube = _change_elements(v_cube, 4, 22, 49, 42)
        v_cube = _change_elements(v_cube, 7, 25, 52, 39)
    return v_cube


def move_l_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 10, 16, 18, 12)
        v_cube = _change_elements(v_cube, 11, 13, 17, 15)
        v_cube = _change_elements(v_cube, 1, 45, 46, 19)
        v_cube = _change_elements(v_cube, 4, 42, 49, 22)
        v_cube = _change_elements(v_cube, 7, 39, 52, 25)
    return v_cube


# right
def move_r(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 28, 30, 36, 34)
        v_cube = _change_elements(v_cube, 31, 29, 33, 35)
        v_cube = _change_elements(v_cube, 21, 3, 43, 48)
        v_cube = _change_elements(v_cube, 24, 6, 40, 51)
        v_cube = _change_elements(v_cube, 27, 9, 37, 54)
    return v_cube


def move_r_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 28, 34, 36, 30)
        v_cube = _change_elements(v_cube, 31, 35, 33, 29)
        v_cube = _change_elements(v_cube, 21, 48, 43, 3)
        v_cube = _change_elements(v_cube, 24, 51, 40, 6)
        v_cube = _change_elements(v_cube, 27, 54, 37, 9)
    return v_cube


# top
def move_u(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 1, 3, 9, 7)
        v_cube = _change_elements(v_cube, 2, 6, 8, 4)
        v_cube = _change_elements(v_cube, 21, 12, 39, 30)
        v_cube = _change_elements(v_cube, 20, 11, 38, 29)
        v_cube = _change_elements(v_cube, 19, 10, 37, 28)
    return v_cube


def move_u_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 1, 7, 9, 3)
        v_cube = _change_elements(v_cube, 2, 4, 8, 6)
        v_cube = _change_elements(v_cube, 21, 30, 39, 12)
        v_cube = _change_elements(v_cube, 20, 29, 38, 11)
        v_cube = _change_elements(v_cube, 19, 28, 37, 10)
    return v_cube


# down
def move_d(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 46, 48, 54, 52)
        v_cube = _change_elements(v_cube, 47, 51, 53, 49)
        v_cube = _change_elements(v_cube, 25, 34, 43, 16)
        v_cube = _change_elements(v_cube, 26, 35, 44, 17)
        v_cube = _change_elements(v_cube, 27, 36, 45, 18)
    return v_cube


def move_d_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 46, 52, 54, 48)
        v_cube = _change_elements(v_cube, 47, 49, 53, 51)
        v_cube = _change_elements(v_cube, 25, 16, 43, 34)
        v_cube = _change_elements(v_cube, 26, 17, 44, 35)
        v_cube = _change_elements(v_cube, 27, 18, 45, 36)
    return v_cube


def move_m(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 2, 20, 47, 44)
        v_cube = _change_elements(v_cube, 5, 23, 50, 41)
        v_cube = _change_elements(v_cube, 8, 26, 53, 38)
    return v_cube


def move_e(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 22, 31, 40, 13)
        v_cube = _change_elements(v_cube, 23, 32, 41, 14)
        v_cube = _change_elements(v_cube, 24, 33, 42, 15)
    return v_cube


def move_s(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 4, 29, 51, 17)
        v_cube = _change_elements(v_cube, 5, 32, 50, 14)
        v_cube = _change_elements(v_cube, 6, 35, 49, 11)
    return v_cube


def _formula_element(v_cube, element: str) -> str:
    # once
    if element == 'R': v_cube = move_r(v_cube, 1)
    if element == 'L': v_cube = move_l(v_cube, 1)
    if element == 'D': v_cube = move_d(v_cube, 1)
    if element == 'U': v_cube = move_u(v_cube, 1)
    if element == 'F': v_cube = move_f(v_cube, 1)
    if element == 'B': v_cube = move_b(v_cube, 1)
    if element == 'M': v_cube = move_m(v_cube, 1)
    if element == 'E': v_cube = move_e(v_cube, 1)
    if element == 'S': v_cube = move_s(v_cube, 1)
    if element == 'R"': v_cube = move_r_cc(v_cube, 1)
    if element == 'L"': v_cube = move_l_cc(v_cube, 1)
    if element == 'D"': v_cube = move_d_cc(v_cube, 1)
    if element == 'U"': v_cube = move_u_cc(v_cube, 1)
    if element == 'F"': v_cube = move_f_cc(v_cube, 1)
    if element == 'B"': v_cube = move_b_cc(v_cube, 1)
    if element == 'M"': v_cube = move_m(v_cube, 3)
    if element == 'E"': v_cube = move_e(v_cube, 3)
    if element == 'S"': v_cube = move_s(v_cube, 3)
    # twice
    if element == 'R2': v_cube = move_r(v_cube, 2)
    if element == 'L2': v_cube = move_l(v_cube, 2)
    if element == 'D2': v_cube = move_d(v_cube, 2)
    if element == 'U2': v_cube = move_u(v_cube, 2)
    if element == 'F2': v_cube = move_f(v_cube, 2)
    if element == 'B2': v_cube = move_b(v_cube, 2)
    if element == 'M2': v_cube = move_m(v_cube, 2)
    if element == 'E2': v_cube = move_e(v_cube, 2)
    if element == 'S2': v_cube = move_s(v_cube, 2)
    if element == 'R"2': v_cube = move_r_cc(v_cube, 2)
    if element == 'L"2': v_cube = move_l_cc(v_cube, 2)
    if element == 'D"2': v_cube = move_d_cc(v_cube, 2)
    if element == 'U"2': v_cube = move_u_cc(v_cube, 2)
    if element == 'F"2': v_cube = move_f_cc(v_cube, 2)
    if element == 'B"2': v_cube = move_b_cc(v_cube, 2)
    if element == 'M"2': v_cube = move_m(v_cube, 2)
    if element == 'E"2': v_cube = move_e(v_cube, 2)
    if element == 'S"2': v_cube = move_s(v_cube, 2)
    return v_cube


def formula(v_cube: str, v_formula: str) -> str:
    ff = []
    ff = v_formula.split(' ')
    for ind in range(0, len(ff)):
        v_cube = _formula_element(v_cube, str(ff.__getitem__(ind)))
    return v_cube


def calc_cube_state(v_cube: str) -> str:
    v_cube_state_list = list('.0000X00000000X00000000X00000000X00000000X00000000X0000')
    for iside in ('up', 'left', 'front', 'right', 'back', 'down'):
        vside = get_side(v_cube, iside)
        for j in range(0, 9):
            s = '0'
            if vside[j] == vside[4]: s = '1'
            v_cube_state_list[vSide[iside] * 9 + j + 1] = s
        v_cube_state_list[vSide[iside] * 9 + 5] = vside[4]
    v_cube_state = _to_str(v_cube_state_list)
    return v_cube_state


def calc_cube_done(v_cube_state: str) -> int:
    v_done = 0
    for ind in range(0, len(vCubes)):
        v_done_cube = 1
        v_cubes_item = vCubes.__getitem__(ind)
        for cind in range(0, len(v_cubes_item)):
            if v_cube_state[v_cubes_item.__getitem__(cind)] == '0': v_done_cube = 0
        # if v_done_cube == 1: print(v_cubes_item)
        v_done = v_done + v_done_cube
    return v_done


def scramble(count: int) -> str:
    v_turns_list = vTurns.split(' ')
    ff = []
    for ind in range(0, count):
        ff.append(v_turns_list[round((len(v_turns_list) - 1) * random())])
    return _to_str_split(ff)


def scramble_turns(count: int, v_turs:str) -> str:
    v_turns_list = v_turs.split(' ')
    ff = []
    for ind in range(0, count):
        ff.append(v_turns_list[round((len(v_turns_list) - 1) * random())])
    return _to_str_split(ff)


def find_next_move_2(v_cube: str, v_formula: str, v_turns: str, v_delta: int) -> str:
    v_turn_list = v_turns.split(' ')
    v_cube = formula(v_cube, v_formula)
    v_cube_done = calc_cube_done(calc_cube_state(v_cube))
    v_next_move = ''
    for ind in range(0, len(v_turn_list)):
        v_cube_done_new = calc_cube_done(calc_cube_state(formula(v_cube, str(v_turn_list[ind]))))
        if (v_cube_done_new >= v_cube_done - v_delta) and (v_cube_done_new > 0):
            v_next_move = str(v_turn_list[ind])
            break
    return v_next_move

def find_next_turns_2(v_cube: str, v_formula: str, v_turns: str, v_delta) -> str:
    v_turns_list = v_turns.split(' ')
    v_cube = formula(v_cube, v_formula)
    v_cube_done = calc_cube_done(calc_cube_state(v_cube))
    v_turns_new_list = []
    for ind in range(0, len(v_turns_list)):
        sind = str(v_turns_list[ind])
        cc = calc_cube_done(calc_cube_state(formula(v_cube, sind)))
        if (cc >= v_cube_done - v_delta):
            v_turns_new_list.append(sind)
    v_turns_new = _to_str_split(v_turns_new_list)
    return v_turns_new


def find_solve_2(v_cube: str, v_formula: str, v_turns: str):
    global vDone
    if vDone == True:
        return (0)
    else:
        if check_solve(formula(v_cube, v_formula)) == True:
            vDone = True
            print('Solve.')
            print(v_formula)
            return (0)
        v_formula_list = v_formula.split(' ')
        v_depth = len(v_formula_list)
        v_turns_new = find_next_turns_2(v_cube, v_formula, v_turns, 5)
        if v_depth <= 3: print('find: ', v_depth, v_cube, ' - ', v_formula, ' - ', v_turns_new)
        while (v_turns_new != '') and (v_depth < 7):
            v_next_move = str(v_turns_new.split(' ').__getitem__(0))
            v_formula_new = v_formula+' '+v_next_move
            v_turns_next = vTurnsNext[v_next_move]
            find_solve_2(v_cube, v_formula_new, v_turns_next)
            if vDone == True:
                return (0)
            else:
                v_turns_new_list = v_turns_new.split(' ')
                v_turns_new_list.__delitem__(v_turns_new_list.index(v_next_move))
                v_turns_new = _to_str_split(v_turns_new_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ff = 'U F R F" U'
    v_cube = init_cube()
    # ff = scramble_turns(5, 'U F R')
    ff = scramble(5)
    print(ff)
    v_cube = formula(v_cube, ff)
    v_cube_state = calc_cube_state(v_cube)
    v_cube_done = calc_cube_done(v_cube_state)
    show_sides(v_cube)
    print('cube:  ', end=' '), show_text(v_cube),
    print('state: ', end=' '), show_text(v_cube_state),
    print('cubes done: ', v_cube_done)
    # while not check_solve(v_cube):
    #     i += 1
    #     v_cube = _formula(v_cube, ff)
    #     v_cube_state = calc_cube_state(v_cube)
    #     show_text(v_cube), show_text(v_cube_state), print(calc_cube_done(v_cube_state))
    print(check_solve(v_cube))
    find_solve_2(v_cube, '', vTurns)
    print('cube scramble')
    print(ff)
    print(v_cube)
    # show_sides(v_cube)
    # print('cube:  ', end=' '), show_text(v_cube),
    # print('state: ', end=' '), show_text(v_cube_state),
    # print('cubes done: ', v_cube_done)

    # print((check_solve(v_cube)))
    print()

