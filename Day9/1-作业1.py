import copy


def use_list_copy():
    """
    使用列表自身的 copy 方法创建副本。
    特点：
    - 属于浅拷贝，只复制第一层内容。
    - 副本与原列表在内存中占据不同位置，但嵌套对象指向相同引用。
    :return:
    """
    a = [1, 2, 3]
    b = a.copy()  # 使用列表自身的 copy 方法
    b[0] = 10  # 修改副本中的值不会影响原列表
    print(a)  # 输出 [1, 2, 3]
    print(b)  # 输出 [10, 2, 3]
    print(id(a))
    print(id(b))


def use_copy():
    """
    使用 copy 模块中的 copy 方法。
    特点：
    - 浅拷贝，只复制对象的第一层。
    - 原始对象和副本是不同的对象。
    :return:
    """
    c = [1, 2, 3]
    d = copy.copy(c)  # 使用 copy 模块创建浅拷贝
    d[0] = 10  # 修改副本中的值不会影响原列表
    print(id(c))  # 打印原列表的内存地址
    print(id(d))  # 打印副本的内存地址，二者不同
    print(c)  # 输出 [1, 2, 3]
    print(d)  # 输出 [10, 2, 3]


def use_copy2():
    """
    浅拷贝示例：仅复制第一层内容。
    特点：
    - 如果嵌套对象发生变化，浅拷贝的副本也会受影响。
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]  # 嵌套列表
    # print(c)
    d = copy.copy(c)  # 创建浅拷贝
    print(id(c))  # 原列表的内存地址
    print(id(d))  # 副本的内存地址
    a[0] = 10  # 修改嵌套对象
    print(f'c--{c}')  # 输出 [[10, 2], [3, 4]]
    print(f'd--{d}')  # 输出 [[10, 2], [3, 4]] - 副本也变化
    print('-' * 50)
    print(id(c[0]), id(c[1]))  # 原列表中嵌套对象的内存地址
    print(id(d[0]), id(d[1]))  # 副本中嵌套对象的内存地址（相同）


def use_deepcopy():
    """
    深拷贝示例：递归复制所有层级。
    特点：
    - 深拷贝会创建嵌套对象的新副本，因此嵌套对象的变化不会影响副本。
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]  # 嵌套列表
    d = copy.deepcopy(c)  # 创建深拷贝
    print(id(c))  # 原列表的内存地址
    print(id(d))  # 副本的内存地址
    a[0] = 10  # 修改嵌套对象
    print(f'c--{c}')  # 输出 [[10, 2], [3, 4]]
    print(f'd--{d}')  # 输出 [[1, 2], [3, 4]] - 副本未变化
    print('-' * 50)
    print(id(c[0]), id(c[1]))  # 原列表中嵌套对象的内存地址
    print(id(d[0]), id(d[1]))  # 副本中嵌套对象的内存地址（不同）


class Hero:
    """
    自定义对象 Hero
    """

    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        self.equipment = ['鞋子', '指环']  # 初始装备


def use_copy_own_obj():
    """
    自定义对象的拷贝示例。
    特点：
    - 深拷贝适合复杂对象，确保对象属性和嵌套对象都被独立复制。
    :return:
    """
    old_hero = Hero('蚂蚁', 90)  # 创建原始对象
    new_hero = copy.deepcopy(old_hero)  # 创建对象的深拷贝
    new_hero.blood = 80  # 修改新对象的属性
    new_hero.equipment.append('药水')  # 修改新对象的装备

    # 原对象保持不变
    print(old_hero.blood)  # 输出 90
    print(old_hero.equipment)  # 输出 ['鞋子', '指环']
    print(new_hero.blood)
    print(new_hero.equipment)


if __name__ == '__main__':
    # use_list_copy()
    # use_copy()  # 测试浅拷贝
    # use_copy2()  # 测试浅拷贝对嵌套对象的影响
    # use_deepcopy()  # 测试深拷贝对嵌套对象的影响
    use_copy_own_obj()  # 测试自定义对象的深拷贝
