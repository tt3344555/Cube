# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

vCubeSide = '.YYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWW'
vSide = {'up': 0, 'left': 1, 'front': 2, 'right': 3, 'back': 4, 'down': 5}

vCubeState = '.000010000000010000000010000000010000000010000000010000'
vCubes = [(7, 12, 19), (18, 25, 46), (1, 10, 39), (45, 16, 52),
          (21, 28, 9), (27, 34, 48), (3, 30, 37), (54, 36, 43),
          (24, 31), (20, 8), (22, 15), (26, 47),
          (2, 38), (33, 40), (13, 42), (53, 44),
          (6, 29), (4, 11), (35, 51), (17, 49)]


def show_sides(v_cube_side: str):
    sidefront = get_side(v_cube_side, 'front')
    sideback = get_side(v_cube_side, 'back')
    sideleft = get_side(v_cube_side, 'left')
    sideright = get_side(v_cube_side, 'right')
    sidedown = get_side(v_cube_side, 'down')
    sideup = get_side(v_cube_side, 'up')
    print('front     back      left      right     down      up')
    print(sidefront[0], sidefront[1], sidefront[2], '   ', sideback[0], sideback[1], sideback[2], '   ',
          sideleft[0], sideleft[1], sideleft[2], '   ', sideright[0], sideright[1], sideright[2], '   ',
          sidedown[0], sidedown[1], sidedown[2], '   ', sideup[0], sideup[1], sideup[2])
    print(sidefront[3], sidefront[4], sidefront[5], '   ', sideback[3], sideback[4], sideback[5], '   ',
          sideleft[3], sideleft[4], sideleft[5], '   ', sideright[3], sideright[4], sideright[5], '   ',
          sidedown[3], sidedown[4], sidedown[5], '   ', sideup[3], sideup[4], sideup[5])
    print(sidefront[6], sidefront[7], sidefront[8], '   ', sideback[6], sideback[7], sideback[8], '   ',
          sideleft[6], sideleft[7], sideleft[8], '   ', sideright[6], sideright[7], sideright[8], '   ',
          sidedown[6], sidedown[7], sidedown[8], '   ', sideup[6], sideup[7], sideup[8])


def show_text(v_cube: str):
    for iside in ('up', 'left', 'front', 'right', 'back', 'down'):
        vside = v_cube[vSide[iside] * 9 + 1: vSide[iside] * 9 + 10]
        print(vside, end=' ')
    print()


def init_cube() -> str:
    return '.YYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWW'


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


def _to_str(side: list) -> str:
    res = ''
    for ind in range(0, len(side)):
        res = res + str(side.__getitem__(ind))
    return res


# front
def move_f_clock(v_cube: str, count: int) -> str:
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 19, 21, 27, 25)
        v_cube = _change_elements(v_cube, 20, 24, 26, 22)
        v_cube = _change_elements(v_cube, 7, 28, 48, 18)
        v_cube = _change_elements(v_cube, 8, 31, 47, 15)
        v_cube = _change_elements(v_cube, 9, 34, 46, 12)
        return v_cube


def move_f_counterclock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 19, 25, 27, 21)
        v_cube = _change_elements(v_cube, 20, 22, 26, 24)
        v_cube = _change_elements(v_cube, 7, 18, 48, 28)
        v_cube = _change_elements(v_cube, 8, 15, 47, 31)
        v_cube = _change_elements(v_cube, 9, 12, 46, 34)
        return v_cube


# back
def move_b_clock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 37, 39, 45, 43)
        v_cube = _change_elements(v_cube, 38, 42, 44, 40)
        v_cube = _change_elements(v_cube, 1, 16, 54, 30)
        v_cube = _change_elements(v_cube, 2, 13, 53, 33)
        v_cube = _change_elements(v_cube, 3, 10, 52, 36)
        return v_cube


def move_b_counterclock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 37, 43, 45, 39)
        v_cube = _change_elements(v_cube, 38, 40, 44, 42)
        v_cube = _change_elements(v_cube, 1, 30, 54, 16)
        v_cube = _change_elements(v_cube, 2, 33, 53, 13)
        v_cube = _change_elements(v_cube, 3, 36, 52, 10)
        return v_cube


# left
def move_l_clock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 10, 12, 18, 16)
        v_cube = _change_elements(v_cube, 11, 15, 17, 13)
        v_cube = _change_elements(v_cube, 1, 19, 46, 45)
        v_cube = _change_elements(v_cube, 4, 22, 49, 42)
        v_cube = _change_elements(v_cube, 7, 25, 52, 39)
        return v_cube


def move_l_counterclock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 10, 16, 18, 12)
        v_cube = _change_elements(v_cube, 11, 13, 17, 15)
        v_cube = _change_elements(v_cube, 1, 45, 46, 19)
        v_cube = _change_elements(v_cube, 4, 42, 49, 22)
        v_cube = _change_elements(v_cube, 7, 39, 52, 25)
        return v_cube


# right
def move_r_clock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 28, 30, 36, 34)
        v_cube = _change_elements(v_cube, 31, 29, 33, 35)
        v_cube = _change_elements(v_cube, 21, 3, 43, 48)
        v_cube = _change_elements(v_cube, 24, 6, 40, 51)
        v_cube = _change_elements(v_cube, 27, 9, 37, 54)
        return v_cube


def move_r_counterclock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 28, 34, 36, 30)
        v_cube = _change_elements(v_cube, 31, 35, 33, 29)
        v_cube = _change_elements(v_cube, 21, 48, 43, 3)
        v_cube = _change_elements(v_cube, 24, 51, 40, 6)
        v_cube = _change_elements(v_cube, 27, 54, 37, 9)
        return v_cube


# top
def move_u_clock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 1, 3, 9, 7)
        v_cube = _change_elements(v_cube, 2, 6, 8, 4)
        v_cube = _change_elements(v_cube, 21, 12, 39, 30)
        v_cube = _change_elements(v_cube, 20, 11, 38, 29)
        v_cube = _change_elements(v_cube, 19, 10, 37, 28)
        return v_cube


def move_u_counterclock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 1, 7, 9, 3)
        v_cube = _change_elements(v_cube, 2, 4, 8, 6)
        v_cube = _change_elements(v_cube, 21, 30, 39, 12)
        v_cube = _change_elements(v_cube, 20, 29, 38, 11)
        v_cube = _change_elements(v_cube, 19, 28, 37, 10)
        return v_cube


# down
def move_d_clock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 46, 48, 54, 52)
        v_cube = _change_elements(v_cube, 47, 51, 53, 49)
        v_cube = _change_elements(v_cube, 25, 34, 43, 16)
        v_cube = _change_elements(v_cube, 26, 35, 44, 17)
        v_cube = _change_elements(v_cube, 27, 36, 45, 18)
        return v_cube


def move_d_counterclock(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 46, 52, 54, 48)
        v_cube = _change_elements(v_cube, 47, 49, 53, 51)
        v_cube = _change_elements(v_cube, 25, 16, 43, 34)
        v_cube = _change_elements(v_cube, 26, 17, 44, 35)
        v_cube = _change_elements(v_cube, 27, 18, 45, 36)
        return v_cube


def move_m(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 2, 20, 47, 44)
        v_cube = _change_elements(v_cube, 5, 23, 50, 41)
        v_cube = _change_elements(v_cube, 8, 26, 53, 38)
        return v_cube


def move_e(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 22, 31, 40, 13)
        v_cube = _change_elements(v_cube, 23, 32, 41, 14)
        v_cube = _change_elements(v_cube, 24, 33, 42, 15)
        return v_cube


def move_s(v_cube: str, count: int):
    for i in range(1, count):
        v_cube = _change_elements(v_cube, 4, 29, 51, 17)
        v_cube = _change_elements(v_cube, 5, 32, 50, 14)
        v_cube = _change_elements(v_cube, 6, 35, 49, 11)
        return v_cube


def calc_cube_state(v_cube: str) -> str:
    v_cube_state_list = list('.000010000000010000000010000000010000000010000000010000')
    for iside in ('up', 'left', 'front', 'right', 'back', 'down'):
        vside = get_side(v_cube, iside)
        for j in range(0, 9):
            s = '0'
            if vside[j] == vside[4]: s = '1'
            v_cube_state_list[vSide[iside] * 9 + j + 1] = s
    v_cube_state = _to_str(v_cube_state_list)
    return v_cube_state


def calc_cube_done(v_cube_state: str) -> int:
    v_done = 0
    v_done_cube = 0
    for ind in range(0, len(vCubes)):
        for cind in range(0, len(vCubes.__getitem__(ind))):
            v_done_cube = 1
            if v_cube_state[vCubes.__getitem__(ind).__getitem__(cind)] == '0': v_done_cube = 0
        v_done = v_done + v_done_cube
    return v_done


def _formula_element(v_cube, element: str) -> str:
    # once
    if element == 'R': v_cube = move_r_clock(v_cube, 1)
    if element == 'R"': v_cube = move_r_counterclock(v_cube, 1)
    if element == 'L': v_cube = move_l_clock(v_cube, 1)
    if element == 'L"': v_cube = move_l_counterclock(v_cube, 1)
    if element == 'D': v_cube = move_d_clock(v_cube, 1)
    if element == 'D"': v_cube = move_d_counterclock(v_cube, 1)
    if element == 'U': v_cube = move_u_clock(v_cube, 1)
    if element == 'U"': v_cube = move_u_counterclock(v_cube, 1)
    if element == 'F': v_cube = move_f_clock(v_cube, 1)
    if element == 'F"': v_cube = move_f_counterclock(v_cube, 1)
    if element == 'B': v_cube = move_b_clock(v_cube, 1)
    if element == 'B"': v_cube = move_b_counterclock(v_cube, 1)
    if element == 'M': v_cube = move_m(v_cube, 1)
    if element == 'E': v_cube = move_e(v_cube, 1)
    if element == 'S': v_cube = move_s(v_cube, 1)
    # twice
    if element == 'R2': v_cube = move_r_clock(v_cube, 2)
    if element == 'R"2': v_cube = move_r_counterclock(v_cube, 2)
    if element == 'L2': v_cube = move_l_clock(v_cube, 2)
    if element == 'L"2': v_cube = move_l_counterclock(v_cube, 2)
    if element == 'D2': v_cube = move_d_clock(v_cube, 2)
    if element == 'D"2': v_cube = move_d_counterclock(v_cube, 2)
    if element == 'U2': v_cube = move_u_clock(v_cube, 2)
    if element == 'U"2': v_cube = move_u_counterclock(v_cube, 2)
    if element == 'F2': v_cube = move_f_clock(v_cube, 2)
    if element == 'F"2': v_cube = move_f_counterclock(v_cube, 2)
    if element == 'B2': v_cube = move_b_clock(v_cube, 2)
    if element == 'B"2': v_cube = move_b_counterclock(v_cube, 2)
    if element == 'M2': v_cube = move_m(v_cube, 2)
    if element == 'E2': v_cube = move_e(v_cube, 2)
    if element == 'S2': v_cube = move_s(v_cube, 2)
    return v_cube


def _formula(v_cube, formula: list) -> str:
    for ind in range(0, len(formula)):
        v_cube = _formula_element(v_cube, formula.__getitem__(ind))
    return v_cube


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ff = ['U2', 'R2', 'U"2', 'R"2']
    v_cube = init_cube()
    v_cube = _formula(v_cube, ff)
    v_cube_state = calc_cube_state(v_cube)
    show_sides(v_cube), show_text(v_cube), show_text(v_cube_state), print(calc_cube_done(v_cube_state))
    i = 1
    while not check_solve(v_cube):
        i += 1
        v_cube = _formula(v_cube, ff)
        v_cube_state = calc_cube_state(v_cube)
        show_text(v_cube), show_text(v_cube_state), print(calc_cube_done(v_cube_state))
    print(check_solve(v_cube), i)
