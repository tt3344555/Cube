# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

dCubeSide = ['front', 'back', 'left', 'right', 'bottom', 'top']
dSide = {'front': 0, 'back': 1, 'left': 2, 'right': 3, 'bottom': 4, 'top': 5}
dCubeColor = ['orange', 'red', 'green', 'blue', 'white', 'yellow']
dTurnDirect = ['clock', 'unclock']
vCube = "OOOOOOOOO.RRRRRRRRR.GGGGGGGGG.BBBBBBBBB.WWWWWWWWW.YYYYYYYYY."


# vCube = '123456789BBBBBBBBBLLLLLLLLLRRRRRRRRROOOOOOOOOTTTTTTTTT'
# sCubeAr = array (sCubeSide)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def getside(side: dCubeSide) -> str:
    global vCube
    res = vCube[dSide[side] * 10:dSide[side] * 10 + 9]
    #   print (res)
    return res


def setside(side: dCubeSide, value: str):
    global vCube
    if dSide[side] != 0:
        vCube = vCube[0:dSide[side] * 10 - 1] + '.' + value + '.' + vCube[dSide[side] * 10 + 10:len(vCube)]
    else:
        vCube = value + '.' + vCube[10:len(vCube)]


#    print (vCube)

def turnside(side: dCubeSide, turn: dTurnDirect, count: int):
    res = getside(side)
    if turn == 'clock':
        for i in range(count):
            res = res[6] + res[3] + res[0] + res[7] + res[4] + res[1] + res[8] + res[5] + res[2]
    else:
        for i in range(count):
            res = res[2] + res[5] + res[8] + res[1] + res[4] + res[7] + res[0] + res[3] + res[6]
    setside(side, res)


def setsideelement(side: dCubeSide, ind: int, value: str) -> str:
    side[ind] = value
    return side


def turnsideextclock(side1: dCubeSide, s11, s12, s13: int, side2: dCubeSide, s21, s22, s23: int,
                side3: dCubeSide, s31, s32, s33: int, side4: dCubeSide, s41, s42, s43: int):
    vside1 = getside(side1)
    vside2 = getside(side2)
    vside3 = getside(side3)
    vside4 = getside(side4)

    nside2 = ''
    for i in range(0, 9):
        if i == s21: nside2 = nside2 + vside1[s11]
        elif i == s22: nside2 = nside2 + vside1[s12]
        elif i == s23: nside2 = nside2 + vside1[s13]
        else: nside2 = nside2 + vside2[i]

    nside3 = ''
    for i in range(0, 9):
        if i == s31:  nside3 = nside3 + vside2[s21]
        elif i == s32: nside3 = nside3 + vside2[s22]
        elif i == s33: nside3 = nside3 + vside2[s23]
        else: nside3 = nside3 + vside3[i]

    nside4 = ''
    for i in range(0, 9):
        if i == s41: nside4 = nside4 + vside3[s31]
        elif i == s42: nside4 = nside4 + vside3[s32]
        elif i == s43: nside4 = nside4 + vside3[s33]
        else: nside4 = nside4 + vside4[i]

    nside1 = ''
    for i in range(0, 9):
        if i == s11: nside1 = nside1 + vside4[s41]
        elif i == s12: nside1 = nside1 + vside4[s42]
        elif i == s13: nside1 = nside1 + vside4[s43]
        else: nside1 = nside1 + vside1[i]

    setside(side1, nside1)
    setside(side2, nside2)
    setside(side3, nside3)
    setside(side4, nside4)

def moveFront():
    turnside('front', 'clock', 1)
    turnsideextclock('top', 6, 7, 8,
                'right', 0, 3, 6,
                'bottom', 0, 1, 2,
                'left', 2, 5, 8)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(vCube)
    #   print(getside('top'))
    #   setside('top','VVVVVVVVV')
    #   print(vCube)
    #    setside('top','VVVVVVVVV')
    print(vCube)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
