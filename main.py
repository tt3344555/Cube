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
    _turn_element(37, 43, 45, 39)
    _turn_element(38, 40, 44, 42)
    _turn_element(1, 30, 54, 16)
    _turn_element(2, 33, 53, 13)
    _turn_element(3, 36, 52, 10)


# left
def move_left_clockwise():
    _turn_element(10, 12, 18, 16)
    _turn_element(11, 15, 17, 13)
    _turn_element(1, 19, 46, 45)
    _turn_element(4, 22, 49, 42)
    _turn_element(7, 25, 52, 39)


def move_left_counterclockwise():
    _turn_element(10, 16, 18, 12)
    _turn_element(11, 13, 17, 15)
    _turn_element(1, 45, 46, 19)
    _turn_element(4, 42, 49, 22)
    _turn_element(7, 39, 52, 25)

# right
def move_right_clockwise():
    _turn_element(28, 30, 36, 34)
    _turn_element(31, 29, 33, 35)
    _turn_element(21, 3, 43, 48)
    _turn_element(24, 6, 40, 51)
    _turn_element(27, 9, 37, 54)

def move_right_counterclockwise():
    _turn_element(28, 34, 36, 30)
    _turn_element(31, 35, 33, 29)
    _turn_element(21, 48, 43, 3)
    _turn_element(24, 51, 40, 6)
    _turn_element(27, 54, 37, 9)

# top
def move_up_clockwise():
    _turn_element(1, 3, 9, 7)
    _turn_element(2, 6, 8, 4)
    _turn_element(21, 12, 39, 30)
    _turn_element(20, 11, 38, 29)
    _turn_element(19, 10, 37, 28)

def move_up_counterclockwise():
    _turn_element(1, 7, 9, 3)
    _turn_element(2, 4, 8, 6)
    _turn_element(21, 30, 39, 12)
    _turn_element(20, 29, 38, 11)
    _turn_element(19, 28, 37, 10)

# down
def move_down_clockwise():
    _turn_element(46, 48, 54, 52)
    _turn_element(47, 51, 53, 49)
    _turn_element(25, 34, 43, 16)
    _turn_element(26, 35, 44, 17)
    _turn_element(27, 36, 45, 18)

def move_down_counterclockwise():
    _turn_element(46, 52, 54, 48)
    _turn_element(47, 49, 53, 51)
    _turn_element(25, 16, 43, 34)
    _turn_element(26, 17, 44, 35)
    _turn_element(27, 18, 45, 36)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#    print(vCubeSideStr)
    move_down_clockwise()
    show()
    i = 1
    while not check_solve():
        print(i, end=', ')
        i += 1
        move_down_clockwise()
    print()
    print(vCubeSideStr, check_solve(), i)
