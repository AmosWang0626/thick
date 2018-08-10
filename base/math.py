# coding=utf-8
import math

# python里边的基本数据类型(整形/浮点型)

# pi
print(math.pi)
# sin 90
print(math.sin(math.pi / 2))
# cos 90
print(math.cos(math.pi / 2))
print(round(math.cos(math.pi / 2)))
# 向下取整
print(math.floor(9.2346))
# 向上取整
print(math.ceil(9.2346))
print(5 * 2 + 15 * 1.5)
# , 分隔符
print('hello', 'this is a statement')
# {}, 可用format替换, 和java区别就是它是 ''.format('')
print('hello {} this is {}'.format('lal', '666'))
message = 'hello, amos wang'
print(message.lower())
print(message.upper())
print(message.title())
