# COPYRIGHT: Roky Edward Iven Henderson
from config import your_game
from config import your_game_name
import random
import os
import time

options = [
    " 1. Commands\n",
    "2. Timed Commands\n",
    "3. Display\n",
    "4. Help/Info\n",
    "5. Keep Going!\n",
    f"6. {your_game_name} \n",
]
help = [
    " Commands-Commands gives you a command to Copy!\n",
    "Timed Commands-Does the same as Commands except it shows you for a breif time\n",
    "Displays all commands that can be ruturned\n",
]
words_1 = [
    "rm -rf .config/nvim/lua",
    "brew reinstall python3",
    "npm install -g typescript",
    "vim test.txt",
    "vim $(fzf)",
    "brew uninstall emacs",
    "bash file.sh",
    "git clone http://github.com/a/repo.git",
    "git commit -m 'A really cool commit message here",
    "apt update",
    "cowsay '(:'",
    "sl",
]
W_options = ["remove nvim with brew"]
W_goals = ["brew uninstall neovim"]


def lose(x):
    print(f"You Lost at: {x}")


def win(x):
    print(f"You Won at: {x}")


def handle_game(x):
    if x == 1:
        goal = random.choice(words_1)
        print(goal)
        in_1 = input(": ")
        if in_1 == goal:
            return True
        else:
            return False
    if x == 2:
        goal = random.choice(words_1)
        print(goal)
        time.sleep(1)
        os.system("clear")
        in_2 = input(": ")
        if in_2 == goal:
            return True
        else:
            return False
    if x == 3:
        print(*words_1)
        return True
    if x == 4:
        print(*help)
        return True
    if x == 5:
        y = 0
        while True:
            goal = random.choice(words_1)
            print(goal)
            time.sleep(1)
            os.system("clear")
            if y:
                win("Keep Going!")
            else:
                lose("Keep Going!")
            in_5 = input(": ")
            if in_5 == goal:
                y = True
            else:
                y = False
    if x == 6:
        your_game()


def handle_optionin(x):
    if x == "1":
        game_1 = handle_game(1)
        if game_1:
            win("Commands")
        else:
            lose("Commands")
    if x == "2":
        game_2 = handle_game(2)
        if game_2:
            win("Write Commands")
        else:
            lose("Write Commands")
    if x == "3":
        game_3 = handle_game(3)
        if game_3:
            win("Display")
        else:
            lose("Display")
    if x == "4":
        game_4 = handle_game(4)
        if game_4:
            win("Help")
        else:
            lose("Help")
    if x == "5":
        game_5 = handle_game(5)
        if game_5:
            win("Keep Going!")
        else:
            lose("Keep Going!")
    if x == "6":
        game_6 = handle_game(6)
        if game_6:
            win(your_game_name)
        else:
            lose(your_game_name)


def handle_start():
    print(*options)
    optionin = input(": ")

    handle_optionin(optionin)


handle_start()
