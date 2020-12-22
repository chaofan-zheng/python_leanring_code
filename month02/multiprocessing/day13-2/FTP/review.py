"""
    复习 MVC
        class XXModel:
            # 封装数据
            def __init__(self,参数1,参数2,参数3):
                self.数据1 = 参数1
                self.数据2 = 参数2
                self.数据3 = 参数3

        class XXView:
            def __init__(self):
                self.controller = XXController()

            # 界面逻辑:输入、输出、页面跳转
            def 输入信息方法(self):
                数据 = XXModel(输入的各种信息)
                self.controller.存储信息方法(数据)

        class XXController:
            # 业务逻辑:对数据的核心操作
            def 存储信息方法():
                ...

        view = XXView()
        view.输入信息方法()

    导入模块
    方式一："我过去"    --- 本质：通过变量关联模块
        import 模块名
        模块名.成员

    方式二："你过来"    --- 本质：将模块的成员导入到当前作用域中
        from 模块名 import 成员
        成员
        小心：命名冲突
"""
print("你猜我的模块名：",__name__)

def func01():
    print("func01")
