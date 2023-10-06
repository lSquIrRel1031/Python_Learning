planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]

# 索引

print("The first planet is", planets[0])
# 第一行
print("The second planet is", planets[1])
# 第二行
print("The third planet is", planets[2])
# 第三行

# 修改

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# 确定长度
number_of_planets = len(planets)
print(f"There are {number_of_planets} planets in the solar system.")

# 添加
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# 删除
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# 负索引
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# 查找
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
