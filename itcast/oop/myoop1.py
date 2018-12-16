#!/usr/bin/env python3
# 1. 在对象的方法内部，是直接可以访对象属性的
# 2. 同一个类创建的不同对象之间，属性互不干扰


class Person:
    """
    描述人的类
    """

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫 %s , 体重 %.2f" % (self.name, self.weight)

    def run(self):
        """跑步"""

        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        """吃东西"""

        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1


xiaoming = Person('xiaoming', 75.0)
print(xiaoming)
xiaoming.run()
print(xiaoming.weight)
