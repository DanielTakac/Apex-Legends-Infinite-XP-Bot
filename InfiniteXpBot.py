from contextlib import nullcontext
from distutils.spawn import spawn
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
startTime = time.time()

def main():

    print("Started at " + GetTime())

    while(True):
        if(CheckIfInLobby()):
            GetInGame()
            while(CheckIfInGame == False):
                CheckIfUserExits()
                sleep(1)
            SelectLegend()
            while(CheckIfGameEnded() == False):
                CheckIfUserExits()
                CheckIfCrashed()
                if(CheckIfCanSpawn()):
                    Spawn()
                if(CheckIfDied()):
                    Death()
                Move()
                sleep(0.5)

    '''while(keyboard.is_pressed("x") != True):
        print(pyautogui.position())'''

def Quit():
    print("Time running: " + (startTime - time.time()))
    print("Games played: " + gamesPlayed)
    print("Games won: " + gamesWon)
    print("Games lost: "+ gamesLost)
    print("XP earned: " + (gamesPlayed * xpPerGame))

def Move():
    write("dwadsadawdawdawdadsdddaadawdsdawd", interval=0.1)

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

    print("Match ended at " + GetTime() + " Result: " + result)

def SelectLegend():
    print("Got in game at " + GetTime())

def CheckIfCrashed():
    if pyautogui.locateOnScreen("CrashCheck.png", confidence=0.8) != None:
        print("Crashed at " + GetTime)
        exit()

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
    if pyautogui.locateOnScreen("CanSpawnCheck.png", confidence=0.95) != None:
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
        exit()

main()