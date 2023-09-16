# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from random import random
# import sys
# sys.setrecursionlimit(5000)

g_faces_cube_width = 60
g_faces_cube = [0 for ind in range(54)]
g_faces_text = {'up': 'U', 'left': 'L', 'front': 'F', 'right': 'R', 'back': 'B', 'down': 'D', }
g_faces_colors = {'Y': "yellow", 'G': "green", 'R': "red", 'W': "white", 'B': "blue", 'O': "orange"}
g_faces_offset_x = {'up': 3, 'left': 0, 'front': 3, 'right': 6, 'back': 9, 'down': 3, }
g_faces_offset_y = {'up': 0, 'left': 3, 'front': 3, 'right': 3, 'back': 3, 'down': 6, }

g_cubes_side = '.YYYYYYYYYGGGGGGGGGOOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWW'
# g_cube = '.000000000111111111222222222333333333444444444555555555'
g_side = {'up': 0, 'left': 1, 'front': 2, 'right': 3, 'back': 4, 'down': 5}
# g_cube_state = '.0000X00000000X00000000X00000000X00000000X00000000X0000'
g_done = False
g_cube = '.YYYYYYYYYBBBBBBBBBRRRRRRRRRGGGGGGGGGOOOOOOOOOWWWWWWWWW'

g_cubes = [(7, 12, 19), (18, 25, 46), (1, 10, 39), (45, 16, 52),
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
        vside = v_cube[g_side[iside] * 9 + 1: g_side[iside] * 9 + 10]
        print(iside, vside, end=' ')
    print('-')


def init_cube() -> str:
    global g_cube
    g_cube = '.YYYYYYYYYBBBBBBBBBRRRRRRRRRGGGGGGGGGOOOOOOOOOWWWWWWWWW'
    return g_cube


def check_solve(v_cube) -> bool:
    global g_cube
    res = (v_cube == g_cube)
    return res


def get_side(v_cube, side: str) -> str:
    if side in ('front', 'back', 'left', 'right', 'down', 'up'):
        res = v_cube[g_side[side] * 9 + 1:g_side[side] * 9 + 10]
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

def move_m_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 2, 44, 47, 20)
        v_cube = _change_elements(v_cube, 5, 41, 50, 23)
        v_cube = _change_elements(v_cube, 8, 38, 53, 26)
    return v_cube


def move_e(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 22, 31, 40, 13)
        v_cube = _change_elements(v_cube, 23, 32, 41, 14)
        v_cube = _change_elements(v_cube, 24, 33, 42, 15)
    return v_cube

def move_e_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 22, 13, 40, 31)
        v_cube = _change_elements(v_cube, 23, 14, 41, 32)
        v_cube = _change_elements(v_cube, 24, 15, 42, 33)
    return v_cube

def move_s(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 4, 29, 51, 17)
        v_cube = _change_elements(v_cube, 5, 32, 50, 14)
        v_cube = _change_elements(v_cube, 6, 35, 49, 11)
    return v_cube

def move_s_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 4, 17, 51, 29)
        v_cube = _change_elements(v_cube, 5, 14, 50, 32)
        v_cube = _change_elements(v_cube, 6, 11, 49, 35)
    return v_cube


def move_rr(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_r(v_cube, count)
        v_cube = move_m_cc(v_cube, count)
    return v_cube

def move_rr_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_r_cc(v_cube, count)
        v_cube = move_m(v_cube, count)
    return v_cube

def move_ll(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_l(v_cube, count)
        v_cube = move_m(v_cube, count)
    return v_cube

def move_ll_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_l_cc(v_cube, count)
        v_cube = move_m_cc(v_cube, count)
    return v_cube

def move_uu(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_u(v_cube, count)
        v_cube = move_e_cc(v_cube, count)
    return v_cube

def move_uu_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_u_cc(v_cube, count)
        v_cube = move_e(v_cube, count)
    return v_cube

def move_dd(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_d(v_cube, count)
        v_cube = move_e(v_cube, count)
    return v_cube

def move_dd_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_d_cc(v_cube, count)
        v_cube = move_e_cc(v_cube, count)
    return v_cube

def move_ff(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_f(v_cube, count)
        v_cube = move_s(v_cube, count)
    return v_cube

def move_ff_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_f_cc(v_cube, count)
        v_cube = move_s_cc(v_cube, count)
    return v_cube

def move_bb(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_b(v_cube, count)
        v_cube = move_s_cc(v_cube, count)
    return v_cube

def move_bb_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_b_cc(v_cube, count)
        v_cube = move_s(v_cube, count)
    return v_cube

def move_xxx(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_rr(v_cube, count)
        v_cube = move_l_cc(v_cube, count)
    return v_cube

def move_xxx_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_rr_cc(v_cube, count)
        v_cube = move_l(v_cube, count)
    return v_cube


def move_yyy(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_u(v_cube, count)
        v_cube = move_dd_cc(v_cube, count)
    return v_cube

def move_yyy_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_u_cc(v_cube, count)
        v_cube = move_dd(v_cube, count)
    return v_cube

def move_zzz(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_bb_cc(v_cube, count)
        v_cube = move_f(v_cube, count)
    return v_cube

def move_zzz_cc(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = move_bb(v_cube, count)
        v_cube = move_f_cc(v_cube, count)
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
    if element == 'M"': v_cube = move_m_cc(v_cube, 1)
    if element == 'E"': v_cube = move_e_cc(v_cube, 1)
    if element == 'S"': v_cube = move_s_cc(v_cube, 1)
    if element == 'r': v_cube = move_rr(v_cube, 1)
    if element == 'l': v_cube = move_ll(v_cube, 1)
    if element == 'u': v_cube = move_uu(v_cube, 1)
    if element == 'd': v_cube = move_dd(v_cube, 1)
    if element == 'f': v_cube = move_ff(v_cube, 1)
    if element == 'b': v_cube = move_bb(v_cube, 1)
    if element == 'x': v_cube = move_xxx(v_cube, 1)
    if element == 'y': v_cube = move_yyy(v_cube, 1)
    if element == 'z': v_cube = move_zzz(v_cube, 1)
    if element == 'r"': v_cube = move_rr_cc(v_cube, 1)
    if element == 'l"': v_cube = move_ll_cc(v_cube, 1)
    if element == 'u"': v_cube = move_uu_cc(v_cube, 1)
    if element == 'd"': v_cube = move_dd_cc(v_cube, 1)
    if element == 'f"': v_cube = move_ff_cc(v_cube, 1)
    if element == 'b"': v_cube = move_bb_cc(v_cube, 1)
    if element == 'x"': v_cube = move_xxx_cc(v_cube, 1)
    if element == 'y"': v_cube = move_yyy_cc(v_cube, 1)
    if element == 'z"': v_cube = move_zzz_cc(v_cube, 1)
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
    if element == 'r2': v_cube = move_rr(v_cube, 2)
    if element == 'l2': v_cube = move_ll(v_cube, 2)
    if element == 'u2': v_cube = move_uu(v_cube, 2)
    if element == 'd2': v_cube = move_dd(v_cube, 2)
    if element == 'f2': v_cube = move_ff(v_cube, 2)
    if element == 'b2': v_cube = move_bb(v_cube, 2)
    if element == 'x2': v_cube = move_xxx(v_cube, 2)
    if element == 'y2': v_cube = move_yyy(v_cube, 2)
    if element == 'z2': v_cube = move_zzz(v_cube, 2)
    if element == 'r"2': v_cube = move_rr_cc(v_cube, 2)
    if element == 'l"2': v_cube = move_ll_cc(v_cube, 2)
    if element == 'u"2': v_cube = move_uu_cc(v_cube, 2)
    if element == 'd"2': v_cube = move_dd_cc(v_cube, 2)
    if element == 'f"2': v_cube = move_ff_cc(v_cube, 2)
    if element == 'b"2': v_cube = move_bb_cc(v_cube, 2)
    if element == 'x"2': v_cube = move_xxx_cc(v_cube, 2)
    if element == 'y"2': v_cube = move_yyy_cc(v_cube, 2)
    if element == 'z"2': v_cube = move_zzz_cc(v_cube, 2)
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
            v_cube_state_list[g_side[iside] * 9 + j + 1] = s
        v_cube_state_list[g_side[iside] * 9 + 5] = vside[4]
    v_cube_state = _to_str(v_cube_state_list)
    return v_cube_state


def calc_cube_done(v_cube: str) -> int:
    v_done = 0
    v_cube_state = calc_cube_state(v_cube)
    for ind in range(0, len(g_cubes)):
        v_done_cube = 1
        v_cubes_item = g_cubes.__getitem__(ind)
        for cind in range(0, len(v_cubes_item)):
            if v_cube_state[v_cubes_item.__getitem__(cind)] == '0': v_done_cube = 0
        # if v_done_cube == 1: print(v_cubes_item)
        v_done = v_done + v_done_cube
    return v_done


def scramble(count: int) -> str:
    v_turns_list = vTurns.split(' ')
    ss = v_turns_list[round((len(v_turns_list) - 1) * random())]
    ff = []
    ff.append(ss)
    for ind in range(0, count-1):
        ss = ff.__getitem__(ind)
        v_turns_list = vTurnsNext[str(ss)].split(' ')
        ss = v_turns_list[round((len(v_turns_list) - 1) * random())]
        ff.append(ss)
    return _to_str_split(ff)


def scramble_turns(count: int, v_turns: str) -> str:
    v_turns_list = v_turns.split(' ')
    ss = v_turns_list[round((len(v_turns_list) - 1) * random())]
    ff = []
    ff.append(ss)
    for ind in range(0, count-1):
        ss = ff.__getitem__(ind)
        v_turns_list = vTurnsNext[str(ss)].split(' ')
        ss = v_turns_list[round((len(v_turns_list) - 1) * random())]
        ff.append(ss)
    return _to_str_split(ff)


# def find_next_move_2(v_cube: str, v_formula: str, v_turns: str, v_delta: int) -> str:
#     v_turn_list = v_turns.split(' ')
#     v_cube = formula(v_cube, v_formula)
#     v_cube_done = calc_cube_done(v_cube)
#     v_next_move = ''
#     for ind in range(0, len(v_turn_list)):
#         v_cube_done_new = calc_cube_done(formula(v_cube, str(v_turn_list[ind])))
#         if (v_cube_done_new >= v_cube_done - v_delta) and (v_cube_done_new > 0):
#             v_next_move = str(v_turn_list[ind])
#             break
#     return v_next_move

def find_next_turns_2(v_cube: str, v_formula: str, v_turns: str, v_delta) -> str:
    v_turns_list = v_turns.split(' ')
    v_cube = formula(v_cube, v_formula)
    v_cube_done = calc_cube_done(v_cube)
    v_turns_new_list = []
    for ind in range(0, len(v_turns_list)):
        sind = str(v_turns_list[ind])
        cc = calc_cube_done(formula(v_cube, sind))
        if (cc >= v_cube_done - v_delta):
            v_turns_new_list.append(sind)
    v_turns_new = _to_str_split(v_turns_new_list)
    return v_turns_new


def find_solve_2(v_cube: str, v_formula: str, v_turns: str):
    global g_done
    if g_done == True:
        return (0)
    else:
        if check_solve(formula(v_cube, v_formula)) == True:
            g_done = True
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
            if g_done == True:
                return (0)
            else:
                v_turns_new_list = v_turns_new.split(' ')
                v_turns_new_list.__delitem__(v_turns_new_list.index(v_next_move))
                v_turns_new = _to_str_split(v_turns_new_list)

def draw_cube_faces(v_cube: str):
    for iside in ('up', 'left', 'front', 'right', 'back', 'down'):
        for cind in range(9):
            v_cube_x = 10 + (cind - (cind // 3) * 3) * g_faces_cube_width + g_faces_offset_x[iside] * g_faces_cube_width
            v_cube_y = 10 + (cind // 3) * g_faces_cube_width + g_faces_offset_y[iside] * g_faces_cube_width
            g_faces_cube[g_side[iside] * 9 + cind] = v_canvas.create_rectangle(v_cube_x, v_cube_y,
                     v_cube_x + g_faces_cube_width, v_cube_y + g_faces_cube_width,
                      fill=g_faces_colors[str(v_cube[g_side[iside] * 9 + cind + 1])])
            if cind == 4:
                v_canvas.create_text(v_cube_x + g_faces_cube_width // 2, v_cube_y + g_faces_cube_width // 2,
                                     font=('', 14), text=g_faces_text[iside], state=DISABLED)

def draw_cube_faces_update():
    global g_cube
    for ind in range(len(g_faces_cube)):
        v_canvas.itemconfig(g_faces_cube[ind], fill=g_faces_colors[str(g_cube[ind + 1])])
    # v_canvas.tag_raise(v_canvas.index(ind))

def draw_scramble():
    global g_cube
    ff = []
    ff = scramble(5)
    g_cube = init_cube()
    g_cube = formula(g_cube, ff)
    text1.delete("1.0", "end")
    text1.insert(INSERT, _to_str_split(ff)+'\n')
    draw_cube_faces_update()

def draw_move(v_move: str):
    global g_cube
    g_cube = formula(g_cube, v_move)
    draw_cube_faces_update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ff = 'U F R F" U'
    v_cube = init_cube()
    # ff = scramble_turns(5, 'U F R')
    ff = scramble(3)
    print(ff)
    v_cube = formula(v_cube, ff)
    v_cube_state = calc_cube_state(v_cube)
    v_cube_done = calc_cube_done(v_cube_state)
    # show_sides(v_cube)
    print('cube:  ', end=' '), show_text(v_cube),
    # print('state: ', end=' '), show_text(v_cube_state),
    # print('cubes done: ', v_cube_done)
    # print(check_solve(v_cube))
    root = Tk()
    root.wm_title('Cube example')
    v_canvas = Canvas(root, width=g_faces_cube_width * 18 + 30, height=g_faces_cube_width*9 + 30)
    v_canvas.pack()

    bfront = Button(text="F", height=2, width=4, relief=RAISED, command=lambda:draw_move('F'))
    bfront_window = v_canvas.create_window(10 + 12.5 * g_faces_cube_width, 10 , anchor=NW, window=bfront)
    bright = Button(text="R", height=2, width=4, relief=RAISED, command=lambda:draw_move('R'))
    bright_window = v_canvas.create_window(10 + 13.2 * g_faces_cube_width, 10 , anchor=NW, window=bright)
    bup = Button(text="U", height=2, width=4, relief=RAISED, command=lambda:draw_move('U'))
    bup_window = v_canvas.create_window(10 + 13.9 * g_faces_cube_width, 10 , anchor=NW, window=bup)
    bback = Button(text="B", height=2, width=4, relief=RAISED, command=lambda:draw_move('B'))
    bback_window = v_canvas.create_window(10 + 14.6 * g_faces_cube_width, 10 , anchor=NW, window=bback)
    bleft = Button(text="L", height=2, width=4, relief=RAISED, command=lambda:draw_move('L'))
    bleft_window = v_canvas.create_window(10 + 15.3 * g_faces_cube_width, 10 , anchor=NW, window=bleft)
    bdown = Button(text="D", height=2, width=4, relief=RAISED, command=lambda:draw_move('D'))
    bdown_window = v_canvas.create_window(10 + 16.0 * g_faces_cube_width, 10 , anchor=NW, window=bdown)

    bfrontcc = Button(text="F'", height=2, width=4, relief=RAISED, command=lambda:draw_move('F"'))
    bfrontcc_window = v_canvas.create_window(10 + 12.5 * g_faces_cube_width, 10 + .7 * g_faces_cube_width, anchor=NW, window=bfrontcc)
    brightcc = Button(text="R'", height=2, width=4, relief=RAISED, command=lambda:draw_move('R"'))
    brightcc_window = v_canvas.create_window(10 + 13.2 * g_faces_cube_width, 10 + .7 * g_faces_cube_width, anchor=NW, window=brightcc)
    bupcc = Button(text="U'", height=2, width=4, relief=RAISED, command=lambda:draw_move('U"'))
    bupcc_window = v_canvas.create_window(10 + 13.9 * g_faces_cube_width, 10 + .7 * g_faces_cube_width, anchor=NW, window=bupcc)
    bbackcc = Button(text="B'", height=2, width=4, relief=RAISED, command=lambda:draw_move('B"'))
    bbackcc_window = v_canvas.create_window(10 + 14.6 * g_faces_cube_width, 10 + .7 * g_faces_cube_width, anchor=NW, window=bbackcc)
    bleftcc = Button(text="L'", height=2, width=4, relief=RAISED, command=lambda:draw_move('L"'))
    bleftcc_window = v_canvas.create_window(10 + 15.3 * g_faces_cube_width, 10 + .7 * g_faces_cube_width, anchor=NW, window=bleftcc)
    bdowncc = Button(text="D'", height=2, width=4, relief=RAISED, command=lambda:draw_move('D"'))
    bdowncc_window = v_canvas.create_window(10 + 16.0 * g_faces_cube_width, 10 + .7 * g_faces_cube_width, anchor=NW, window=bdowncc)

    bfront2 = Button(text="F2", height=2, width=4, relief=RAISED, command=lambda:draw_move('F2'))
    bfront2_window = v_canvas.create_window(10 + 12.5 * g_faces_cube_width, 10 + 1.4 * g_faces_cube_width, anchor=NW, window=bfront2)
    bright2 = Button(text="R2", height=2, width=4, relief=RAISED, command=lambda:draw_move('R2'))
    bright2_window = v_canvas.create_window(10 + 13.2 * g_faces_cube_width, 10 + 1.4 * g_faces_cube_width, anchor=NW, window=bright2)
    bup2 = Button(text="U2", height=2, width=4, relief=RAISED, command=lambda:draw_move('U2'))
    bup2_window = v_canvas.create_window(10 + 13.9 * g_faces_cube_width, 10 + 1.4 * g_faces_cube_width, anchor=NW, window=bup2)
    bback2 = Button(text="B2", height=2, width=4, relief=RAISED, command=lambda:draw_move('B2'))
    bback2_window = v_canvas.create_window(10 + 14.6 * g_faces_cube_width, 10 + 1.4 * g_faces_cube_width, anchor=NW, window=bback2)
    bleft2 = Button(text="L2", height=2, width=4, relief=RAISED, command=lambda:draw_move('L2'))
    bleft2_window = v_canvas.create_window(10 + 15.3 * g_faces_cube_width, 10 + 1.4 * g_faces_cube_width, anchor=NW, window=bleft2)
    bdown2 = Button(text="D2", height=2, width=4, relief=RAISED, command=lambda:draw_move('D2'))
    bdown2_window = v_canvas.create_window(10 + 16.0 * g_faces_cube_width, 10 + 1.4 * g_faces_cube_width, anchor=NW, window=bdown2)

    bnewcubfaces = Button(text="Scramble", height=2, width=10, relief=RAISED, command=draw_scramble)
    bnewcubfaces_window  = v_canvas.create_window(10 + 10.5 * g_faces_cube_width, 10 + 6.5 * g_faces_cube_width, anchor=NW, window=bnewcubfaces)
    text1 = Text(height=7, width=39)
    text_window = v_canvas.create_window(10 + 6.2 * g_faces_cube_width, 10 , anchor=NW, window=text1)
    # display.insert(INSERT, g_cube)

    draw_cube_faces(g_cube)
    root.mainloop()
    # find_solve_2(v_cube, '', vTurns)
    # print(g_faces_cube)
    print('cube scramble')
    print(ff)
    print(v_cube)
    # show_sides(v_cube)
    # print('cube:  ', end=' '), show_text(v_cube),
    # print('state: ', end=' '), show_text(v_cube_state),
    # print('cubes done: ', v_cube_done)
    # print((check_solve(v_cube)))
    print('End.')

