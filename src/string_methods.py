# .title()
print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

# .split()
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

temperatures2 = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list2 = temperatures2.split('\n')
print(temperatures_list2)

# .join()
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))

# in
print("Moon" in "This text will describe facts and challenges with space travel")

print("Moon" in "This text will describe facts about the Moon")

# .find()
temperatures3 = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures3.find("Moon"))
# 找不到该单词，会返回‘-1’

temperatures4 = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures4.find("Mars"))

# .count()
temperatures5 = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures5.count("Mars"))
print(temperatures5.count("Moon"))

# .lower() & .upper()
print("The Moon And The Earth".lower())

print("The Moon And The Earth".upper())

# 检查内容
temperatures6 = "Mars Average Temperature: -60 C"
parts = temperatures6.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
# 与.isnumeric()方法一样.isdecimal()可检查类似于小数的字符串。

# .startswith()
print("-60".startswith('-'))

# .endswith()
if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# 转换文本
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())
# python大小写区分，用.lower()来检查
