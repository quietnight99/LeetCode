"""
遍历数据集合： 使用迭代器可以逐个访问集合中的元素，例如列表、元组、字典等。这在处理大量数据时非常有用，因为迭代器不会一次性加载整个数据集合到内存中，而是逐个访问元素，节省了内存空间。

文件读取： 在处理大型文件时，迭代器可以逐行读取文件内容，而不是一次性加载整个文件到内存中。这对于处理大型日志文件、CSV文件等非常有用。

生成器函数： 生成器函数是一种特殊的函数，可以使用 yield 关键字生成迭代器。生成器函数可以动态生成数据，而不需要一次性将所有数据存储在内存中。这对于处理大量数据或者需要按需生成数据的情况非常有用。

处理无限序列： 有些情况下，序列可能是无限的，例如生成斐波那契数列、素数序列等。迭代器可以按需生成序列中的元素，而不需要提前知道序列的长度。

惰性计算： 迭代器支持惰性计算，即只有在需要时才计算元素值。这对于处理复杂的数据转换、筛选、映射等操作时非常有用，可以节省计算资源。
"""

my_list = [1, 2, 3, 4, 5]
# 创建迭代器对象
my_iterator = iter(my_list)
print(type(my_list))
print(type(my_iterator))
print(id(my_list))
print(id(my_iterator))
# <class 'list'>
# <class 'list_iterator'>
# for item in my_iterator:
#     print(item) # 迭代器是一次性的，意味着一旦迭代器被耗尽，它就无法再次使用


# 使用 next() 函数遍历迭代器中的元素
print(next(my_iterator))  # 输出: 1
print(next(my_iterator))  # 输出: 2
print(next(my_iterator))  # 输出: 3
print(next(my_iterator))  # 输出: 4
print(next(my_iterator))  # 输出: 5


# 如果没有更多的元素可以返回，会引发 StopIteration 异常
# print(next(my_iterator))  # 引发 StopIteration 异常


# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)
# for item in my_iterator:
#     print(item)
