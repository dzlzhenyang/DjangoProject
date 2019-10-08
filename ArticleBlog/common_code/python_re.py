"""
正则是一种高级的字符串处理方式，通常用于字符的匹配
字符串匹配有两种
    内容配置  re
        通过描述要匹配内容的类型和个数来实现匹配
        匹配手机号
            11位数字
    结构匹配  lxml xpath
        通过描述要匹配内容在整体当中的结构来实现匹配
        匹配手机号
            手机号:后面跟着的东西
    匹配的方式：
        类型匹配：
            1. 原样匹配 匹配对应的原样字符，通常不单独使用，
                匹配手机号  匹配139开头的11位数字
            2. .匹配
            3. \w 匹配
            4. \W 匹配
            5. \d 匹配
            6. \D匹配
            7. []匹配
            8. | 匹配
            9. ()组匹配
            10 ()命名组匹配
        长度匹配：
            1.*匹配
            2.+匹配
            3.？匹配
            4.{}匹配
        特殊匹配：
            1.^
            2.$

"""
import re

# .匹配 匹配任意非换行字符
string = "123\nabc"
result = re.findall('.', string)  # ['1', '2', '3', 'a', 'b', 'c']
# result = re.findall('..', string) # ['12', 'ab']
print(result)

# \w匹配: 匹配所有数字，字母，下划线
result = re.findall('\w', string)  # ['1', '2', '3', 'a', 'b', 'c']
print(result)

# \W匹配：匹配所有非数字，非字母，飞下划线
result = re.findall('\W', string)  # ['\n']
print(result)

# \d匹配：匹配所有的数字
result = re.findall('\d', string)  # ['1', '2', '3']
print(result)

# \D匹配：匹配所有的非数字，包括\n
result = re.findall('\D', string)  # ['\n', 'a', 'b', 'c']
print(result)

# []匹配 匹配中括号当中任意字符
# result = re.findall('[1an]', string) # ['1', 'a']
# 匹配中括号当中的范围任意一个字符
# result = re.findall('[a-z0-9]', string)
# [] 返回非中括号当中的任意一个字符
result = re.findall(r'[^a-z0-9]', string)  # ['\n']
print(result)

# |匹配：匹配|两边的任意一边字符
# result = re.findall(r'a|1', string) #['1', 'a']
result = re.findall(r'ab|123|34', string)  # ['123', 'ab']
print(result)

# ()组匹配：将组外的匹配作为条件匹配
# 匹配a后面跟着数字或者字母或者下划线的字符串
result = re.findall('a\w', string)  # ['ab']
print(result)
# 匹配一个数字或者字母或者下划线，这个字母前面需要是a
result = re.findall('a(\w)', string)  # ['b']
print(result)

# () 命名组匹配：给组起名字然后调用
string = "123 343 666 987"
# 匹配连续的两个数字
# result = re.findall('\d\d', string)  # ['12', '34', '66', '98']
# 匹配一个数字，这个数字后面跟着两个数字
# result = re.findall('(\d)\d\d', string)  # ['1', '3', '6', '9']
# 匹配一串数字（id数字id） 这个数字后面跟着一个数字，之后在调用这个数字
result = re.findall('(?P<id>\d)\d(?P=id)', string)  # ['3', '6']
print(result)

# *匹配：匹配0到多个
result = re.findall('\d*', string)  # ['123', '', '343', '', '666', '', '987', '']
print(result)

# +匹配：匹配1到多个
result = re.findall('\d+', string)  # ['123', '343', '666', '987']
print(result)

# ?匹配：匹配0到1次
result = re.findall('\d?', string)  # ['1', '2', '3', '', '3', '4', '3', '', '6', '6', '6', '', '9', '8', '7', '']
print(result)

# {}匹配：匹配指定次数
# 匹配2个数字
# result = re.findall('\d{2}', string)  # ['12', '34', '66', '98']
# 能匹配2个就匹配2个，1个也满足匹配
result = re.findall('\d{1,2}', string)  # ['12', '3', '34', '3', '66', '6', '98', '7']
print(result)

# ^ 匹配开头
result = re.findall('^\d', string)  # ['1']
print(result)

# $匹配结尾
result = re.findall('\d$', string)  # ['7']
print(result)
