#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function: Echo with different colors in the Windows command
import ctypes

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

# Define font color
FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue.
FOREGROUND_DARKGREEN = 0x02 # dark green.
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_DARKRED = 0x04 # dark red.
FOREGROUND_DARKPINK = 0x05 # dark pink.
FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_DARKGRAY = 0x08 # dark gray.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.
 
 
# Define background colors
BACKGROUND_BLUE = 0x10 # dark blue.
BACKGROUND_GREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE) 
def _set_cmd_color(cmdcolor, handle=std_out_handle):
    if cmdcolor=='red':
        color= FOREGROUND_RED
    elif cmdcolor == 'green':
        color = FOREGROUND_GREEN
    elif cmdcolor == 'white':
        color = FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE
    elif cmdcolor == 'yellow':
        color = FOREGROUND_YELLOW
    elif cmdcolor == 'pink':
        color = FOREGROUND_PINK
    elif cmdcolor == 'skyblue':
        color = FOREGROUND_SKYBLUE
    elif cmdcolor == 'blue':
        color = FOREGROUND_BLUE
        
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def color_print(text,color):
    _set_cmd_color(color)
    print(text)
    _set_cmd_color('white')
