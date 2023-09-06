# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

vCubeSideSet = {'front': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                'back': ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                'left': ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                'right': ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
                'down': ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                'up': ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']}


def check_solve() -> bool:
    global vCubeSideSet
    res = vCubeSideSet == {'front': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                           'back': ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                           'left': ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                           'right': ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
                           'down': ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                           'up': ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']}
    return res


def get_side(side: str) -> set():
    global vCubeSideSet
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        res = vCubeSideSet[side]
#        print ('get_side: value', res)
        return res
    else:
        print('get_side: error: side value: front, back, left, right, down, top')
        exit(1)


def set_side(side: str, value: set()):
    global vCubeSideSet
#    print ('set_side: value', value)
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        vCubeSideSet[side] = value
    else:
        print('set_side: error: side value: front, back, left, right, down, top')
        exit(1)


def turn_side(side: str, turn: str):
    resside = get_side(side)
    resstr = resside[0]+resside[1]+resside[2]+resside[3]+resside[4]+resside[5]+resside[6]+resside[7]+resside[8]
    if turn == 'clock':
        res = [resstr[6], resstr[3], resstr[0], resstr[7], resstr[4], resstr[1], resstr[8], resstr[5], resstr[2]]
    elif turn == 'unclock':
        res = [resstr[2], resstr[5], resstr[8], resstr[1], resstr[4], resstr[7], resstr[0], resstr[3], resstr[6]]
    else:
        print('turn_side: error: turn value: clock, unclock')
        exit(1)
    set_side(side, res)


def turn_side_ext_old(side1: str, s11, s12, s13: int, side2: str, s21, s22, s23: int,
                  side3: str, s31, s32, s33: int, side4: str, s41, s42, s43: int):


    vside1 = str(get_side(side1))
    vside2 = str(get_side(side2))
    vside3 = str(get_side(side3))
    vside4 = str(get_side(side4))

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

def turn_side_ext(side1: str, s11, s12, s13: int, side2: str, s21, s22, s23: int,
                  side3: str, s31, s32, s33: int, side4: str, s41, s42, s43: int):
    vside1 = get_side(side1)
    vside1str = vside1[0]+vside1[1]+vside1[2]+vside1[3]+vside1[4]+vside1[5]+vside1[6]+vside1[7]+vside1[8]
    vside2 = get_side(side2)
    vside2str = vside2[0]+vside2[1]+vside2[2]+vside2[3]+vside2[4]+vside2[5]+vside2[6]+vside2[7]+vside2[8]
    vside3 = get_side(side3)
    vside3str = vside3[0]+vside3[1]+vside3[2]+vside3[3]+vside3[4]+vside3[5]+vside3[6]+vside3[7]+vside3[8]
    vside4 = get_side(side4)
    vside4str = vside4[0]+vside4[1]+vside4[2]+vside4[3]+vside4[4]+vside4[5]+vside4[6]+vside4[7]+vside4[8]

    nside1 = get_side(side1)
    nside2 = get_side(side2)
    nside3 = get_side(side3)
    nside4 = get_side(side4)

    nside2[s21] = vside1str[s11]
    nside2[s22] = vside1str[s12]
    nside2[s23] = vside1str[s13]

    nside3[s31] = vside2str[s21]
    nside3[s32] = vside2str[s22]
    nside3[s33] = vside2str[s23]

    nside4[s41] = vside3str[s31]
    nside4[s42] = vside3str[s32]
    nside4[s43] = vside3str[s33]

    nside1[s11] = vside4str[s41]
    nside1[s12] = vside4str[s42]
    nside1[s13] = vside4str[s43]

    set_side(side1, nside1)
    set_side(side2, nside2)
    set_side(side3, nside3)
    set_side(side4, nside4)


# front
def move_front_clock():
    turn_side('front', 'clock')
    turn_side_ext('up', 6, 7, 8, 'right', 0, 3, 6,
                  'down', 2, 1, 0, 'left', 8, 5, 2)


def move_front_unclock():
    turn_side('front', 'unclock')
    turn_side_ext('up', 6, 7, 8, 'left', 8, 5, 2,
                  'down', 2, 1, 0, 'right', 0, 3, 6)


# back
def move_back_clock():
    turn_side('back', 'clock')
    turn_side_ext('up', 0, 1, 2, 'left', 6, 3, 0,
                  'down', 8, 7, 6, 'right', 2, 5, 8)


def move_back_unclock():
    turn_side('back', 'unclock')
    turn_side_ext('up', 0, 1, 2, 'right', 2, 5, 8,
                  'down', 8, 7, 6, 'left', 6, 3, 0)


# left
def move_left_clock():
    turn_side('left', 'clock')
    turn_side_ext('up', 0, 3, 6, 'front', 0, 3, 6,
                  'down', 0, 3, 6, 'back', 8, 5, 2)


def move_left_unclock():
    turn_side('left', 'unclock')
    turn_side_ext('up', 0, 3, 6, 'back', 8, 5, 2,
                  'down', 0, 3, 6, 'front', 0, 3, 6)


# right
def move_right_clock():
    turn_side('right', 'clock')
    turn_side_ext('up', 2, 5, 8, 'back', 6, 3, 0,
                  'down', 2, 5, 8, 'front', 2, 5, 8)


def move_right_unclock():
    turn_side('right','unclock')
    turn_side_ext('up', 2, 5, 8, 'front', 2, 5, 8,
                  'down', 2, 5, 8, 'back', 6, 3, 0)


# top
def move_up_clock():
    turn_side('up', 'clock')
    turn_side_ext('front', 0, 1, 2, 'left', 0, 1, 2,
                  'back', 0, 1, 2, 'right', 0, 1, 2)


def move_up_unclock():
    turn_side('up', 'unclock')
    turn_side_ext('front', 0, 1, 2, 'right', 0, 1, 2,
                  'back', 0, 1, 2, 'left', 0, 1, 2)


# down
def move_down_clock():
    turn_side('down', 'clock')
    turn_side_ext('front', 6, 7, 8, 'right', 6, 7, 8,
                  'back', 6, 7, 8, 'left', 6, 7, 8)


def move_down_unclock():
    turn_side('down', 'unclock')
    turn_side_ext('front', 6, 7, 8, 'left', 6, 7, 8,
                  'back', 6, 7, 8, 'right', 6, 7, 8)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(vCubeSideSet)
    for i in range(1,7):
        move_right_clock()
        move_up_clock()
        move_right_unclock()
        move_up_unclock()
    print(vCubeSideSet)
    print(check_solve())
#    print(vCubeSideSet)
#    vCubeSideSet['front'][0] = 'Z'
#    print(vCubeSideSet)
