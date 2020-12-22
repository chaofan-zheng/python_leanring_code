from bll import GameControl


class GameView:
    def __init__(self):
        self.controller = GameControl()

    def show_menu(self):
        print("按下w上滑")
        print("按下s下滑")
        print("按下a左滑")
        print("按下d右滑")

    def select_menu(self, map):
        result = input("请输入你的选项")
        if result == "w":
            self.controller.upslide(map)
        if result == "a":
            self.controller.leftslide(map)
        if result == "s":
            self.controller.downslide(map)
        if result == "d":
            self.controller.rightslide(map)

