import pyautogui
import time
import math_reader

location = {}


def move(params):
    try:
        pyautogui.moveTo(int(params[0]), int(params[1]), duration=0.25)
    except:
        print("Please enter a integer")


def movePicture(params):
    global location
    if params[0] == '|picture|':
        if location:
            move([location['x'], location['y']])
        else:
            print('Location not defined')
    else:
        t = pyautogui.locateCenterOnScreen(params[0])
        if t == None:
            print('Picture Not Found')
        else:
            x, y = t
            pyautogui.moveTo(x, y, duration=0.25)


def click():
    pyautogui.click()


def getinfogui():
    pyautogui.mouseInfo()


def doubleclick():
    pyautogui.doubleClick()


def middleclick():
    pyautogui.middleClick()


def rightclick():
    pyautogui.rightClick()


def mousedown():
    pyautogui.mouseDown()


def mouseup():
    pyautogui.mouseUp()


def wait(params):
    try:

        time.sleep(int(params[0]))
    except:
        print("Please enter integer")


def drag(params):
    try:
        pyautogui.dragTo(int(params[0]), int(
            params[1]), button=params[2], duration=0.25)
    except:
        print("Please enter integers")


def scroll(params):
    try:
        pyautogui.scroll(int(params[0]))
    except:
        print("Please enter integer")


def typeF(params):
    pyautogui.write(params[0])


def hotkey(params):
    pyautogui.hotkey(*params)


def screenshot(params):
    pyautogui.screenshot(params[0])


def doMath(params):
    # print(params[0])
    return math_reader.solveParsed(math_reader.parseInput(params[0]))


def printF(params):
    print(params[0])


def startLoop(params):
    return {"commands": [], "on": True, "times": params[0]}


def waitP(params):
    global location
    while True:
        temp = pyautogui.locateOnScreen(params[0])
        if temp:
            location['x'], location['y'] = temp[0], temp[1]
            break


def moveDuration(params):
    try:
        pyautogui.moveTo(int(params[0]), int(
            params[1]), duration=(int(params[2])/100))
    except:
        print("Please enter a integer")
