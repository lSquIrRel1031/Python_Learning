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

---

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

---

## 变量

[^变量]:在程序运行时,能储存计算结果或能表示值的抽象概念



### 定义格式

```python
name = value
```

---

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

---

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

---

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



### 逻辑运算符

|      |      |
| ---- | ---- |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |



## 在 Python 中使用数字

除了核心算法以外，还可以对数字使用其他运算。 可能需要执行舍入或将字符串转换为数字。

在本模块的方案中，你希望接受来自用户的输入。 输入将是一个字符串而不是数字，因此需要将其转换为数字。 此外，用户输入的答案可能是负数，而你不想显示这些值。 你可能需要将答案转换为绝对值。 幸运的是，Python 为这些运算提供了实用程序。

### 将字符串转换为数字

Python 支持两种主要类型的数字：整数（或 `int`）和浮点（或 `float`）。 二者之间的主要区别在于是否存在小数点；整数是整值，而浮点包含小数值。

将字符串转换为数字时，需要指定要创建的数字的类型。 必须确定是否需要小数点。 使用 `int` 将转换为整数，而使用 `float` 将转换为浮点数。

```python
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)
```

```Output
215
215.3
```

***重要***

如果为 `int` 或 `float` 使用了无效的值，则会发生错误。

### 绝对值

数学中的绝对值是没有符号的非负数。 在不同情况下，使用绝对值会很有用，其中包括用于确定两个行星之间距离的示例。 请考虑下面的数学运算：

```python
print(39 - 16)
print(16 - 39)
```

请注意，这两个方程之间的区别在于数字是相反的。 答案分别为 `23` 和 `-23`。 在确定两个行星之间的距离时，数字的输入顺序并不重要，因为绝对答案是相同的。

使用 `abs` 将负值转换为其绝对值。 如果使用 `abs` 执行相同的操作（并输出答案），你会注意到这两个公式的结果都显示为 `23`。

```python
print(abs(39 - 16))
print(abs(16 - 39))
```

```Output
23
23
```

### 舍入

名为 `round` 的内置 Python 函数也很有用。 如果小数值大于 `.5`，则使用它可向上舍入到最接近的整数；如果小数值小于或等于 `.5`，使用它可以向下舍入。

```python
print(round(14.5))
```

输出：14

[另一用法](###关于 f-string)：转换为小数

### 数学库

Python 中有一些库，可提供更高级的运算和计算。 最常见的一种是 `math` 库。 `math` 允许你使用 `floor` 和 `ceil` 执行舍入、提供 pi 的值以及许多其他运算。 让我们来看看如何使用这个库进行向上或向下舍入。

舍入数字让你能够去掉浮点的小数部分。 可以选择始终使用 `ceil` 向上舍入到最接近的整数，或者使用 `floor` 向下舍入。

```python
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
```



```Output
13
12
```

---

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

---

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

---

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

—

## 使用包

你编写的大多数程序将依赖于其他人编写的代码。 此代码通常以包的形式出现，包是包含在项目中的外部模块或库。 对于需要一组资源的任何项目，请务必考虑如何确保正确的资源可用于你的程序。

好的开端是学习如何管理程序。 执行此操作的一种方法是将该程序视为一个项目。 Python 使用称为虚拟环境的内容来解决这种情况。

#### 什么是虚拟环境？

你有一台开发计算机。 在该计算机上，你可能已安装了某个版本的 Python 或你打算使用某个版本的库。 将程序移到安装了不同版本的 Python 或依赖的不同版本的库的计算机时，会发生什么情况？

你不想做的一件事就是：假设你的程序可以工作，并且只能安装所依赖的任何库的最新版本。 如果这样做，则可能最终会损坏其他程序在目标计算机上的运行能力。 解决方案是找到一种让应用独立运行的方式。

Python 针对这些问题的解决方案是虚拟环境。 虚拟环境是运行程序所需的所有内容的自包含副本。 这包括 Python 解释器和程序所需的任何库。 通过使用虚拟环境，你可以确保你的程序能够访问正确的版本和资源，从而正常运行。

基本工作流如下所示：

1. 创建一个不会影响计算机其余部分的虚拟环境。
2. 单步执行虚拟环境，其中指定了所需的 Python 版本和库。
3. 开发你的程序。

#### 创建虚拟环境

可以通过调用 `venv` 模块来创建虚拟环境。 该模块需要一个名称作为参数。 你将在下一单元中设置自己的虚拟环境，因此无需运行以下任何代码。

执行以下步骤：

1. 转到要保存项目的目录。

2. 使用以下命令调用 `venv` 模块。

	控制台

	```console
	python -m venv env
	```

	此时会为你创建一些目录。 目录名称因操作系统而略有不同。

	Windows 中的目录如下所示：

	输出

	```output
	/env
	  /include
	  /lib
	  /Scripts
	```

	Linux 和 macOS 中的目录如下所示：

	输出

	```output
	/env
	  /bin
	  /include
	  /lib
	```

	环境需要 `env` 目录来跟踪详细信息，如你使用的 Python 版本和库。 不要将程序文件放在 `env` 目录中。 建议将文件放在称为 `src` 的目录或类似目录中。 项目结构可能如下所示：

	输出

	```output
	/env
	/src
	  program.py  
	```

#### 激活虚拟环境

此时，你有一个虚拟环境，但尚未开始使用它。 若要使用它，需要通过调用 `activate` 脚本来激活它。

下面是在 Windows 上激活的方式：

控制台

```console
C:\ .. \env\Scripts\activate
```

下面是在 Linux 和 macOS 上激活的方式：

Bash

```bash
source env/bin/activate
```

调用 `activate` 会更改提示。 它现在前面带有 `(env)`，类似于以下示例：

输出

```output
(env) -> path/to/project
```

此时，你处于虚拟环境中。 你所做的任何操作都会独立发生。

### 什么是包？

使用外部库的主要优点之一是，加速程序的开发。 可以在 Internet 上提取此类库。 但通过虚拟环境提取并安装这些库，可以确保只为虚拟环境安装这些库，而不是针对整个计算机进行全局安装。

### 安装包

使用 `pip` 安装包。 `pip` 命令使用 Python 包索引（简称 PyPi）来了解从何处获取包。 你可以访问 [PyPi 网站](https://pypi.org/) 来查看可用的包。

若要安装包，请从 `env` 目录运行 `pip install`，如以下示例所示：

控制台

```console
pip install python-dateutil
```

如果运行上述命令，将下载并安装 `dateutil`，这是一个用于分析 .yml 文件格式的包。 安装包后，如果你展开 env 下的 lib 目录，则可以看到它已列出，如下所示：

输出

```output
/env
  /lib
    /dateutil
```

若要查看哪些包现在已安装在虚拟环境中，可以运行 `pip freeze`。 此命令生成终端中已安装包的列表：

输出

```output
python-dateutil==2.8.2
six==1.16.0
```

 备注

前面的列表不仅仅包含 `pipdate` 的原因是 `pipdate` 本身依赖于也被提取的其他库。

若要确保这些包仅存在于虚拟环境中，请尝试通过调用 `deactivate` 退出该环境：

控制台

```console
deactivate
```

请注意终端提示如何变化。 它不再以 `(env)` 开头，并恢复为以下外观：

输出

```output
path/to/project
```

如果运行 `pip freeze`，将看到更长的依赖项列表。 此列表指示你可以看到计算机上安装的所有包，而不仅仅是虚拟环境中安装的包。

#### 安装包的更多方法

你还可以使用以下命令来安装包：

- 计算机上有一组文件，并从此源进行安装：

	```console
	cd <to where the package is on your machine>
	python3 -m pip install .
	```

- 从提供版本控制的 GitHub 存储库安装：

	```console
	git+https://github.com/your-repo.git
	```

- 从压缩的存档文件安装：

	```console
	python3 -m pip install package.tar.gz
	```

### 使用已安装的包

你现在已经安装了一个包。 如何在代码中使用它？

确保你有文件的目录。 建议调用目录 src，并添加名为 app.py 的入口点 Python 文件。 现在，添加一些代码来调用 `dateutil`：

```python
from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)
```

运行应用：

控制台

```console
python newapp.py
```

输出应类似于：

输出

```output
2023-01-30 17:04:24.799976
2023-03-07 10:04:24.799976
```

------------------------------

## 什么是“else”和“elif”

如果希望程序在测试表达式为 `False` 时也运行一段代码该怎么办？ 或者，如果想包含另一个测试表达式该怎么办？ Python 有其他关键字可用于创建更复杂的 `if` 语句，即 `else` 和 `elif`。 结合使用 `if`、`else` 和 `elif` 时，可以编写具有多个测试表达式和语句的复杂程序来运行。

### 使用 `else`

你知道，使用 `if` 语句时，程序主体将仅在测试表达式为 `True` 时运行。 若要添加在测试表达式为 `False` 时将运行的更多代码，需要添加 `else` 语句。

让我们改编上一节中的示例：

```python
a = 27
b = 93
if a >= b:
    print(a)
```

在此示例中，如果 `a` 不大于或等于 `b`，则不会执行任何操作。 假设你想要在测试表达式为 `False` 时改为打印 `b`：

```python
a = 27
b = 93
if a >= b:
    print(a)
else:
    print(b)
```

输出：`93`

如果测试表达式为 `False`，则跳过 `if` 语句主体中的代码，程序从 `else` 语句继续运行。 `if/else` 语句的语法始终为：

```python
if test_expression:
    # statement(s) to be run
else:
    # statement(s) to be run
```

### 使用 `elif`

在 Python 中，关键字 `elif` 是“否则如果”的缩写。 使用 `elif` 语句可以将多个测试表达式添加到程序中。 这些语句按照其编写顺序运行，因此只有当第一个 `if` 语句为 `False` 时，程序才会输入 `elif` 语句。 例如：

```python
a = 27
b = 93
if a <= b:
    print("a is less than or equal to b")
elif a == b:
    print("a is equal to b")
```

输出：`a is less than or equal to b`

在此变体中，代码块中的 `elif` 语句不会运行，因为 `if` 语句为 `True`。

`if/elif` 语句的语法为：

```python
if test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run
```

### 结合使用 `if`、`elif` 和 `else` 语句

可以结合使用 `if`、`elif` 和 `else` 语句来创建具有复杂条件逻辑的程序。 请记住，仅当 `if` 条件为 `false` 时才运行 `elif` 语句。 另请注意，一个 `if` 块只能有一个 `else` 块，但它可以有多个 `elif` 块。

我们来看一个包含 `if`、`elif` 和 `else` 语句的示例：

```python
a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b")    
```

使用所有三种类型语句的代码块具有以下语法：

```python
if test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run
else:
    # statement(s) to be run
```

### 使用嵌套条件逻辑

Python 还支持嵌套条件逻辑，这意味着你可以嵌套 `if`、`elif` 和 `else` 语句来创建更复杂的程序。 若要嵌套条件，请缩进内部条件，同一缩进级别的所有内容都将在同一代码块中运行：

```python
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")
```

此代码段生成输出 `a is less than b`。

嵌套条件逻辑与每个代码块中的常规条件逻辑遵循相同的规则。 下面是语法的示例：

```python
if test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
elif test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
else:
    # statement(s) to be run
```

## 什么是“and”和“or”运算符？

有时，你可能需要合并测试表达式以在一个 `if`、`elif` 或 `else` 语句中评估多个条件。 在这种情况下，将使用布尔运算符 `and` 和 `or`。

### `or` 运算符

可以使用布尔 `or` 运算符连接两个布尔或测试表达式。 要使整个表达式的计算结果为 `True`，至少有一个子表达式必须为 true。 如果子表达式均不为 true，则整个表达式的计算结果为 `False`。 例如，在以下表达式中，整个测试表达式的计算结果为 `True`，因为已满足子表达式中的条件之一：

```python
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)
```

如果两个子表达式都为 true，则整个测试表达式的计算结果也为 `True`。

使用 `or` 的布尔表达式具有以下语法：

```python
sub-expression1 or sub-expression2
```

### `and` 运算

还可以使用布尔 `and` 运算符连接两个测试表达式。 测试表达式中的两个条件都必须为 true，整个测试表达式的计算结果才为 `True`。 在任何其他情况下，测试表达式都为 `False`。 在以下示例中，整个测试表达式的计算结果为 `False`，因为子表达式中只有一个条件为 true：

```python
a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)
```

使用 `and` 的布尔表达式具有以下语法：

```python
sub-expression1 and sub-expression2
```

### `and` 和 `or` 之间的差异

若要突出显示两个布尔运算符之间的差异，可以使用真值表。 真值表根据两个子表达式显示整个测试表达式的计算结果。

下面是 `and` 的真值表：

| `subexpression1` | 运算符 | `subexpression2` | 结果    |
| :--------------- | :----- | :--------------- | :------ |
| `True`           | `and`  | `True`           | `True`  |
| `True`           | `and`  | `False`          | `False` |
| `False`          | `and`  | `True`           | `False` |
| `False`          | `and`  | `False`          | `False` |

下面是 `or` 的真值表：

| `subexpression1` | 运算符 | `subexpression2` | 结果    |
| :--------------- | :----- | :--------------- | :------ |
| `True`           | `or`   | `True`           | `True`  |
| `True`           | `or`   | `False`          | `True`  |
| `False`          | `or`   | `True`           | `True`  |
| `False`          | `or`   | `False`          | `False` |

-------------------------------

## Python 中的字符串基础知识

虽然 Python 中的字符串看起来简单直接，但字符串规则存在一定的复杂度，必须掌握它们。 了解规则有助于避免在修改值或设置文本格式时受到字符串行为的影响。

### 简单的字符串

在本单元的示例中，你有一个关于月球的事实，它被赋值到一个变量，如下所示：

```python
fact = "The Moon has no atmosphere."
print(fact)
```

输出显示已将文本分配给变量：`The Moon has no atmosphere.`

### 字符串的不可变性

在 Python 中，字符串是**不可变**的。 也就是说，它们不能更改。 字符串类型的此属性可能令人感到惊讶，因为在你更改字符串时，Python 不会显示错误。

你需要向已被赋值到一个变量的该事实添加另一个事实（句子）。 添加第二个事实似乎会改变变量，如以下示例所示：

```python
fact = "The Moon has no atmosphere."
fact + "No sound can be heard on the Moon."
```

你可能希望输出为：`The Moon has no atmosphere.No sound can be heard on the Moon.`

尽管可能看起来我们已经修改了变量 `fact`，但快速检查值后发现原始值没有变化：

```python
fact = "The Moon has no atmosphere."
fact + "No sound can be heard on the Moon."
print(fact)
```

输出：`The Moon has no atmosphere.`

技巧在于必须使用返回值。 添加字符串时，Python 不会修改任何字符串，但会返回一个新的字符串作为结果。 若要保留这个新结果，请将它分配给新变量：

```python
fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)
```

输出：`The Moon has no atmosphere.No sound can be heard on the Moon.`

操作字符串始终会生成新的字符串作为结果。

### 关于使用引号

可以用单引号、双引号或三引号将 Python 字符串引起来。 尽管可互换使用它们，但最好在项目中一致地使用一种类型。 例如，以下字符串使用双引号：

```python
moon_radius = "The Moon has a radius of 1,080 miles."
```

但是，如果字符串包含也用引号引起来的单词、数字或特殊字符（子字符串），则应使用其他样式。 例如，如果子字符串使用双引号，那么请用单引号将整个字符串引起来，如下所示：

```python
'The "near side" is the part of the Moon that faces the Earth.'
```

同样，如果在字符串中的任何位置有单引号（或撇号，如下例中的 Moon's 所示），请用双引号将整个字符串引起来：

```python
"We only see about 60% of the Moon's surface."
```

如果不能替换单引号和双引号，可能会导致 Python 解释器引发语法错误，如下所示：

```output
'We only see about 60% of the Moon's surface.'
  File "<stdin>", line 1
    'We only see about 60% of the Moon's surface.'
                                       ^
SyntaxError: invalid syntax
```

如果文本包含单引号和双引号的组合，可使用三引号来防止解释器出现问题：

```python
"""We only see about 60% of the Moon's surface, this is known as the "near side"."""
```

### 多行文本

有几种不同的方法可将多行文本定义为单个变量。 最常见的方法是：

- 使用换行符 (`\n`)。
- 使用三引号 (""")。

打印输出时，换行符将文本分隔到多行：

```python
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)
```

```Output
Facts about the Moon:
 There is no atmosphere.
 There is no sound.
```

可使用三引号到达这一目的：

```python
multiline = """Facts about the Moon:
 There is no atmosphere.
 There is no sound.
"""
 print(multiline)
```

## Python 中的字符串方法

字符串方法是 Python 中最常见的方法类型之一。 你通常需要操作字符串来提取信息或适应特定格式。 Python 包含几种旨在执行最常见和最有用的转换的字符串方法。

字符串方法是 `str` 类型的一部分。 这意味着这些方法作为字符串变量，或者直接作为字符串的一部分存在。 例如，`.title()` 方法以首字母大写形式返回字符串，并且可以直接与字符串一起使用：

```python
print("temperatures and facts about the moon".title())
```

输出：`Temperatures And Facts About The Moon`

变量上也有这样的行为和使用情况：

```python
heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)
```

### 拆分字符串

常见的字符串方法是 `.split()`。 如果没有参数，该方法将在每个空格处分隔字符串。 这将创建一个单词或数字列表，每个单词或数字由空格分隔：

```python
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures .split()
print(temperatures_list)
```

输出：`['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']`

在本示例中，你将处理多个行，因此可使用（隐式）换行符在每行的末尾拆分字符串，从而创建单行：

```python
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures .split('\n')
print(temperatures_list)
```

输出：`['Daylight: 260 F', 'Nighttime: -280 F']`

当需要循环来处理或提取信息时，或者从文本文件加载数据时，这种类型的拆分会非常方便。

### 搜索字符串

某些字符串方法还可在处理之前查找内容，而无需使用循环。 假设你有两个讨论不同行星和月球温度的语句。 但是，你只对与月球相关的温度感兴趣。 也就是说，如果句子没有讨论月球，则不应处理这些句子来提取信息。

要发现某个字符串中是否存在给定的单词、字符或字符组，最简单的操作是使用 `in` 运算符：

```python
print("Moon" in "This text will describe facts and challenges with space travel")
```

输出：`False`

```python
print("Moon" in "This text will describe facts about the Moon")
```

输出：`True`

要查找特定单词在字符串中的位置，一种方法是使用 `.find()` 方法：

```python
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))
```

输出：`-1`

如果找不到该单词，`.find()` 方法会返回 `-1`；否则它将返回索引（表示字符串中的位置的数字）。 这是搜索“Mars”（火星）一词时的行为方式：

```python
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))
```

输出：`64`

`64` 是字符串中出现 `"Mars"` 的位置。

搜索内容的另一种操作是使用 `.count()` 方法，这将返回某个单词在字符串出现的总次数：

```python
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))
```

```Output
1
0
```

Python 中的字符串区分大小写，这意味着 Moon 和 moon 被视为不同的单词。 若要执行不区分大小写的比较，可使用 `.lower()` 方法将字符串转换为全部是小写字母：

```python
print("The Moon And The Earth".lower())
```

输出：`the moon and the earth`

与 `.lower()` 方法类似，字符串具有执行相反操作（即，将每个字符都转换为大写）的 `.upper()` 方法：

```python
print("The Moon And The Earth".upper())
```

输出：`THE MOON AND THE EARTH`

----------------

*提示：搜索和检查内容时，更可靠的方法是将字符串小写，这样大小写就不会妨碍匹配。 例如，如果计算单词 the 出现的次数，则方法不会计算 The 出现的次数，即使这两者是同一个词。 可使用 `.lower()` 方法将所有字符都更改为小写。*

### 检查内容

有时，你将处理文本来提取在呈现中不规则的信息。 例如，下面的字符串比非结构化段落更容易处理：

```python
temperatures = "Mars Average Temperature: -60 C"
```

为了提取火星上的平均温度，可使用以下方法：

```python
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
```

```Output
['Mars average temperature', ' -60 C']
' -60 C'
```

上述方法信任冒号 (`:`) 后的所有内容都是温度。 字符串在 `:` 处进行拆分，这将生成一个包含两个项的列表。 在列表中使用 `[-1]` 将返回最后一项，在本示例中就是温度。

如果文本不规则，则不能使用这些拆分方法来获取值。 必须循环访问这些项，并检查值是否属于某种类型。 Python 提供了方法来帮助检查字符串的类型：

```python
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
```

输出：`30`

与 `.isnumeric()` 方法一样，`.isdecimal()` 可检查类似于小数的字符串。

----

*重要：知道 `"-70".isnumeric()` 会返回 `False` 可能令人吃惊。 这是因为字符串中的所有字符都必须是数字，而短划线 (`-`) 不是数字。 如果需要检查字符串中的负数，则 `.isnumeric()` 方法不起作用。*



可对字符串应用额外的验证来检查值。 对于负数，短划线是数字的前缀，可通过 `.startswith()` 方法进行检测：

```python
print("-60".startswith('-'))
```

输出：`True`

同样，`.endswith()` 方法有助于验证字符串的最后一个字符：

```python
if "30 C".endswith("C"):
	print("This temperature is in Celsius")
```

输出：`This temperature is in Celsius`

### 转换文本

如果需要将文本转换为其他内容，还有其他方法可提供帮助。 到目前为止，你已经看到了可用 C 表示 Celsius（摄氏度），用 F 表示 Fahrenheit（华氏度）的字符串。 你可使用 `.replace()` 方法查找某个字符或某一组字符的出现情况并替换它们：

```python
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
```

输出：`Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.`

如前文所述，`.lower()` 是规范化文本来执行不区分大小写的搜索的好方法。 让我们快速查看一些文本是否讨论了温度：

```python
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)
```

输出：`False`

```python
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())
```

输出：`True`

你可能不需要总是执行不区分大小写的验证，但当文本大小写混用时，将每个字母小写是一种很好的方法。

拆分文本并执行转换后，你可能需要将所有部分重新组合在一起。 正如 `.split()` 方法可分隔字符一样，`.join()` 方法可将它们重新组合在一起。

`.join()` 方法要求可迭代项（例如 Python 列表）作为参数，因此它的用法看起来与其他字符串方法不同：

```python
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
```

输出：`The Moon is drifting away from the Earth. On average, the Moon is moving about 4cm every year.`

在本示例中，使用 `' '` 来联接列表中的每一项。

---

## Python 中的字符串格式

除了转换文本和执行基本操作（例如匹配和搜索）外，在显示信息时必须设置文本的格式。 要使用 Python 显示文本信息，最简单的方法是使用 `print()` 函数。 你会发现，将变量中的信息和其他数据结构获取到 `print()` 可使用的字符串中非常重要。

在本单元中，你将了解通过使用 Python 在文本中包含变量值的几个有效方法。

### 百分号 (`%`) 格式

字符串中变量的占位符为 `%s`。 在字符串之后，使用另一个 `%` 字符，后跟变量名称。 以下示例演示如何使用 `%` 字符设置格式：

```python
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
```

输出：`On the Moon, you would weigh about 1/6 of your weight on Earth.`

使用多个值将更改语法，因为它需要用括号括住传入的变量：

```python
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
```

输出：`Both sides of the Moon get the same amount of sunlight, but only one side is seen from Earth because the Moon rotates around its own axis when it orbits Earth.`

***提示***:尽管此方法仍然是设置字符串格式的有效方法，但在处理多个变量时，它可能会导致错误并降低代码的清晰性。 本单元中还描述了其他两个格式设置选项，其中任何一个都更适合此目的。

### `format()` 方法

`.format()` 方法使用大括号 (`{}`) 作为字符串中的占位符，并使用变量赋值来替换文本。

```python
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
```

输出：`On the Moon, you would weigh about 1/6 of your weight on Earth.`

不需要给重复的变量赋值多次，使它变得更简洁，因为需要赋值的变量变少了:

```python
mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
```

输出：`You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth.`

替换使用的是数字，而不是空的大括号。 `{0}` 表示使用 `.format()` 的第一个（索引 0）参数，在本例中是 `Moon`。 对于简单的重复，`{0}` 效果很好，但它会降低可读性。 为了提高可读性，请在 `.format()` 中使用关键字参数，并在大括号内引用这些参数：

```python
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))
```

输出：`You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth.`

### 关于 f-string

从 Python 版本 3.6 开始，可使用 f-string。 这些字符串看起来像模板，并使用代码中的变量名称。 在上例中使用 f-string 将得到如下结果：

```python
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
```

输出：`On the Moon, you would weigh about 1/6 of your weight on Earth.`

变量在大括号中，并且字符串必须使用 `f` 前缀。

f-string 比任何其他格式设置选项都更简洁。除了它之外，还可用大括号将表达式括起来。 这些表达式可以是函数或直接操作。 例如，如果想要将 `1/6` 值表示为具有一个小数位的百分比，可直接使用 `round()` 函数：

[^round()]:round(数,小数位数)

[另一用法](###舍入)： 舍入

```python
print(round(100/6, 1))
```

输出：`16.7`

使用 f-string 时，无需提前向变量赋值：

```python
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")
```

输出：`On the Moon, you would weigh about 16.7% of your weight on Earth.`

使用表达式不需要函数调用。 任何字符串方法也能做到这一点。 例如，字符串可强制使用特定的大小写来创建标题：

```python
subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)
```

输出：`Interesting Facts About The Moon`



---

## 列表简介

Python 具有许多内置类型，例如字符串和整数。 Python 有一种用于存储值集合的类型：列表。

### 创建列表

你可以通过将一系列值分配给变量来创建列表。 每个值用逗号分隔并用方括号 (`[]`) 括起来。 以下示例将所有行星的列表存储在 `planets` 变量中：

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
```

### 按索引访问列表项

可以通过将索引括在列表变量名称后的方括号 `[]` 中来访问列表中的任何项。 索引从 0 开始，因此在以下代码中，`planets[0]` 是列表 `planets` 中的第一项：

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
```

```Output
The first planet is Mercury
The second planet is Venus
The third planet is Earth
```

***备注***：由于所有索引都从 0 开始，因此 `[1]` 是第二项，`[2]` 是第三项，依此类推。

还可以使用索引修改列表中的值。 为此，可以分配一个新值，方法与分配变量值大致相同。 例如，可以更改列表中火星的名称以使用其别名：

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])
```

输出：`Mars is also known as Red Planet`

### 确定列表的长度

若要获取列表的长度，请使用内置函数 `len()`。 以下代码创建一个新变量 `number_of_planets`。 该代码为该变量分配列表 `planets` 中的项数 (8)。

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
```

输出：`There are 8 planets in the solar system`

### 向列表中添加值

Python 中的列表是动态的：可以在创建项后添加和删除项。 若要向列表中添加项，请使用方法 `.append(value)`。

例如，以下代码将字符串 `"Pluto"` 添加到列表 `planets` 的末尾：

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
```

输出：`There are actually 9 planets in the solar system.`

### 从列表中删除值

通过对列表变量调用 `.pop()` 方法，可以删除列表中的最后一项：

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")
```

### 使用负索引

请查看如何使用索引来提取列表中的单个项：

```python
print("The first planet is", planets[0])
```

输出：`The first planet is Mercury`

索引从零开始并增加。 负索引从列表末尾开始，并向后执行。

在以下示例中，`-1` 的索引返回列表中的最后一项。 `-2` 的索引返回倒数第二项。

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])
```

```Output
The last planet is Neptune
The penultimate planet is Uranus
```

如果想返回倒数第三项，请使用 `-3` 的索引（依此类推）。

### 在列表中查找值

若要确定某值在列表中的存储位置，请使用列表的 `index` 方法。 此方法在列表中搜索值并返回该项的索引。 如果未找到匹配项，则返回 `-1`。

以下示例显示使用 `"Jupiter"` 作为索引值：

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
```

输出：`Jupiter is the 5 planet from the sun`

***备注***：由于索引从 0 开始，所以需要加 1 才能显示正确的数字。

再提供一个示例：

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
mercury_index = planets.index("Mercury")
print("Mercury is the", mercury_index + 1, "planet from the sun")
```

输出：`Mercury is the 1 planet from the sun`



## 使用列表中的数字

### 在列表中存储数字

若要在 Python 中存储带小数位的数字，请使用 `float` 类型。 若要创建浮点数，请输入带小数位的数字并将其分配给变量：

```python
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
```

以下代码创建一个列表，显示太阳系中所有八颗行星的重力，以 G 为单位：

```python
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
```

在这个列表中，`gravity_on_planets[0]` 是水星上的重力 (0.378 G)，`gravity_on_planets[1]` 是金星上的重力 (0.907 G)，依此类推。

在地球上，一辆双层巴士重达 124,054 牛顿 (N)。 在重力为 0.378 G 的水星上，同一辆巴士的重量为 124,054 牛顿乘以 0.378。 在 Python 中，要将两个值相乘，请使用 `*` 符号。

在以下示例中，可以通过从列表中获取值来计算不同行星上双层巴士的重量：

```python
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")
```

```Output
On Earth, a double-decker bus weighs 124054 N
On Mercury, a double-decker bus weighs 46892.4 N
```

### 将 `min()` 和 `max()` 与列表配合使用

Python 具有用于计算列表中最大和最小数字的内置函数。 `max()` 函数返回最大数，`min()` 返回最小数。 因此 `min(gravity_on_planets)` 返回 `gravity_on_planets` 列表中的最小数，即 0.377（火星）。

以下代码使用这些函数计算太阳系中的最小和最大重量：

```python
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")
```

```Output
On Earth, a double-decker bus weighs 124054 N
The lightest a bus would be in the solar system is 46768.35 N
The heaviest a bus would be in the solar system is 292767.44 N
```



## 操作列表数据

你可能需要使用列表的不同部分。 例如，假设有一个包含不同月份降雨量的列表。 要正确分析此类数据，可能需要查找某三个月内的降雨量。 或者你可能希望按照降雨量从多到少的顺序对列表进行排序。

Python 为处理列表中的数据提供了强大的支持。 这种支持包括切片数据（仅检查一部分）和排序。

### 切片列表

可以使用切片来检索部分列表。 切片使用方括号，但不是仅包含单个项，而是具有起始和结束索引。 使用切片时，会创建一个新列表，该列表从起始索引开始，在结束索引之前（并且不包括）结束。

行星列表有八项。 地球是列表中的第三项。 若要获取地球之前的行星，请使用切片获取从 0 开始到 2 结束的项：

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)
```

输出：`['Mercury', 'Venus']`

请注意，列表中不包含地球。 原因在于该索引在结束索引之前结束。

若要获取地球之后的所有行星，请从第三项开始，到第八项：

```python
planets_after_earth = planets[3:8]
print(planets_after_earth) 
```

输出：`['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']`

在本例中，显示了海王星。 原因是海王星的索引是 `7`，而索引从 `0` 开始。 由于结束索引是 `8`，因此包含最后一个值。 如果未将停止索引置于切片中，Python 会假定你要转到列表的末尾：

```python
planets_after_earth = planets[3:]
print(planets_after_earth)
```

输出：`['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']`

***重要***：切片会创建一个新列表。 它不会修改当前列表。

### 联接列表

你已了解如何使用切片来拆分列表，但是如何将它们重新联接在一起呢？

若要联接两个列表，可以将另一个运算符 (`+`) 与两个列表一起使用，以返回一个新列表。

木星有 79 颗已知卫星。 最大的四颗是木卫一、木卫二、木卫三和木卫四。 这些卫星被称为伽利略卫星，因为伽利略·伽利莱在 1610 年用他的望远镜发现了它们。 比伽利略卫星群更接近木星的是阿马尔塞卫星群。 它由卫星木卫十六、木卫十五、木卫五和木卫十四组成。

创建两个列表。 用四个阿马尔塞卫星填充第一个列表，用四个伽利略卫星填充第二个列表。 使用 `+` 将它们联接在一起以创建一个新列表：

```python
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
```

输出：`The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']`

***重要***：联接列表会创建一个新列表。 它不会修改当前列表。

### 对列表进行排序

若要对列表进行排序，请对列表使用 `.sort()` 方法。 Python 按字母顺序对字符串列表排序，按数字顺序对数字列表排序：

```python
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
```

输出：`The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']`

若要以相反的顺序对列表进行排序，请对列表调用 `.sort(reverse=True)`：

```python
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
```

输出：`The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']`

***重要***：使用 `sort` 修改当前列表。操作列表数据



