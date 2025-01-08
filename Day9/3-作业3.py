# 作者: 段鼎肯
# 2025年01月06日23时02分20秒
# xxx@qq.com


# 练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例
# 练习上课的search，findall,sub等案例
# 练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例
# 练习上课的search，findall,sub等案例

import re


def use_greedy():
    """
    演示贪婪和非贪婪匹配。
    贪婪匹配: 尽可能多地匹配字符。
    非贪婪匹配: 尽可能少地匹配字符。
    """
    s = "This is a number 234-235-22-423"
    # 使用非贪婪匹配，只获取第一个完整数字组合
    ret = re.match(r".+?(\d+-\d+-\d+-\d+)", s)
    print(ret.group(1))  # 输出: 234-235-22-423

    # 贪婪匹配示例
    print(re.match(r"aa(\d+)", "aa2343ddd").group(1))  # 输出: 2343

    # 非贪婪匹配示例
    print(re.match(r"aa(\d+?)", "aa2343ddd").group(1))  # 输出: 2

    # 匹配具体结构: 贪婪匹配
    print(re.match(r"aa(\d+)ddd", "aa2343ddd").group(1))  # 输出: 2343

    # 匹配具体结构: 非贪婪匹配
    print(re.match(r"aa(\d+?)ddd", "aa2343ddd").group(1))  # 输出: 2


def use_r():
    """
    使用原生字符串(r)的作用。
    在正则表达式中避免反斜杠(\)转义问题。
    """
    mm = "c:\\a\\b\\c"  # 普通字符串需要双反斜杠表示路径
    print(mm)  # 输出: c:\a\b\c

    # 使用r前缀，将字符串视为原生字符串，避免转义问题
    print(re.match(r"c:\\", mm).group())  # 输出: c:\


def use_option():
    """
    使用正则表达式的flags选项。
    flags选项可以影响正则表达式的匹配行为。
    """
    # re.A (ASCII-only匹配): 只匹配ASCII字符，不匹配Unicode字符
    print(re.match(r'\w*', 'abc函', flags=re.A).group())  # 输出: abc

    # re.I (忽略大小写): 匹配时忽略大小写差异
    print(re.match(r'a*', 'aA', flags=re.I).group())  # 输出: aA

    # re.S (使点号.匹配包括换行符在内的所有字符)
    print(re.match(r'.*', 'abc\ndef', flags=re.S).group())  # 输出: abc\ndef


if __name__ == '__main__':
    # 调用贪婪和非贪婪匹配示例
    # use_greedy()

    # 调用原生字符串用法示例
    # use_r()

    # 调用flags选项示例
    use_option()

