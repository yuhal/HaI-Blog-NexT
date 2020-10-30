---
title: Python-《Python-实现-2048-游戏》实验报告
categories: Python
---
![74340da14d79fae0a21de03d44699f80b6c624f3.jpg](https://upload-images.jianshu.io/upload_images/15325592-43ea75d2662a8fd9.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  2048 游戏

> wiki:《2048》是一款单人在线和移动端游戏，由19岁的意大利人 Gabriele Cirulli 于2014年3月开发。游戏任务是在一个网格上滑动小方块来进行组合，直到形成一个带有有数字2048的方块。

#  代码

```
#  -*- coding: utf-8 -*-
import sys
import random
import curses
from itertools import chain

class Action(object):
    '''
    游戏控制显示
    '''
    UP = 'up'
    LEFT = 'left'
    DOWN = 'down'
    RIGHT = 'right'
    RESTART = 'restart'
    EXIT = 'exit'

    letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
    #  字母编码，ord返回对应的十进制整数
    actions = [UP, LEFT, DOWN, RIGHT, RESTART, EXIT]
    #  用户行为
    actions_dict = dict(zip(letter_codes, actions * 2))
    #  将字母的十进制整数和用户行为一一对应组合起来,并转换成字典类型
    #  因为不区分大小写，所以这里用户行为需要*2

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get(self):
        char = "N"
        while char not in self.actions_dict:
            char = self.stdscr.getch()
        return self.actions_dict[char]


class Grid(object):

    def __init__(self, size):
        self.size = size
        self.cells = None
        self.reset()

    def reset(self):
        self.cells = [[0 for i in range(self.size)] for j in range(self.size)]
        #  初始化一个二维数组，值都是0，作为棋盘的每格。
        self.add_random_item()
        self.add_random_item()

    def add_random_item(self):
        '''
        随机在某个格子输出2或4
        '''
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.cells[i][j] == 0]
        (i, j) = random.choice(empty_cells)
        self.cells[i][j] = 4 if random.randrange(100) >= 90 else 2

    def transpose(self):
        '''
        利用 Python 内置的 zip(*) 方法来进行矩阵转置
        '''
        self.cells = [list(row) for row in zip(*self.cells)]

    def invert(self):
        '''
        将矩阵的每一行倒序
        '''
        self.cells = [row[::-1] for row in self.cells]

    @staticmethod
    def move_row_left(row):
        '''
        一行向左合并
        '''
        def tighten(row):
            '''把零散的非零单元挤到一块'''
            new_row = [i for i in row if i != 0]
            #  先将非零的元素全拿出来加入到新列表
            new_row += [0 for i in range(len(row) - len(new_row))]
            #  按照原列表的大小，给新列表后面补零
            return new_row

        def merge(row):
            '''对邻近元素进行合并'''
            pair = False
            new_row = []
            for i in range(len(row)):
                if pair:
                    new_row.append(2 * row[i])
                    #  合并后，加入乘 2 后的元素在 0 元素后面
                    GameManager.score += 2 * row[i]
                    #  更新分数
                    pair = False
                else:
                    #  判断邻近元素能否合并
                    if i + 1 < len(row) and row[i] == row[i + 1]:
                        pair = True
                        new_row.append(0)
                        #  可以合并时，新列表加入元素 0
                    else:
                        new_row.append(row[i])
                        #  不能合并，新列表中加入该元素
            #  断言合并后不会改变行列大小，否则报错
            assert len(new_row) == len(row)
            return new_row
        #  先挤到一块再合并再挤到一块
        return tighten(merge(tighten(row)))

    def move_left(self):
        self.cells = [self.move_row_left(row) for row in self.cells]

    def move_right(self):
        self.invert()
        self.move_left()
        self.invert()

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    @staticmethod
    def row_can_move_left(row):
        def change(i):
            if row[i] == 0 and row[i + 1] != 0:
                return True
            if row[i] != 0 and row[i + 1] == row[i]:
                return True
            return False
        return any(change(i) for i in range(len(row) - 1))

    def can_move_left(self):
        return any(self.row_can_move_left(row) for row in self.cells)

    def can_move_right(self):
        self.invert()
        can = self.can_move_left()
        self.invert()
        return can

    def can_move_up(self):
        self.transpose()
        can = self.can_move_left()
        self.transpose()
        return can

    def can_move_down(self):
        self.transpose()
        can = self.can_move_right()
        self.transpose()
        return can

    def can_move_restart(self):
        self.transpose()
        can = self.can_move_down()
        self.transpose()
        return can

    def can_move_exit(self):
        self.transpose()
        can = self.can_move_up()
        self.transpose()
        return can

class Screen(object):
    '''
    棋盘类
    '''
    help_string1 = '(W)up (S)down (A)left (D)right'
    help_string2 = '     (R)Restart (Q)Exit'
    over_string = '           GAME OVER'
    win_string = '          YOU WIN!'

    def __init__(self, screen=None, grid=None, score=0, best_score=0, over=False, win=False):
        self.grid = grid
        self.score = score
        self.over = over
        self.win = win
        self.screen = screen
        self.counter = 0

    def cast(self, string):
        '''
        绘制函数
        '''
        self.screen.addstr(string + '\n')
        #  addstr() 方法将传入的内容展示到终端

    def draw_row(self, row):
        '''
        绘制竖直分割线的函数
        '''
        self.cast(''.join('|{: ^5}'.format(num) if num > 0 else '|     ' for num in row) + '|')

    def draw(self):
        self.screen.clear()
        #  清空屏幕
        self.cast('SCORE: ' + str(self.score))
        for row in self.grid.cells:
            self.cast('+-----' * self.grid.size + '+')
            self.draw_row(row)
        self.cast('+-----' * self.grid.size + '+')
        #  绘制分数

        if self.win:
            self.cast(self.win_string)
        else:
            if self.over:
                self.cast(self.over_string)
            else:
                self.cast(self.help_string1)

        self.cast(self.help_string2)
        #  绘制提示文字


class GameManager(object):

    score = 0
    '''
    游戏状态控制类
    '''

    def __init__(self, size=4, win_num=2048):
        self.size = size 
        #  棋盘宽高
        self.win_num = win_num 
        #  过关分数
        self.reset()
        #  重置清屏

    def reset(self):
        self.state = 'init'
        #  初始化状态
        self.win = False
        #  胜利状态
        self.over = False
        #  失败状态
        #  self.score = GameManager.score
        #  当前分数
        self.grid = Grid(self.size)
        #  创建棋盘
        self.grid.reset()
        #  棋盘清屏

    @property
    def screen(self):
        '''
        显示棋盘
        '''
        return Screen(screen=self.stdscr, score=GameManager.score, grid=self.grid, win=self.win, over=self.over)

    def move(self, direction):
        #  判断棋盘操作是否存在且可行
        if self.can_move(direction):
            getattr(self.grid, 'move_' + direction)()
            #  getattr会调用grid类中的move_left、move_right
            #  move_up、move_down
            self.grid.add_random_item()
            return True
        else:
            return False

    @property
    def is_win(self):
        '''
        判断是否胜利
        '''
        self.win = max(chain(*self.grid.cells)) >= self.win_num
        return self.win

    @property
    def is_over(self):
        '''
        判断是否失败
        '''
        self.over = not any(self.can_move(move) for move in self.action.actions)
        return self.over

    def can_move(self, direction):
        #  getattr会调用grid类中的can_move__left、can_move_right
        #  can_move_up、can_move_down
        return getattr(self.grid, 'can_move_' + direction)()

    def state_init(self):
        '''
        初始化状态
        '''
        self.reset()
        return 'game'

    def state_game(self):
        '''
        游戏状态
        '''
        self.screen.draw()
        #  显示得分和棋盘
        action = self.action.get()
        #  获取当前用户行为

        if action == Action.RESTART:
            return 'init'
        if action == Action.EXIT:
            return 'exit'
        if self.move(action):
            if self.is_win:
                return 'win'
            if self.is_over:
                return 'over'
        return 'game'

    def _restart_or_exit(self):
        '''
        重置游戏或退出游戏
        '''
        self.screen.draw()
        return 'init' if self.action.get() == Action.RESTART else 'exit'

    def state_win(self):
        '''
        胜利状态
        '''
        return self._restart_or_exit()

    def state_over(self):
        '''
        失败状态
        '''
        return self._restart_or_exit()

    def __call__(self, stdscr):
        curses.use_default_colors()
        self.stdscr = stdscr
        self.action = Action(stdscr)
        while self.state != 'exit':
            self.state = getattr(self, 'state_' + self.state)()
            #  getattr会依次调用当前类中的state_init、state_game

if __name__ == '__main__':
    recursionlimit = sys.getrecursionlimit()
    #  因为此游戏中的递归调用可能会超过最大递归深度，
    #  这里判断python中的最大递归深度是否小于2000，
    #  没有则赋值2000
    if recursionlimit < 2000:
        sys.setrecursionlimit(2000)
    curses.wrapper(GameManager())
```

> 创建 2048.py，内容如上。

#  执行 

```
python3 2048.py
```

![Screen Shot 2020-07-21 at 5.13.42 PM.png](https://upload-images.jianshu.io/upload_images/15325592-1c2528d1841979eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
