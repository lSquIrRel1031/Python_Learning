from datetime import date

# 打印今天日期
print(date.today())

""" wrong example:
    print("今天日期为" + date.today())
    
    没有转换日期类型为字符串
"""

print("今天日期为",date.today())
# or
print("今天日期为" + str(date.today()))