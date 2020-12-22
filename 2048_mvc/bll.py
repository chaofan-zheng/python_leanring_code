

from random import randint


class GameControl:
    def __init__(self):
        pass

    # self.game_list = GameModel.game_list

    def move_zero_to_end(self, list_target):
        for i in range(len(list_target) - 1, -1, -1):
            if list_target[i] == 0:
                del list_target[i]
                list_target.append(0)
        return list_target

    def merge_the_same(self, list_target):
        list_sorted = self.move_zero_to_end(list_target)
        for i in range(len(list_sorted) - 1, 0, -1):
            if list_sorted[i] == list_sorted[i - 1]:
                list_sorted[i] += list_sorted[i - 1]
                del list_sorted[i - 1]
                list_sorted.append(0)
        return list_sorted

    def transpose(self, list_game):
        for r in range(1, len(list_game)):
            for c in range(r, len(list_game)):
                list_game[r - 1][c], list_game[c][r - 1] = list_game[c][r - 1], list_game[r - 1][c]
        return list_game

    def leftslide(self, map):
        for i in range(len(map)):
            result_line = self.merge_the_same(map[i])
            map[i] = result_line
        return map

    def rightslide(self, map):
        for i in range(len(map)):
            result_line = self.merge_the_same(map[i][::-1])
            map[i][::-1] = result_line
        return map

    def upslide(self, map):
        return self.transpose(self.leftslide(self.transpose(map)))

    def downslide(self, map):
        return self.transpose(self.rightslide(self.transpose(map)))

    def two_generator(self, map):
        """
        随机在一个没有2的位置生成2,
        :return: none
        """
        while True:
            r = randint(0, 3)
            c = randint(0, 3)
            if map[r][c] == 0:
                map[r][c] = 2
                break
        return map


if __name__ == '__main__':
    game_control = GameControl()
    print(game_control.move_zero_to_end([0, 4, 0, 0]))
    print(game_control.move_zero_to_end([0, 4, 3, 0]))
    print(game_control.merge_the_same([0, 4, 4, 0]))
    print(game_control.leftslide([
        [2, 2, 0, 0],
        [4, 0, 0, 4],
        [2, 0, 0, 0],
        [2, 2, 2, 2]
    ]))
