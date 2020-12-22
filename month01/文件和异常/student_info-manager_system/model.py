"""
    student info system 的model模块
    用来存储学生信息
"""

class StudentModel:
    """
        数据模型：封装数据
    """

    def __init__(self, name="", age=0, score=0.0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 学生编号(全球唯一标示符)
        self.sid = sid

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise Exception("成绩有误")

    def __str__(self):
        return f"学生的名字是{self.name},年龄是{self.age},编号是{self.sid},成绩是{self.score}"

    def __eq__(self, other):
        if self.sid == other.sid:
            return True

