# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter.messagebox import *
from cube import *
from cube import _to_str_split,_to_str
from const import *
# import sys
# sys.setrecursionlimit(5000)

g_faces_cube_width = 45
g_button_width = 40
g_faces_cube = [0 for ind in range(54)]
g_faces_text = {'up': 'U', 'left': 'L', 'front': 'F', 'right': 'R', 'back': 'B', 'down': 'D', }
g_faces_colors = {'Y': "yellow", 'G': "green", 'R': "red", 'W': "white", 'B': "blue", 'O': "orange"}
g_faces_offset_x = {'up': 3, 'left': 0, 'front': 3, 'right': 6, 'back': 9, 'down': 3, }
g_faces_offset_y = {'up': 0, 'left': 3, 'front': 3, 'right': 3, 'back': 3, 'down': 6, }
g_faces_block_offset_x = 10
g_faces_block_offset_y = 10
g_button_block_offset_x = 20
g_button_block_offset_y = 20



def draw_cube_faces(v_cube: str):
    for iside in ('up', 'left', 'front', 'right', 'back', 'down'):
        for cind in range(9):
            v_cube_x = 10 + (cind - (cind // 3) * 3) * g_faces_cube_width + g_faces_offset_x[iside] * g_faces_cube_width + g_faces_offset_x[iside]
            v_cube_y = 10 + (cind // 3) * g_faces_cube_width + g_faces_offset_y[iside] * g_faces_cube_width + g_faces_offset_y[iside]
            g_faces_cube[g_side[iside] * 9 + cind] = v_canvas.create_rectangle(v_cube_x, v_cube_y,
                     v_cube_x + g_faces_cube_width, v_cube_y + g_faces_cube_width,
                      fill=g_faces_colors[str(v_cube[g_side[iside] * 9 + cind + 1])])
            if cind == 4:
                v_canvas.create_text(v_cube_x + g_faces_cube_width // 2, v_cube_y + g_faces_cube_width // 2,
                                     font=('', 13), text=g_faces_text[iside], state=DISABLED)

def draw_cube_faces_update():
    global g_cube
    for ind in range(len(g_faces_cube)):
        v_canvas.itemconfig(g_faces_cube[ind], fill=g_faces_colors[str(g_cube[ind + 1])])
    # v_canvas.tag_raise(v_canvas.index(ind))

def draw_full():
    global g_cube
    g_cube = init_cube()
    text1.delete("1.0", "end")
    draw_cube_faces_update()

def draw_turns():
    global g_cube
    v_turns = str(bttofull_text.get("0.0", "end"))
    v_count = str(bttofull_count.get("0.0","end"))
    v_turns = v_turns[:-1]
    v_count = v_count[:-1]
    # showinfo(title='scramble', message=v_turns + ' - ' + v_count)
    if (v_turns != '') and (v_count != ''):
        for ind in range(int(v_count)):
            g_cube = formula(g_cube, v_turns)
    draw_cube_faces_update()


def draw_tofull():
    global g_cube
    v_cube = g_cube
        vside = v_cube[vSide[iside] * 9 + 1: vSide[iside] * 9 + 10]
        print(iside, vside, end=' ')
    print('-')


def init_cube() -> str:
    global vCubeSide
    return vCubeSide


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
        print('get_side: error: side value: front, back, left, right, down, top')
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


def move_e(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 22, 31, 40, 13)
        v_cube = _change_elements(v_cube, 23, 32, 41, 14)
        v_cube = _change_elements(v_cube, 24, 33, 42, 15)
    return v_cube


def move_s(v_cube: str, count: int):
    for i in range(0, count):
        v_cube = _change_elements(v_cube, 4, 29, 51, 17)
        v_cube = _change_elements(v_cube, 5, 32, 50, 14)
        v_cube = _change_elements(v_cube, 6, 35, 49, 11)
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
    if element == 'M"': v_cube = move_m(v_cube, 3)
    if element == 'E"': v_cube = move_e(v_cube, 3)
    if element == 'S"': v_cube = move_s(v_cube, 3)
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
    return v_cube


def formula(v_cube: str, v_formula: str) -> str:
    ff = []
    v_turns = str(bttofull_text.get("0.0", "end"))
    v_count = str(bttofull_count.get("0.0","end"))
    v_turns = v_turns[:-1]
    v_count = v_count[:-1]
    id_count = 0
    v_solved = False
    # showinfo(title='scramble', message=v_turns + ' - ' + v_count)
    if (v_turns != '') and (v_count != ''):
        # ff = scramble_turns_set(int(v_count), v_turns)
        while (v_solved == False) and (id_count <= int(v_count) - 1):
            v_cube = formula(v_cube, v_turns)
            v_solved = check_solve(v_cube)
            id_count += 1
        if v_solved == True:
            showinfo(title='turns to full', message='turns to full: ' + str(id_count))
        else:
            showinfo(title='turns to full', message='turns to full: not reached in ' + str(v_count) + ' turns')
    draw_cube_faces_update()



def draw_scramble():
    global g_cube
    ff = []
    v_turns = str(bscramble_text.get("0.0", "end"))
    v_count = str(bscramble_count.get("0.0","end"))
    v_turns = v_turns[:-1]
    v_count = v_count[:-1]
    # showinfo(title='scramble', message=v_turns + ' - ' + v_count)
    if (v_turns != '\n') and (v_count != '\n'):
        ff = scramble_turns_set(int(v_count), v_turns)
        g_cube = init_cube()
        g_cube = formula(g_cube, ff)
        text1.delete("0.0", "end")
        ffs = _to_str(ff)
        for ind in range(len(ffs)):
            text1.insert(END, ffs[ind])
        draw_cube_faces_update()

def draw_move(v_move: str):
    global g_cube
    g_cube = formula(g_cube, v_move)
    draw_cube_faces_update()

def draw_test():
    v_canvas.yview_scroll(1, 'units')

def draw_main():
    global bfront_window
    global root
    global v_canvas
    global v_canvas_2
    global text1
    global bscramble_text
    global bscramble_text_window
    global bscramble_count
    global bscramble_count_window
    global bttofull
    global bttofull_window
    global bttofull_text
    global bttofull_text_window
    global bttofull_count
    global bttofull_count_window

    root = Tk()
    root.wm_title('Cube example')
    v_canvas = Canvas(root, scrollregion=(0, 0, 30+g_faces_cube_width * 12 + 18 * g_button_width, 1000), width=30+g_faces_cube_width * 12 + 18 * g_button_width, height=g_faces_cube_width * 6 + 30) #9
    v_canvas.pack(side=LEFT, fill=Y)
    s = Scrollbar(root, command=v_canvas.yview)
    s.pack(side=RIGHT, fill=Y)
    v_canvas.configure(yscrollcommand=s.set)
    v_canvas.configure(yscrollincrement='2')
    bfront = Button(text="F", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('F'))
    bfront_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 0 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bfront)
    bright = Button(text="R", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('R'))
    bright_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 1 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bright)
    bup = Button(text="U", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('U'))
    bup_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 2 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bup)
    bback = Button(text="B", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('B'))
    bback_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 3 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bback)
    bleft = Button(text="L", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('L'))
    bleft_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 4 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bleft)
    bdown = Button(text="D", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('D'))
    bdown_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 5 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bdown)
    #
    bffront = Button(text="f", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('f'))
    bffront_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 6 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bffront)
    brright = Button(text="r", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('r'))
    brright_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 7 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=brright)
    buup = Button(text="u", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('u'))
    buup_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 8 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=buup)
    bbback = Button(text="b", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('b'))
    bbback_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 9 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bbback)
    blleft = Button(text="l", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('l'))
    bbleft_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 10 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=blleft)
    bddown = Button(text="d", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('d'))
    bddown_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 11 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bddown)
    #
    bm = Button(text="M", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('M'))
    bm_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 12 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bm)
    be = Button(text="E", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('E'))
    be_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 13 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=be)
    bs = Button(text="S", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('S'))
    bs_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 14 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bs)
    bx = Button(text="x", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('x'))
    bx_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 15 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bx)
    by = Button(text="y", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('y'))
    by_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 16 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=by)
    bz = Button(text="z", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('z'))
    bz_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 17 * g_button_width, 10 + 0 * g_button_width, anchor=NW, window=bz)
    #
    bfrontcc = Button(text="F'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('F\''))
    bfrontcc_window = v_canvas.create_window(g_faces_block_offset_x + 12* g_faces_cube_width + g_button_block_offset_x + 0 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bfrontcc)
    brightcc = Button(text="R'", height=2, width=4, font=('',9),  relief=RAISED, command=lambda:draw_move('R\''))
    brightcc_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 1 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=brightcc)
    bupcc = Button(text="U'", height=2, width=4,  font=('',9), relief=RAISED, command=lambda:draw_move('U\''))
    bupcc_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 2 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bupcc)
    bbackcc = Button(text="B'", height=2, width=4,  font=('',9), relief=RAISED, command=lambda:draw_move('B\''))
    bbackcc_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 3 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bbackcc)
    bleftcc = Button(text="L'", height=2, width=4,  font=('',9), relief=RAISED, command=lambda:draw_move('L\''))
    bleftcc_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 4 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bleftcc)
    bdowncc = Button(text="D'", height=2, width=4,  font=('',9), relief=RAISED, command=lambda:draw_move('D\''))
    bdowncc_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 5 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bdowncc)
    #
    bffront2 = Button(text="f'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('f\''))
    bffront2_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 6 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bffront2)
    brright2 = Button(text="r'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('r\''))
    brright2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 7 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=brright2)
    buup2 = Button(text="u'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('u\''))
    buup2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 8 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=buup2)
    bbback2 = Button(text="b'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('b\''))
    bbback2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 9 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bbback2)
    blleft2 = Button(text="l'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('l\''))
    bbleft2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 10 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=blleft2)
    bddown2 = Button(text="d'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('d\''))
    bddown2_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 11 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bddown2)
    #
    bmcc = Button(text="M'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('M\''))
    bmcc_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 12 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bmcc)
    becc = Button(text="E'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('E\''))
    becc_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 13 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=becc)
    bscc = Button(text="S'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('S\''))
    bscc_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 14 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bscc)
    bxcc = Button(text="x'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('x\''))
    bxcc_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 15 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bxcc)
    bycc = Button(text="y'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('y\''))
    bycc_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 16 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bycc)
    bzcc = Button(text="z'", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('z\''))
    bzcc_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 17 * g_button_width, 10 + 1.05 * g_button_width, anchor=NW, window=bzcc)
    #
    bfront2 = Button(text="F2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('F2'))
    bfront2_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 0 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bfront2)
    bright2 = Button(text="R2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('R2'))
    bright2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 1 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bright2)
    bup2 = Button(text="U2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('U2'))
    bup2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 2 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bup2)
    bback2 = Button(text="B2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('B2'))
    bback2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 3 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bback2)
    bleft2 = Button(text="L2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('L2'))
    bleft2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 4 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bleft2)
    bdown2 = Button(text="D2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('D2'))
    bdown2_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 5 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bdown2)
    #
    bffront2 = Button(text="f2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('f2'))
    bffront2_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 6 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bffront2)
    brright2 = Button(text="r2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('r2'))
    brright2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 7 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=brright2)
    buup2 = Button(text="u2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('u2'))
    buup2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 8 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=buup2)
    bbback2 = Button(text="b2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('b2'))
    bbback2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 9 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bbback2)
    blleft2 = Button(text="l2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('l2'))
    bbleft2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 10 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=blleft2)
    bddown2 = Button(text="d2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('d2 '))
    bddown2_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 11 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bddown2)
    #
    bm2 = Button(text="M2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('M2'))
    bm2_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 12 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bm2)
    be2 = Button(text="E2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('E2'))
    be2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 13 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=be2)
    bs2 = Button(text="S2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('S2'))
    bs2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 14 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bs2)
    bx2 = Button(text="x2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('x2'))
    bx2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 15 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bx2)
    by2 = Button(text="y2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('y2'))
    by2_window = v_canvas.create_window(g_faces_block_offset_x + 12  * g_faces_cube_width + g_button_block_offset_x + 16 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=by2)
    bz2 = Button(text="z2", height=2, width=4, font=('',9), relief=RAISED, command=lambda:draw_move('z2'))
    bz2_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x + 17 * g_button_width, 10 + 2.1 * g_button_width, anchor=NW, window=bz2)
    #
    bfull = Button(text="Full", height=1, width=8, relief=RAISED, command=draw_full)
    bfull_window  = v_canvas.create_window(10, 10 + 0.8 * g_button_width, anchor=NW, window=bfull)
    text1 = Text(height=7, width=20, wrap='none', font=('', 10))
    text_window = v_canvas.create_window(10 + 6.2 * g_faces_cube_width, 10 , anchor=NW, window=text1)
    bscramble = Button(text="Scramble", height=1, width=15, relief=RAISED, command=draw_scramble)
    bscramble_window  = v_canvas.create_window(g_faces_block_offset_x + 25 * g_faces_cube_width + g_button_block_offset_x + 10, 10 + 6 * g_button_block_offset_y + 10, anchor=NW, window=bscramble)
    bscramble_text = Text(height=1, width=66, wrap='none')
    bscramble_text_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x, 10 + 6 * g_button_block_offset_y + 10 , anchor=NW, window=bscramble_text)
    bscramble_count = Text(height=1, width=5, wrap='none')
    bscramble_count_window = v_canvas.create_window(g_faces_block_offset_x + 24 * g_faces_cube_width + g_button_block_offset_x, 10 + 6 * g_button_block_offset_y + 10 , anchor=NW, window=bscramble_count)
    bttofull = Button(text="Turns to full", height=1, width=15, relief=RAISED, command=draw_tofull)
    bttofull_window  = v_canvas.create_window(g_faces_block_offset_x + 25 * g_faces_cube_width + g_button_block_offset_x + 10, 10 + 7.5 * g_button_block_offset_y + 10, anchor=NW, window=bttofull)
    bttofull_text = Text(height=1, width=66, wrap='none')
    bttofull_text_window = v_canvas.create_window(g_faces_block_offset_x + 12 * g_faces_cube_width + g_button_block_offset_x, 10 + 7.5 * g_button_block_offset_y + 10 , anchor=NW, window=bttofull_text)
    bttofull_count = Text(height=1, width=5, wrap='none')
    bttofull_count_window = v_canvas.create_window(g_faces_block_offset_x + 24 * g_faces_cube_width + g_button_block_offset_x, 10 + 7.5 * g_button_block_offset_y + 10 , anchor=NW, window=bttofull_count)
    btest = Button(text="Test", height=1, width=15, relief=RAISED, command=draw_test)
    btest_window  = v_canvas.create_window(g_faces_block_offset_x + 25 * g_faces_cube_width + g_button_block_offset_x + 10, 10 + 11.5 * g_button_block_offset_y + 10, anchor=NW, window=btest)
    bturns = Button(text="Turns", height=1, width=15, relief=RAISED, command=draw_turns)
    bturns_window  = v_canvas.create_window(g_faces_block_offset_x + 25 * g_faces_cube_width + g_button_block_offset_x + 10, 10 + 9 * g_button_block_offset_y + 10, anchor=NW, window=bturns)
    # v_canvas.focus_set()
    # v_canvas_2 = Canvas(v_canvas, width=30+g_faces_cube_width * 12 + 18 * g_button_width, height=g_faces_cube_width * 9 + 30)
    # v_canvas_2.pack(side=BOTTOM)
    draw_cube_faces(g_cube)
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ff = 'U F R F" U'
    v_cube = init_cube()
    # ff = scramble_turns(5, 'U F R')
    # ff = scramble(3)
    # print(ff)
    # v_cube = formula(v_cube, ff)
    # v_cube = formula(v_cube, 'd2')
    # v_cube_state = calc_cube_state(v_cube)
    # v_cube_done = calc_cube_done(v_cube_state)
    # show_sides(v_cube)
    print('cube:  ', end=' '), show_text(v_cube)
    # print('state: ', end=' '), show_text(v_cube_state),
    # print('cubes done: ', v_cube_done)
    # print(check_solve(v_cube))
    # display.insert(INSERT, g_cube)
    draw_main()
    # find_solve_2(v_cube, '', vTurns)
    # print(g_faces_cube)
    print('cube scramble')
    # print(ff)
    print(v_cube)
    # show_sides(v_cube)
    # print('cube:  ', end=' '), show_text(v_cube),
    # print('state: ', end=' '), show_text(v_cube_state)
    # print('cubes done: ', v_cube_done)
    # print((check_solve(v_cube)))
    # print(F2L)
    print('End.')