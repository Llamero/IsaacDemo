#Search:
#Game: https://www.addictinggames.com/clicker/timber-guy
#1 - python get screen shot
#2 - python get mouse coordinates
#3 - pyautogui get pixel color
#4 - python detect mouse click event

import pyautogui
from pynput.mouse import Listener
import time
import win32api
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def waitForClick():
    while(True):
        a = win32api.GetKeyState(0x01)
        while(a<0):
            a = win32api.GetKeyState(0x01)
            if(a>=0):
                return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    w=135 #135 85 50
    h=110 #110 70 42
    mouse_pos = [0]*2
    bkgnd_screenshot = [0] * 2
    bkgnd_colors = [0] * 2
    waitForClick()
   # pyautogui.move(135,0)
    #sys.exit()
    mouse_pos[0] = pyautogui.position() #Get mouse position - http://www.learningaboutelectronics.com/Articles/How-to-get-the-current-position-of-mouse-in-Python-using-pyautogui.php#:~:text=To%20determine%20the%20mouse's%20current,where%20the%20mouse%20cursor%20is.
    mouse_pos[1] = [mouse_pos[0][0]+w, mouse_pos[0][1]]
    #full_screenshot = pyautogui.screenshot() #Get image of whole screen - https://datatofish.com/screenshot-python/
    #px = full_screenshot.getpixel(mouse_pos) #Get pixel color - https://stackoverflow.com/questions/64722136/how-to-use-pyautogui-to-detect-rgb-values
    #bkgnd_px = pyautogui.pixel(mouse_pos[0], mouse_pos[1]) #Get pixel value - https://stackoverflow.com/questions/3800458/quickly-getting-the-color-of-some-pixels-on-the-screen-in-python-on-windows-7

    bkgnd_screenshot[0] = pyautogui.screenshot(region=(mouse_pos[0][0], mouse_pos[0][1] - h, 1, h))
    bkgnd_colors[0] = bkgnd_screenshot[0].getcolors()
    i=0
    r_set = False
    for a in range(500):
        #px = pyautogui.pixel(mouse_pos[0], mouse_pos[1])
        screenshot = pyautogui.screenshot(region=(mouse_pos[i][0], mouse_pos[i][1] - h, 1, h))
        colors = screenshot.getcolors()
        if(colors != bkgnd_colors[i]):
            i = abs(i-1)
            if(not r_set):
                bkgnd_screenshot[i] = pyautogui.screenshot(region=(mouse_pos[i][0], mouse_pos[i][1] - h, 1, h))
                bkgnd_colors[i] = bkgnd_screenshot[i].getcolors()
                r_set = True
            print("switch")
        if(i==0):
            pyautogui.press('left')
            print("<-")
        else:
            pyautogui.press('right')
            print("->")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
