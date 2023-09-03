# This is a sample Python script.
from array import array

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

dCubeSide = ['front', 'back', 'left', 'right', 'bottom', 'top']
dSide = {'front':0, 'back':1, 'left':2, 'right':3, 'bottom':4, 'top':5}
dCubeColor = ['orange','red','green','blue','white','yellow']
dTurnDirect = ['clock','unclock']
#vCube = "GGGGGGGGGBBBBBBBBBRRRRRRRRROOOOOOOOOHHHHHHHHHYYYYYYYYY"
vCube = '123456789BBBBBBBBBLLLLLLLLLRRRRRRRRROOOOOOOOOTTTTTTTTT'
#sCubeAr = array (sCubeSide)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def getside (side : dCubeSide) -> str:
  res = vCube[dSide[side]*9:dSide[side]*9+9]
  print (res)
  return res

def setside (side : dCubeSide, value : str):
    global vCube
    if dSide[side] != 0 :
        vCube = vCube[0:dSide[side]*9-1] + value + vCube[dSide[side]*9+10:53]
    else:
      vCube = value + vCube[9:len(vCube)]
    print (vCube)

def turnside(side : dCubeSide, turn : dTurnDirect, count : int):
    res = getside(side)
    if turn == 'clock':
        for i in range(count) :
            res = res[6] + res[3] + res[0] + res[7] + res[4] + res[1] + res[8] + res[5] + res[2]
    else:
        for i in range(count):
            res = res[2] + res[5] + res[8] + res[1] + res[4] + res[7] + res[0] + res[3] + res[6]
    setside(side, res)

def moveR() : nothing



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(vCube)
    getside('top')
    #    setside('top','VVVVVVVVV')
    turnside('front', 'unclock', 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
