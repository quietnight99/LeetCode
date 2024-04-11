#
#
#
# print(3 > 4 or 4 < 3 and 1 == 1)
# print(1 < 2 and 3 < 4 or 1 > 2)
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
#
# print('\n')
# print(0 or 0)
# print(1 or 0)
# print(1 or 0 and 0)
# print(0 or 0 or 0)
# print(0 or 0 or 0)
# print(0 or 0 or 0)
#
#
# print("None")
# a = None
# if a:
#     print('--------------------------------')
#
# #
# # name = input("Name:")
# # age = input("Age:")
# # job = input("Job:")
# # hobby = input("Hobbie:")
#
#
# # 字符串切割
# s9 = "bao_heihei_nezha_huhu"
# lst = s9.split("_")
# # 字符串切割, 根据_进行切割
# print(type(lst),lst)
#
#
# lst = ['周杰伦', '王力宏', '麻花藤']
# s = "+".join(lst)
# print(type(s),s)  # 周杰伦_王力宏_麻花藤
#
#
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)  # True
# print(a is b)  # False
#
# c = '123'
# d = '123'
# print(c == d)  # True
# print(c is d)  # True
#
#
#
# def fun(*args):
#     print(args)
#
#
# lst = [1, 4, 7,5,4]
# fun(lst[0], lst[1], lst[2])
#
# fun(*list(set(lst))) # 可以使用*把一个列表按顺序打散
# s = "臣妾做不到"
# fun(*s) # 字符串也可以打散, (可迭代对象)
#
#
# s = "我的哈哈哈"
# print(dir(s)) # 可以打印对象中的方法和函数
# print(dir(str)) # 也可以打印类中声明的方法和函数

# s = "我的哈哈哈"
# print(dir(s)) # 可以打印对象中的方法和函数
# print(dir(str)) # 也可以打印类中声明的方法和函数


s = "我爱北京天安门"
c = s.__iter__()  # 获取迭代器
print(c.__next__())  # 使用迭代器进行迭代. 获取一个元素   我
print(c.__next__())  # 爱
print(c.__next__())  # 北
print(c.__next__())  # 京
print(c.__next__())  # 天
print(c.__next__())  # 安
print(c.__next__())  # 门


# print(c.__next__())  # StopIteration


def cloth() :
    for i in range(0, 10000) :
        yield "衣服" + str(i)


cl = cloth()
print(cl.__next__())
print(cl.__next__())
print(cl.__next__())
print(cl.__next__())

lst = [i * 2 for i in range(1, 15)]
print(lst)

f = lambda x : x + 1
print(f(10))


a = input(">>>")
b = input(">>>")
c = a if a > b else b
print(c)
