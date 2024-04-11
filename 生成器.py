def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
# 创建一个生成器对象
fib_gen = fibonacci(10)

# 使用 next() 函数逐个生成斐波那契数列的值
print(next(fib_gen))  # 输出: 0
print(next(fib_gen))  # 输出: 1
# 使用 for 循环迭代生成器对象
for num in fib_gen:
    print(num)  # 输出: 1，2,3，5, 8, 13, 21, ...



print('---------------')
def fib():
    a = 0
    b = 1
    yield a
    while True:
        a,b = b,a+b
        yield a
my_list = fib()
for i in range(10):
    print(next(my_list))

print('----------------')
lst = [1,2,3]
lst_iter = lst.__iter__()
while True:
    try:
        i = lst_iter.__next__()
        print(i)
    except StopIteration:
        break