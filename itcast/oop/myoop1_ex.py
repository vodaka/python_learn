#!/usr/bin/env python3


class Person:
    """这是一个人类"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        
        return "我叫 %s, 体重 %.2f" % (self.name, self.weight)

    def run(self):
        """我爱跑步，跑步锻炼身体"""
        print("%s 爱跑步" % self.name)
        self.weight -= 0.5

    def eat(self):
        """我是个吃货"""

        print("吃包了才有力气减肥")
        self.weight += 1

xiaoming = Person('xiaoming', 75)
xiaoming.run()
xiaoming.eat()
print(xiaoming.weight)

