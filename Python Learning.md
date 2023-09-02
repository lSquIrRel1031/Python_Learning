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



### 逻辑运算符

|      |      |
| ---- | ---- |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |



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

## `and` 和 `or` 之间的差异

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
