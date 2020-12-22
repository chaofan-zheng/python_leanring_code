"""
    可迭代对象工具集
"""


class IterableHelper:

    @staticmethod
    def find_all(iterable, func):
        """
            在可迭代对象中，根据条件查找多个元素
        :param iterable: 可迭代对象
        :param func: 函数类型的条件
        :return: 生成器
        """
        for item in iterable:
            if func(item):
                yield item

    @staticmethod
    def find_single(iterable, func):
        """
            在可迭代对象中，根据功能查找单个元素
        :param iterable: 可迭代对象
        :param func: 函数类型的条件
        :return: 单个元素
        """
        for item in iterable:
            if func(item, ):
                return item

    @staticmethod
    def select(iterable, func):
        """
            在可迭代对象中，根据功能返回特定元素
        :param iterable: 可迭代对象
        :param func: 返回特定属性的函数
        :return: 生成器
        """
        for item in iterable:
            yield func(item)

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
            在可迭代对象中，找到根据某一属性排序后的可迭代对象 （升序）
        :param iterable: 可迭代对象
        :param func: 根据对象返回某一对象的属性
        :return: 整理好顺序的可迭代对象
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if func(iterable[r]) > func(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
        result = iterable
        return result

    @staticmethod
    def get_multiple_max(iterable, func):
        """
            在可迭代对象中（具有索引），范围具有特定最大值的多个对象
        :param iterable: 可迭代对象（具有索引）
        :param func: 根据功能返回需要找到最大值的属性
        :return: 具有此最大值的对象的生成器
        """
        max_num = func(iterable[0])
        for item in iterable:
            if func(item) > max_num:
                max_num = func(item)
        for item in iterable:
            if func(item) == max_num:
                yield item

    @staticmethod
    def get_multiple_min(iterable, func):
        """
            在可迭代对象中（具有索引），范围具有特定最大值的多个对象
        :param iterable: 可迭代对象（具有索引）
        :param func: 根据功能返回需要找到最大值的属性
        :return: 具有此最大值的对象的生成器
        """
        min_num = func(iterable[0])
        for item in iterable:
            if func(item) < min_num:
                min_num = func(item)
        for item in iterable:
            if func(item) == min_num:
                yield item

    @staticmethod
    def get_all_info_count_of_one_item(iterable, func):
        """
            得到拥有某一属性的对象的个数，返回字典
        :param iterable:
        :param func: 返回特定属性
        :return: 字典
        """
        result_dict = {}
        for item in iterable:
            if func(item) in result_dict:
                result_dict[func(item)] += 1
            else:
                result_dict[func(item)] = 1
        return result_dict
