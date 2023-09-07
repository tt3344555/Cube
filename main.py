# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#SideIndex = {'front': 'OOOOOOOOO', 'back': 'RRRRRRRRR', 'left': 'GGGGGGGGG', 'right': 'BBBBBBBBB', 'down': 'WWWWWWWWW', 'up': 'YYYYYYYYY'}
#dTurn = ['clock', 'unclock']
#vCube = 'OOOOOOOOO.RRRRRRRRR.GGGGGGGGG.BBBBBBBBB.WWWWWWWWW.YYYYYYYYY.'
vCubeSide = {'front': 'OOOOOOOOO', 'back': 'RRRRRRRRR', 'left': 'GGGGGGGGG', 'right': 'BBBBBBBBB', 'down': 'WWWWWWWWW', 'up': 'YYYYYYYYY'}


def check_solve() -> bool:
    global vCubeSide
    res = vCubeSide == {'front': 'OOOOOOOOO', 'back': 'RRRRRRRRR', 'left': 'GGGGGGGGG', 'right': 'BBBBBBBBB', 'down': 'WWWWWWWWW', 'up': 'YYYYYYYYY'}
    return res


def get_side(side: str) -> str:
    global vCubeSide
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        res = vCubeSide[side]
        return res
    else:
        print('get_side: error: set side: front, back, left, right, down, top')
        exit(1)


def set_side(side: str, value: str):
    global vCube
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        vCubeSide[side] = value
    else:
        print('set_side: error: set side: front, back, left, right, down, top')
        exit(1)

def side_to_str(side: set) -> str:
    res = str(side[0]+side[1]+side[2]+side[3]+side[4]+side[5]+side[6]+side[7]+side[8])
    return res

def turn_side(side: str, turn: str, count: int):
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

    set_side(side1, side_to_str(nside1))
    set_side(side2, side_to_str(nside2))
    set_side(side3, side_to_str(nside3))
    set_side(side4, side_to_str(nside4))


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
    print(vCubeSide)
    for i in range(6):
       move_back_clock()
       move_left_clock()
       move_back_unclock()
       move_left_unclock()
    print(vCubeSide)
    print(check_solve())

a1 = '1'
a2 = '2'
a3 = '3'
a = (a1, a2, a3)
print(a)
aCube = ('A','A','A'),('B','B','B')
#SideIndex['top'] = (6,'TTT')
#print (SideIndex)
#print (SideIndex['top'])