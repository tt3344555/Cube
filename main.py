# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#vCubeSide = {'front': 'OOOOOOOOO', 'back': 'RRRRRRRRR', 'left': 'GGGGGGGGG', 'right': 'BBBBBBBBB',
#             'down': 'WWWWWWWWW', 'up': 'YYYYYYYYY'}
vCubeSideStr = '.YYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWW'
vInd = {'up': 0, 'left': 1, 'front': 2, 'right': 3, 'back': 4, 'down': 5}
def show():
    sidefront = get_side('front')
    sideback = get_side('back')
    sideleft = get_side('left')
    sideright = get_side('right')
    sidedown = get_side('down')
    sideup = get_side('up')
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


def show_text():
    print(vCubeSideStr)

def check_solve() -> bool:
    global vCubeSideStr
    res = (vCubeSideStr == '.YYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWW')
    return res


def get_side(side: str) -> str:
    global vCubeSideStr
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        res = vCubeSideStr[vInd[side]*9+1:vInd[side]*9+10]
        return res
    else:
        print('get_side: error: set side: front, back, left, right, down, top')
        exit(1)


def set_side(side: str, value: str):
    global vCubeSideStr
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        fside = get_side('front')
        bside = get_side('back')
        lside = get_side('left')
        rside = get_side('right')
        dside = get_side('down')
        uside = get_side('up')
        if side == 'front': fside = value
        if side == 'back': bside = value
        if side == 'left': lside = value
        if side == 'right': rside = value
        if side == 'down': dside = value
        if side == 'up': uside = value
        vCubeSideStr = '.' + uside + lside + fside + rside + bside + dside
    else:
        print('set_side: error: set side: front, back, left, right, down, top')
        exit(1)

def _turn_element(ind1, ind2, ind3, ind4 : int):
    global vCubeSideStr
    vcube = list(vCubeSideStr)
    tind = vcube[ind4]
    vcube[ind4] = vcube[ind3]
    vcube[ind3] = vcube[ind2]
    vcube[ind2] = vcube[ind1]
    vcube[ind1] = tind
    vCubeSideStr = _to_str(vcube)
    pass

def _to_str(side: list) -> str:
    res = ''
    for i in range(0,len(side)):
        res = res + str(side.__getitem__(i))
    return res


def turn_side_int(side: str, turn: str):
    res = get_side(side)
    if turn == 'clockwise':
        res = res[6] + res[3] + res[0] + res[7] + res[4] + res[1] + res[8] + res[5] + res[2]
    elif turn == 'counterclockwise':
        res = res[2] + res[5] + res[8] + res[1] + res[4] + res[7] + res[0] + res[3] + res[6]
    else:
        print('turn_side: error: set turn: clockwise, counterclockwise')
        exit(1)
    set_side(side, res)


def turn_side_ext(side1: str, s11, s12, s13: int, side2: str, s21, s22, s23: int,
                  side3: str, s31, s32, s33: int, side4: str, s41, s42, s43: int):
    vside1 = get_side(side1)
    vside2 = get_side(side2)
    vside3 = get_side(side3)
    vside4 = get_side(side4)

    nside1 = list(vside1)
    nside2 = list(vside2)
    nside3 = list(vside3)
    nside4 = list(vside4)

    nside2[s21] = vside1[s11]
    nside2[s22] = vside1[s12]
    nside2[s23] = vside1[s13]
    nside3[s31] = vside2[s21]
    nside3[s32] = vside2[s22]
    nside3[s33] = vside2[s23]
    nside4[s41] = vside3[s31]
    nside4[s42] = vside3[s32]
    nside4[s43] = vside3[s33]
    nside1[s11] = vside4[s41]
    nside1[s12] = vside4[s42]
    nside1[s13] = vside4[s43]

    set_side(side1, _to_str(nside1))
    set_side(side2, _to_str(nside2))
    set_side(side3, _to_str(nside3))
    set_side(side4, _to_str(nside4))


# front
def move_front_clockwise():
    _turn_element(19, 21, 27, 25)
    _turn_element(20, 24, 26, 22)
    _turn_element(7, 28, 48, 18)
    _turn_element(8, 31, 47, 15)
    _turn_element(9, 34, 46, 12)


def move_front_counterclockwise():
    _turn_element(19, 25, 27, 21)
    _turn_element(20, 22, 26, 24)
    _turn_element(7, 18, 48, 28)
    _turn_element(8, 15, 47, 31)
    _turn_element(9, 12, 46, 34)


# back
def move_back_clockwise():
    _turn_element(37, 39, 45, 43)
    _turn_element(38, 42, 44, 40)
    _turn_element(1, 16, 54, 30)
    _turn_element(2, 13, 53, 33)
    _turn_element(3, 10, 52, 36)


def move_back_counterclockwise():
    turn_side_int('back', 'counterclockwise')
    turn_side_ext('up', 0, 1, 2, 'right', 2, 5, 8,
                  'down', 8, 7, 6, 'left', 6, 3, 0)


# left
def move_left_clockwise():
    turn_side_int('left', 'clockwise')
    turn_side_ext('up', 0, 3, 6, 'front', 0, 3, 6,
                  'down', 0, 3, 6, 'back', 8, 5, 2)


def move_left_counterclockwise():
    turn_side_int('left', 'counterclockwise')
    turn_side_ext('up', 0, 3, 6, 'back', 8, 5, 2,
                  'down', 0, 3, 6, 'front', 0, 3, 6)


# right
def move_right_clockwise():
    turn_side_int('right', 'clockwise')
    turn_side_ext('up', 2, 5, 8, 'back', 6, 3, 0,
                  'down', 2, 5, 8, 'front', 2, 5, 8)


def move_right_counterclockwise():
    turn_side_int('right', 'counterclockwise')
    turn_side_ext('up', 2, 5, 8, 'front', 2, 5, 8,
                  'down', 2, 5, 8, 'back', 6, 3, 0)


# top
def move_up_clockwise():
    turn_side_int('up', 'clockwise')
    turn_side_ext('front', 0, 1, 2, 'left', 0, 1, 2,
                  'back', 0, 1, 2, 'right', 0, 1, 2)


def move_up_counterclockwise():
    turn_side_int('up', 'counterclockwise')
    turn_side_ext('front', 0, 1, 2, 'right', 0, 1, 2,
                  'back', 0, 1, 2, 'left', 0, 1, 2)


# down
def move_down_clockwise():
    turn_side_int('down', 'clockwise')
    turn_side_ext('front', 6, 7, 8, 'right', 6, 7, 8,
                  'back', 6, 7, 8, 'left', 6, 7, 8)


def move_down_counterclockwise():
    turn_side_int('down', 'counterclockwise')
    turn_side_ext('front', 6, 7, 8, 'left', 6, 7, 8,
                  'back', 6, 7, 8, 'right', 6, 7, 8)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(vCubeSideStr)
    move_back_clockwise()
    show()
    i = 1
    while not check_solve():
        print(i, end=', ')
        i += 1
        move_back_clockwise()
    print()
    print(vCubeSideStr, check_solve(), i)
