# 作者: 段鼎肯
# 2025年01月06日22时59分11秒
# xxx@qq.com

# 练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例
# 练习上课的search，findall,sub等案例

import re


def simple():
    """
    基本匹配示例 - 检查字符串是否以指定模式开头
    :return:
    """
    result = re.match("wangdao", "wangdao.cn")  # 匹配字符串开头是否是 'wangdao'
    if result:
        print(result.group())  # 输出匹配结果


def single():
    """
    匹配单个字符
    :return:
    """
    # 匹配任意单个字符
    ret = re.match(".", "M")
    print(ret.group())

    # 匹配t与o之间有一个任意字符
    ret = re.match("t.o", "too")
    print(ret.group())

    ret = re.match("t.o", "two")
    print(ret.group())

    print('-' * 50)
    # 匹配大小写h开头的字符串
    ret = re.match("[hH]", "hello Python")
    print(ret.group())

    ret = re.match("[hH]", "Hello Python")
    print(ret.group())

    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())

    # 匹配0到9开头
    ret = re.match("[0-9]Hello Python", "6Hello Python")
    print(ret.group())

    ret = re.match("[0-35-9]Hello Python", "7Hello Python")  # 匹配 0-3 或 5-9
    print(ret.group())

    print('-' * 50)
    # 使用 \d 匹配数字
    ret = re.match(r"嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())

    ret = re.match(r"嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())

    ret = re.match(r"嫦娥\d号", "嫦娥3号发射成功")
    print(ret.group())


def more_alp():
    """
    匹配多个字符和复杂规则
    :return:
    """
    # 匹配一个大写字母后跟0或多个小写字母
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())

    print('-' * 50)
    # 检查变量命名规则
    names = ["name1", "_name", "2_name", "__name__"]
    for name in names:
        ret = re.match(r'[a-zA-Z_]+\w*', name)
        if ret:
            print(f'{ret.group()} 是正确的')
        else:
            print(f'{name} 不符合命名规范')


def start_end():
    """
    匹配字符串结尾
    :return:
    """
    # 匹配以@163.com结尾的邮箱
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        ret = re.match(r'\w{4,20}@163\.com$', email)
        if ret:
            print(f'{ret.group()}是正确的邮箱{email}')
        else:
            print(f'{email}邮箱地址不正确')


def split_group():
    """
    匹配分组示例
    :return:
    """
    # 匹配0-100数字范围
    ret = re.match(r"[1-9]?\d$|100", "78")
    if ret:
        print(ret.group())
    else:
        print('不是0-100之间')

    # 分组匹配电话号码格式
    ret = re.match(r"([^-]+)-(\d+)", "010-12345678")
    print(ret.group())
    print(ret.group(1))  # 输出第1组匹配
    print(ret.group(2))  # 输出第2组匹配


def other_func():
    """
    搜索、替换和拆分
    :return:
    """
    # search 找到第一个匹配项
    ret = re.search(r"\d+", "阅读次数为 9999,点赞888")
    print(ret.group())

    # findall 找出所有符合规则的项
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)

    # sub 替换匹配项
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)


def use_finditer():
    """
    使用finditer逐个匹配
    :return:
    """
    text = "abc123def456ghi789"
    pattern = r"\d+"
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group())


def use_findall():
    """
    日期格式化示例
    :return:
    """
    s = '现在是2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时|分', r':', ret_s)
    print(ret_s)


def use_sub():
    """
    清理HTML标签
    :return:
    """
    text = "<p>Python 编程</p>"
    ret = re.sub(r'<[^>]*>', '', text)  # 去除所有HTML标签
    print(ret)


def use_split():
    """
    使用 split 根据多个分隔符拆分字符串
    :return:
    """
    ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
    print(ret)


if __name__ == '__main__':
    # 调用各函数进行测试
    simple()
    single()
    more_alp()
    start_end()
    split_group()
    other_func()
    use_finditer()
    use_findall()
    use_sub()
    use_split()


