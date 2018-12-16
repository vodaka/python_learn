#!/usr/bin/env python3
# 被使用的类应该先开发


class HouseItem:

    def __init__(self, name, area):
        """
        :param name:家具名称
        :param area:家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地面积 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        """

        :param house_type: 房间类型
        :param area: 房屋面积
        """
        self.house_type = house_type
        self.area = area

        # 房屋剩余面积默认和总面积相同
        self.area_free = area
        # 默认没有家具
        self.item_list = []

    def __str__(self):
        return ("户型:%s\n总面积：%.2f[剩余面积:%.2f]\n家具:%s"
                % (self.house_type, self.area, self.area_free, self.item_list))

    def add_item(self, item):
        print("要添加：%s" % item)

        # 1. 判断家具是否大于剩余面积
        if item.area > self.area_free:
            print("%s 的面积太大，不能添加到房屋中" % item.name)
            return
        # 2. 将家具的名称追加到名称列表
        self.item_list.append(item.name)

        # 3. 计算剩余面积
        self.area_free -= item.area


# 1. 实例化家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

# 2. 实例化房间对象
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)





