#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# 引入亂數模組
import random
from easygui import *

# 設定猜數字最小與最大數
guess_small = 1
guess_big = 100

# 取亂數值 number 為要猜的數字
number = random.randint(guess_small,guess_big)

msgbox("請猜{0}到{1}之間的整數：".format(guess_small,guess_big),'猜猜數字遊戲')
guess = integerbox("請輸入數字：", '',  None, guess_small, guess_big)

while guess != number:
    if guess_small < guess < number:
        guess_small = guess
    elif number < guess < guess_big:
        guess_big = guess
    guess =integerbox("{0} 與 {1} 之間。".format(guess_small,guess_big), '', None, guess_small, guess_big)
else:
    msgbox("你猜對了！答案是{}".format(number),'BINGO')
