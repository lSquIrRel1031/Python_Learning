fact = "The moon has no atmosphere."
print(fact)


# fact + "No sound can be heard on the moon."
# print(fact)
# 字符串不可变，此方法无效

# 正确方式：
# fact = "The Moon has no atmosphere."
# two_facts = fact + "No sound can be heard on the Moon."
# print(two_facts)

moon_radius = "The Moon has a radius of 1,080 miles."
# 用引号包裹字符串

'The "near side" is the part of the Moon that faces the Earth.'
"We only see about 60% of the Moon's surface."
# 字符串中有一种引号时，应用另一种引号包裹

"""We only see about 60% of the Moon's surface, this is known as the "near side"."""
# 字符串中有两种引号时，应用三引号包裹

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline2 = """Facts about the Moon: 
 There is no atmosphere. 
 There is no sound.
"""
print(multiline2)

# 有几种不同的方法可将多行文本定义为单个变量。 最常见的方法是：

# 使用换行符 (\n)
# 使用三引号 (""")
