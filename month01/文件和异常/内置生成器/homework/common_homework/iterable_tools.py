"""
    常用可迭代函数工具
        集成操作框架
"""


class IterableHelper:
    @staticmethod
    def get_count(iterable, func):
        """
            在可迭代对象中，找到满足一定条件的元素的数量
        :param iterable: 可迭代对象
        :param func: 需要满足的条件，返回布尔值
        :return: 重复的次数
        """
        count = 0
        for item in iterable:
            if func(item):
                count += 1
        return count

    @staticmethod
    def get_min(iterable, func):
        """
            在可迭代对象中，找到某一属性的最小值所对应的对象
        :param iterable: 可迭代对象
        :param func: 找到对象对应的属性
        :return: 拥有最小值的对象
        """
        min_value = iterable[0]
        for item in iterable:
            if func(item) < func(min_value):
                min_value = item
        return min_value

    @staticmethod
    def order_by(iterable, func):
        """
            在可迭代对象中，找到根据某一属性排序后的可迭代对象
        :param iterable: 可迭代对象
        :param func: 根据对象返回某一对象的属性
        :return: 整理好顺序的可迭代对象
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if func(iterable[r]) > func(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
        return iterable
