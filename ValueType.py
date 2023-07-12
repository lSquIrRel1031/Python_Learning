# 方式1：使用print直接输出数据类型
print(type("python"))
print(type(6))
print(type(114.514))
# 方式2：用变量存储变量的数据类型
string_type = type("python")
int_type = type(6)
float_type = type(114.514)
print(string_type)
print(int_type)
print(float_type)
# 方式3：使用type()语句,查看变量中存储的变量类型信息
name = "python"
print(type(name))