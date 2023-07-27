# Python Learning

## 字面量

[^字面量]:在代码中,被写下来的固定下来的值

- 数字(Number)

	- 整数(int)

		如:`10`,`-10`

	- 浮点数(float)
	
		如`13.14`,`-13.14`
	
	  -   复数(complex)
	
		如`4+3j`,以j结尾表示复数
	
	  -   布尔(bool)
	
		表示现实生活中的逻辑,即真(True)和假(False),
	
		True本质上是一个数字记作1,False记作0
	
- 字符串(String)

	[^字符串]:描述文本的一种数据类型

	字符串由任意的字符组成,要用引号包起来 

- 列表(List)

	[^列表]:有序的可变数序

	Python中使用最频繁的数据类型,可有序记录一堆数据

- 元组(Tuple)

- [^元组]:有序的不可变序列

	可无序记录一堆不可变的Python数据集合

- 集合(Set)

	[^集合]:无序不重复集合

	可无序记录一堆不可变的Python数据集合

- 字典(Dictionary)

	[^字典]:无序Key-Value集合

	可无序记录一堆Key-Value型的Python数据集合



## 注释

[^注释]:对代码进行解释说明的文字

### 单行注释

以“#”为开头,#右侧的内容为注释内容

`````python
# information
`````

### 多行注释

用三个双引号包裹起来

```python
"""
	information
	information
"""
```



## 变量

[^变量]:在程序运行时,能储存计算结果或能表示值的抽象概念



### 定义格式

```python
name = value
```



## 数据类型

### 分类

#### string(字符串类型)

[^string]:用引号引起来的数据



#### int[整型(有符号)]

[^int]:数据类型,存放整数



#### float[浮点型(有符号)]

[^float]:数据类型,存放小数

### type()语句

```python
type(vlaue)
```

## 数据类型转换

- 将x转换为整数类型

```python
int(x)
```

- 将x转换为浮点数类型

```python
float(x)
```

- 将x转换为字符串类型

```python
str(x)
```



> 所有的数据类型都可以转成字符串,但只有是数字的字符串可以转成数字类型
>
> 浮点数转整数会丢失小数部分



## 标识符

[^标识符]:用户在编程时所使用的一系列名字，用于给变量、类、方法命名

### 命名规则

- 内容限定
- 大小写敏感
- 不可使用关键字



#### 内容限定

标识符命名中只允许出现：

- 英文
- 中文
- 数字
- 下划线（__）

这四类元素。

其余任何内容都不被允许



注意：

1. 不推荐使用中文
2. 数字不可以用在开头



### 命名规范

- 见名知意（明了、简洁）
- 下划线命名法
- 英文字母全小写



## 运算符

### 算术运算符

| 运算符 |  描述  |
| :----: | :----: |
|   +    |   加   |
|   -    |   减   |
|   *    |   乘   |
|   /    |   除   |
|   //   | 取整除 |
|   %    |  取余  |
|   **   |  指数  |



### 赋值运算符

| 运算符 | 示例               |
| ------ | ------------------ |
| =      | `x = 2`,x现在包含2 |
| +=     | `x += 2`,x增加2    |
| -=     | `x -= 2`,x减去2    |
| /=     | `x /= 2`,x除以2    |
| *=     | `x *= 2`,x乘以2    |





## 日期

### 用途

- **备份文件：**。 使用日期作为备份文件名称的一部分，可以很好地指示何时进行的备份以及何时需要再次进行备份。
- **条件：**。 当存在特定日期时，可能需要执行特定逻辑。
- **指标：**。 日期用于检查代码的性能，例如，测量执行函数所花的时间。



### 用法

需要先导入`date`模块

```python
from datetime import date
```

想调用今天的日期可以调用`date()`函数,还可以打印

```python
date.today()

print(date.today())
```



## 命令行输入

使用 `python3` 启动程序时，请为程序指定要启动的文件的名称。 还可为它提供一组参数：程序在运行时有权访问的数据。 如下所示：

Bash

```bash
python3 backup.py 2023-01-01
```

在以上代码中，字符串“2023-01-01”可以用作程序 backup.py 从该日期开始备份的指令。 使用命令行参数的好处是具有灵活性。 程序的行为可能有所不同，具体取决于其外部输入。

### 命令行参数

在编码时是如何捕获这些命令的？ 通过使用 `sys` 模块，可以检索命令行参数，并在程序中使用它们。 请看以下代码：

```python
import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg
```

`sys.argv` 是一个数组，或者说是一个包含许多项的数据结构。 第一个位置在数组中表示为 `0`，包含程序名称。 第二个位置 `1` 包含第一个参数。 假设程序 backup.py 包含示例代码，并且你按如下所示运行该程序：

控制台

```console
python3 backup.py 2023-01-01
```

然后程序生成以下结果：

输出

```output
['backup.py', '2023-01-01'] 
backup.py
2023-01-01
```



## 用户输入

向程序传递数据的另一种方式是让用户输入数据。 你可以编写代码，让程序告知用户输入信息。 你将输入的数据保存在程序中，然后处理这些数据。

要捕获来自用户的信息，请使用 `input()` 函数。 下面是一个示例：

Python

```python
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)
```

假设程序 input.py 包含示例代码，并且你按如下所示运行该程序：

控制台

```console
python3 input.py
```

运行程序会邀请你输入你的姓名，例如：

输出

```output
Welcome to the greeter program
Enter your name: 
```

输入值并按 Enter 后，会返回问候语：

输出

```output
Welcome to the greeter program
Enter your name: Picard
Greetings Picard
```

### 使用数字

函数 `input()` 将结果存储为字符串，因此，以下代码可能不会执行你想要它执行的操作：

```python
print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)
```

运行此程序会邀请你输入第一个数字，比如说 `3`：

```output
calculator program
first number: 3
```

按 Enter 后，可以输入第二个数字，比如说 `4`：

```output
calculator program
first number: 3
second number: 4
```

按 Enter 可得到以下结果：

```output
calculator program
first number: 3
second number: 4
34
```

你可能想要此程序用 `7` 而不是 `34` 来回答你。 是哪里出错了呢？

原因是 `first_number` 和 `second_number` 是字符串。 为了使计算正常运行，需要使用 `int()` 函数将这些字符串更改为数字。 通过修改程序的最后一行来使用 `int()`，可以解决此问题：

```python
print(int(first_number) + int(second_number))
```

使用相同的值重新运行该程序，现在返回的响应是 `7`：

```output
calculator program
first number: 3
second number: 4
7
```
