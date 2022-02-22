from contextlib import nullcontext
from select import select
from tempfile import gettempdir
from tkinter import Image
from traceback import print_tb
from numpy import true_divide
from pyautogui import *
import pyautogui
import time
import keyboard
import random
from PIL import ImageGrab
from datetime import datetime

gamesPlayed = 0
gamesWon = 0
gamesLost = 0
xpPerGame = 2000
xpToLvlUp = 18000
startTime = time.time()

def main():

    print("Started at " + GetTime())

    while(True):
        if(CheckIfInLobby()):
            GetInGame()
            while(CheckIfInGame == False):
                CheckIfUserExits()
                sleep(1)
            while(CheckIfGameEnded() == False):
                CheckIfUserExits()
                CheckIfCrashed()
                CheckIfAfk()
                if(CheckIfCanChooseLoadout()):
                    ChooseLoadout()
                if(CheckIfCanSpawn()):
                    Spawn()
                if(CheckIfDied()):
                    Death()
                Move()
                sleep(0.5)

    '''while(keyboard.is_pressed("x") != True):
        print(pyautogui.position())'''

    Quit()

def Quit():
    print("Time running: " + str(startTime - time.time()))
    print("Games played: " + str(gamesPlayed))
    print("Games won: " + str(gamesWon))
    print("Games lost: "+ str(gamesLost))
    print("XP earned: " + str(gamesPlayed * xpPerGame))
    print("Levels earned: " + str((gamesPlayed * xpPerGame) / xpToLvlUp))
    exit()

def ChooseLoadout():
    pyautogui.moveTo(381, 450, duration=0.5)
    pyautogui.click()
    sleep(0.5)

def Move():
    pyautogui.keyDown("w")
    pyautogui.click()
    sleep(0.5)
    pyautogui.keyUp("w")
    pyautogui.keyDown("d")
    pyautogui.click()
    sleep(0.5)
    pyautogui.keyUp("d")
    pyautogui.keyDown("w")
    sleep(0.5)
    pyautogui.keyUp("w")
    pyautogui.keyDown("space")
    sleep(0.5)
    pyautogui.keyUp("space")
    pyautogui.keyDown("w")
    pyautogui.click()
    sleep(0.3)
    pyautogui.keyDown("space")
    pyautogui.click()
    sleep(0.5)
    pyautogui.keyUp("space")
    pyautogui.keyUp("w")

def GetTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def GetInGame():

    #Click legends tab
    pyautogui.moveTo(1115, 45, duration=0.5)
    pyautogui.click()

    #Select Valkyrie
    pyautogui.moveTo(283, 807, duration=0.5)
    pyautogui.click()

    #Exit Valkyrie
    pyautogui.hotkey("esc")

    #Click play tab
    pyautogui.moveTo(706, 41, duration=0.5)
    pyautogui.click()

    #Click mode select
    pyautogui.moveTo(225, 803, duration=0.5)
    pyautogui.click()

    #Select control
    pyautogui.moveTo(1708, 570, duration=0.5)
    pyautogui.click()

    #Click ready
    pyautogui.moveTo(231, 968, duration=0.5)
    pyautogui.click()
    sleep(0.5)

    print("Started matchmaking at " + GetTime())

def Spawn():

    #Try spawning on A1
    pyautogui.moveTo(1350, 522, duration=1)
    pyautogui.click()
    sleep(0.5)

    #Try spawning on B1
    pyautogui.moveTo(634, 402, duration=1)
    pyautogui.click()
    sleep(0.5)

    #Try spawning on A2
    pyautogui.moveTo(1350, 520, duration=1)
    pyautogui.click()
    sleep(0.5)

    #Try spawning on B2
    pyautogui.moveTo(608, 444, duration=1)
    pyautogui.click()
    sleep(0.5)

    print("Spawned at " + GetTime())

def Death():
    sleep(5)
    pyautogui.hotkey("tab")
    sleep(5)

    print("Died at " + GetTime())

def MatchEnded(result):
    sleep(30)
    pyautogui.moveTo(968, 993, duration=1)
    pyautogui.hotkey("space")
    pyautogui.click()
    sleep(0.5)
    pyautogui.hotkey("space")
    pyautogui.click()
    sleep(2)
    pyautogui.hotkey("space")
    pyautogui.click()
    sleep(0.5)
    pyautogui.hotkey("space")
    pyautogui.click()
    sleep(0.5)

    global gamesPlayed
    gamesPlayed += 1

    if result == "Win":
        global gamesWon
        gamesWon += 1
    elif result == "Loss":
        global gamesLost
        gamesLost += 1

    print("Match ended at " + GetTime() + " Result: " + result)

def CheckIfCrashed():
    if pyautogui.locateOnScreen("CrashCheck.png", confidence=0.8) != None:
        print("Crashed at " + GetTime)
        Quit()

def CheckIfInLobby():
    if pyautogui.locateOnScreen("InLobbyCheck.png", confidence=0.8) != None:
        return True
    else:
        return False

def CheckIfInGame():
    if pyautogui.locateOnScreen("InGameCheck.png", confidence=0.95) != None:
        return True
    else:
        return False

def CheckIfGameEnded():
    if pyautogui.locateOnScreen("HasWonCheck.png", confidence=0.8) != None:
        MatchEnded("Win")
        return True
    elif pyautogui.locateOnScreen("HasLostCheck.png", confidence=0.8) != None:
        MatchEnded("Loss")
        return True
    else:
        return False

def CheckIfCanSpawn():
    if pyautogui.locateOnScreen("CanSpawnCheck.png", confidence=0.85) != None:
        return True
    else:
        return False

def CheckIfDied():
    if pyautogui.locateOnScreen("DiedCheck.png", confidence=0.9) != None:
        return True
    else:
        return False

def CheckIfUserExits():
    if keyboard.is_pressed("x"):
        print("User terminated the program at " + GetTime())
        Quit()

def CheckIfCanChooseLoadout():
    if pyautogui.locateOnScreen("LoadoutCheck1.png", confidence=0.95) != None:
        return True
    elif pyautogui.locateOnScreen("LoadoutCheck2.png", confidence=0.95) != None:
        return True
    else:
        return False

def CheckIfAfk():
    if pyautogui.locateOnScreen("AfkCheck.png", confidence=1) != None:
        print("Got error for AFK")
        Quit()

main()