# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

vCubeSideStr = '.YYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWW'
vIndSide = {'up': 0, 'left': 1, 'front': 2, 'right': 3, 'back': 4, 'down': 5}


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
        res = vCubeSideStr[vIndSide[side] * 9 + 1:vIndSide[side] * 9 + 10]
        return res
    else:
        print('get_side: error: set side: front, back, left, right, down, top')
        exit(1)


#def set_side(side: str, value: str):
#    global vCubeSideStr
#    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
#        fside = get_side('front')
#        bside = get_side('back')
#        lside = get_side('left')
#        rside = get_side('right')
#        dside = get_side('down')
#        uside = get_side('up')
#        if side == 'front': fside = value
#        if side == 'back': bside = value
#        if side == 'left': lside = value
#        if side == 'right': rside = value
#        if side == 'down': dside = value
#        if side == 'up': uside = value
#        vCubeSideStr = '.' + uside + lside + fside + rside + bside + dside
#    else:
#        print('set_side: error: set side: front, back, left, right, down, top')
#        exit(1)


def _change_elements(ind1, ind2, ind3, ind4: int):
    global vCubeSideStr
    vcube = list(vCubeSideStr)
    ind4str = vcube[ind4]
    vcube[ind4] = vcube[ind3]
    vcube[ind3] = vcube[ind2]
    vcube[ind2] = vcube[ind1]
    vcube[ind1] = ind4str
    vCubeSideStr = _to_str(vcube)


def _to_str(side: list) -> str:
    res = ''
    for ind in range(0, len(side)):
        res = res + str(side.__getitem__(ind))
    return res


# front
def move_f_clock():
    _change_elements(19, 21, 27, 25)
    _change_elements(20, 24, 26, 22)
    _change_elements(7, 28, 48, 18)
    _change_elements(8, 31, 47, 15)
    _change_elements(9, 34, 46, 12)


def move_f_counterclock():
    _change_elements(19, 25, 27, 21)
    _change_elements(20, 22, 26, 24)
    _change_elements(7, 18, 48, 28)
    _change_elements(8, 15, 47, 31)
    _change_elements(9, 12, 46, 34)


# back
def move_b_clock():
    _change_elements(37, 39, 45, 43)
    _change_elements(38, 42, 44, 40)
    _change_elements(1, 16, 54, 30)
    _change_elements(2, 13, 53, 33)
    _change_elements(3, 10, 52, 36)


def move_b_counterclock():
    _change_elements(37, 43, 45, 39)
    _change_elements(38, 40, 44, 42)
    _change_elements(1, 30, 54, 16)
    _change_elements(2, 33, 53, 13)
    _change_elements(3, 36, 52, 10)


# left
def move_l_clock():
    _change_elements(10, 12, 18, 16)
    _change_elements(11, 15, 17, 13)
    _change_elements(1, 19, 46, 45)
    _change_elements(4, 22, 49, 42)
    _change_elements(7, 25, 52, 39)


def move_l_counterclock():
    _change_elements(10, 16, 18, 12)
    _change_elements(11, 13, 17, 15)
    _change_elements(1, 45, 46, 19)
    _change_elements(4, 42, 49, 22)
    _change_elements(7, 39, 52, 25)


# right
def move_r_clock():
    _change_elements(28, 30, 36, 34)
    _change_elements(31, 29, 33, 35)
    _change_elements(21, 3, 43, 48)
    _change_elements(24, 6, 40, 51)
    _change_elements(27, 9, 37, 54)


def move_r_counterclock():
    _change_elements(28, 34, 36, 30)
    _change_elements(31, 35, 33, 29)
    _change_elements(21, 48, 43, 3)
    _change_elements(24, 51, 40, 6)
    _change_elements(27, 54, 37, 9)


# top
def move_u_clock():
    _change_elements(1, 3, 9, 7)
    _change_elements(2, 6, 8, 4)
    _change_elements(21, 12, 39, 30)
    _change_elements(20, 11, 38, 29)
    _change_elements(19, 10, 37, 28)


def move_u_counterclock():
    _change_elements(1, 7, 9, 3)
    _change_elements(2, 4, 8, 6)
    _change_elements(21, 30, 39, 12)
    _change_elements(20, 29, 38, 11)
    _change_elements(19, 28, 37, 10)


# down
def move_d_clock():
    _change_elements(46, 48, 54, 52)
    _change_elements(47, 51, 53, 49)
    _change_elements(25, 34, 43, 16)
    _change_elements(26, 35, 44, 17)
    _change_elements(27, 36, 45, 18)


def move_d_counterclock():
    _change_elements(46, 52, 54, 48)
    _change_elements(47, 49, 53, 51)
    _change_elements(25, 16, 43, 34)
    _change_elements(26, 17, 44, 35)
    _change_elements(27, 18, 45, 36)

def move_m():
    _change_elements(2, 20, 47, 44)
    _change_elements(5, 23, 50, 41)
    _change_elements(8, 26, 53, 38)

def move_e():
    _change_elements(22, 31, 40, 13)
    _change_elements(23, 32, 41, 14)
    _change_elements(24, 33, 42, 15)

def move_s():
    _change_elements(4, 29, 51, 17)
    _change_elements(5, 32, 50, 14)
    _change_elements(6, 35, 49, 11)

def _formula_element(element: str):
    if element == 'R': move_r_clock()
    if element == 'R"': move_r_counterclock()
    if element == 'L': move_l_clock()
    if element == 'L"': move_l_counterclock()
    if element == 'D': move_d_clock()
    if element == 'D"': move_d_counterclock()
    if element == 'U': move_u_clock()
    if element == 'U"': move_u_counterclock()
    if element == 'F': move_f_clock()
    if element == 'F"': move_f_counterclock()
    if element == 'B': move_b_clock()
    if element == 'B"': move_b_counterclock()
    if element == 'M': move_m()
    if element == 'E': move_e()
    if element == 'S': move_s()


def _formula(formula: list):
    for ind in range(0, len(formula)):
        _formula_element(formula.__getitem__(ind))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _formula(['S'])
    show()
    i = 1
    while not check_solve():
        #        print(i, end=', ')
        i += 1
        _formula(['S'])
    print(vCubeSideStr, check_solve(), i)
