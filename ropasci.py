import os
import random
import time
import cson
from colorama import init

os.sys.path.insert(0, "./lib/")

from color import *

# init()

# Want colorama
# Work if dev == True
#REWRITE
def log(text, leftSpace=False, rightSpace=True):
    if dev:
        leftSpace = " " if leftSpace else ""
        rightSpace = " " if rightSpace else ""
        
        print(leftSpace + yellow("[DEV]") + rightSpace + text)

if len(os.sys.argv) > 1:
    dev = os.sys.argv[1] == "dev"
else:
    dev = False

lang = input('Your language? (de, en, ru, ua, em) ')

while lang != "de" and lang != "en" and lang != "ru" and lang != "ua" and lang != "em":
    lang = input('Your language? (de, en, ru, ua, em) ')

with open("./locale/" + lang + ".cson", encoding="utf-8") as locale_file:
    locale = cson.load(locale_file)
    log(locale["name"])

logo(locale["game"])

while True:

    for key in range(3):
        print(str(key + 1) + ". " + locale["objects"][key])

    player_input = input(locale["message"]["choice"])
    while player_input != "1" and player_input != "2" and player_input != "3":
        player_input = input(locale["message"]["choice"])

    player = int(player_input) - 1
    print()

    print(locale["bot"]["choice"])
    print()

    time.sleep(1)
    bot = random.randint(0, 2)

    with open("./config.cson", "r", encoding="utf-8") as config_file:
        modes = cson.load(config_file)
    massive = modes["standart"]

    i = 0
    for key in massive[player]:
        if bot == i:
            if i == 0:
                print(yellow(" " + locale["results"][key] + "!") + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
            if i == 1:
                print(green(" " + locale["results"][key] + "!") + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
            if i == 2:
                print(red(" " + locale["results"][key] + "!") + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
        i += 1

    print()

    play = input(locale["message"]["play"]["request"])

    if play != locale["message"]["play"]["arguments"][0]:
        quit()
