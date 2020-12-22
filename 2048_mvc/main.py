#! /opt/anaconda3/bin/python3

from model import GameModel
from ull import GameView
from bll import GameControl

view = GameView()
control = GameControl()


def game_begin():
    game_list = control.two_generator(GameModel.game_list)
    print("2048游戏开始了！")
    for line in game_list:
        print(line, end="\n")
    while True:
        view.show_menu()
        game_continue = input("是否继续（按q退出）")
        if game_continue == "q":
            break
        view.select_menu(game_list)
        game_list = control.two_generator(game_list)
        for line in game_list:
            print(line, end="\n")


game_begin()



