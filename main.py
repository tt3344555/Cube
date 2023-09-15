# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

SideIndex = {'front': 0, 'back': 1, 'left': 2, 'right': 3, 'down': 4, 'up': 5}
dTurn = ['clock', 'unclock']
vCube = 'OOOOOOOOO.RRRRRRRRR.GGGGGGGGG.BBBBBBBBB.WWWWWWWWW.YYYYYYYYY.'


def check_solve() -> bool:
    global vCube
    res = vCube == 'OOOOOOOOO.RRRRRRRRR.GGGGGGGGG.BBBBBBBBB.WWWWWWWWW.YYYYYYYYY.'
    return res


def get_side(side: str) -> str:
    global vCube
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        res = vCube[SideIndex[side] * 10:SideIndex[side] * 10 + 9]
        return res
    else:
        print('get_side: error: set side: front, back, left, right, down, top')
        exit(1)


def set_side(side: str, value: str):
    global vCube
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        if SideIndex[side] != 0:
            vCube = vCube[0:SideIndex[side] * 10 - 1] + '.' + value + '.' + vCube[SideIndex[side] * 10 + 10:len(vCube)]
        else:
            vCube = value + '.' + vCube[10:len(vCube)]
    else:
        print('set_side: error: set side: front, back, left, right, down, top')
        exit(1)


def turn_side(side: str, turn: dTurn, count: int):
    res = get_side(side)
    if turn == 'clock':
        for i in range(count):
            res = res[6] + res[3] + res[0] + res[7] + res[4] + res[1] + res[8] + res[5] + res[2]
    elif turn == 'unclock':
        for i in range(count):
            res = res[2] + res[5] + res[8] + res[1] + res[4] + res[7] + res[0] + res[3] + res[6]
    else:
        print('turn_side: error: set turn: clock, unclock')
        exit(1)
    set_side(side, res)


def turn_side_ext(side1: str, s11, s12, s13: int, side2: str, s21, s22, s23: int,
                  side3: str, s31, s32, s33: int, side4: str, s41, s42, s43: int):
    vside1 = get_side(side1)
    vside2 = get_side(side2)
    vside3 = get_side(side3)
    vside4 = get_side(side4)

    nside2 = ''
    for i in range(0, 9):
        if i == s21:
            nside2 = nside2 + vside1[s11]
        elif i == s22:
            nside2 = nside2 + vside1[s12]
        elif i == s23:
            nside2 = nside2 + vside1[s13]
        else:
            nside2 = nside2 + vside2[i]

    nside3 = ''
    for i in range(0, 9):
        if i == s31:
            nside3 = nside3 + vside2[s21]
        elif i == s32:
            nside3 = nside3 + vside2[s22]
        elif i == s33:
            nside3 = nside3 + vside2[s23]
        else:
            nside3 = nside3 + vside3[i]

    nside4 = ''
    for i in range(0, 9):
        if i == s41:
            nside4 = nside4 + vside3[s31]
        elif i == s42:
            nside4 = nside4 + vside3[s32]
        elif i == s43:
            nside4 = nside4 + vside3[s33]
        else:
            nside4 = nside4 + vside4[i]

    nside1 = ''
    for i in range(0, 9):
        if i == s11:
            nside1 = nside1 + vside4[s41]
        elif i == s12:
            nside1 = nside1 + vside4[s42]
        elif i == s13:
            nside1 = nside1 + vside4[s43]
        else:
            nside1 = nside1 + vside1[i]

    set_side(side1, nside1)
    set_side(side2, nside2)
    set_side(side3, nside3)
    set_side(side4, nside4)


# front
def move_front_clock():
    turn_side('front', 'clock', 1)
    turn_side_ext('up', 6, 7, 8, 'right', 0, 3, 6,
                  'down', 2, 1, 0, 'left', 8, 5, 2)


def move_front_unclock():
    turn_side('front', 'unclock', 1)
    turn_side_ext('up', 6, 7, 8, 'left', 8, 5, 2,
                  'down', 2, 1, 0, 'right', 0, 3, 6)


# back
def move_back_clock():
    turn_side('back', 'clock', 1)
    turn_side_ext('up', 0, 1, 2, 'left', 6, 3, 0,
                  'down', 8, 7, 6, 'right', 2, 5, 8)


def move_back_unclock():
    turn_side('back', 'unclock', 1)
    turn_side_ext('up', 0, 1, 2, 'right', 2, 5, 8,
                  'down', 8, 7, 6, 'left', 6, 3, 0)


# left
def move_left_clock():
    turn_side('left', 'clock', 1)
    turn_side_ext('up', 0, 3, 6, 'front', 0, 3, 6,
                  'down', 0, 3, 6, 'back', 8, 5, 2)


def move_left_unclock():
    turn_side('left', 'unclock', 1)
    turn_side_ext('up', 0, 3, 6, 'back', 8, 5, 2,
                  'down', 0, 3, 6, 'front', 0, 3, 6)


# right
def move_right_clock():
    turn_side('right', 'clock', 1)
    turn_side_ext('up', 2, 5, 8, 'back', 6, 3, 0,
                  'down', 2, 5, 8, 'front', 2, 5, 8)


def move_right_unclock():
    turn_side('right', 'unclock', 1)
    turn_side_ext('up', 2, 5, 8, 'front', 2, 5, 8,
                  'down', 2, 5, 8, 'back', 6, 3, 0)


# top
def move_up_clock():
    turn_side('up', 'clock', 1)
    turn_side_ext('front', 0, 1, 2, 'left', 0, 1, 2,
                  'back', 0, 1, 2, 'right', 0, 1, 2)


def move_up_unclock():
    turn_side('up', 'unclock', 1)
    turn_side_ext('front', 0, 1, 2, 'right', 0, 1, 2,
                  'back', 0, 1, 2, 'left', 0, 1, 2)


# down
def move_down_clock():
    turn_side('down', 'clock', 1)
    turn_side_ext('front', 6, 7, 8, 'right', 6, 7, 8,
                  'back', 6, 7, 8, 'left', 6, 7, 8)


def move_down_unclock():
    turn_side('down', 'unclock', 1)
    turn_side_ext('front', 6, 7, 8, 'left', 6, 7, 8,
                  'back', 6, 7, 8, 'right', 6, 7, 8)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(vCube)
    for i in range(6):
       move_back_clock()
       move_left_clock()
       move_back_unclock()
       move_left_unclock()
    print(vCube)
    print(check_solve())

a1 = '1'
a2 = '2'
a3 = '3'
a = (a1, a2, a3)
print(a)

