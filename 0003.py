import itertools
import random

# 生成24点游戏题目
def calculate24(numbers) :
    # 生成所有可能的数字排列
    for perm in itertools.permutations(numbers) :
        # 生成所有可能的运算符组合
        for ops in itertools.product('+-*/', repeat = 3) :
            # 构建表达式
            expression = '{}{}{}{}{}{}{}'.format(perm[0], ops[0], perm[1], ops[1], perm[2], ops[2], perm[3])
            # 尝试计算表达式的结果
            try :
                result = eval(expression)
                # 如果结果为24，则返回表达式
                if result == 24 :
                    return expression
            except ZeroDivisionError :
                # 如果除数为0，则继续下一个表达式
                continue
    # 如果找不到解，则返回 "No solution found"
    return False


question = []
# 生成100个24点游戏
for i in range(1000) :
    # 随机生成四个数字（范围可以自行调整）
    numbers = random.sample(range(1, 14), 4)
    # 解决24点游戏
    solution = calculate24(numbers)
    if solution :
        print(solution)
        # question.append(list(str(solution)))
    # # 打印数字和解决方案
    # print(f"Game {i+1}: Numbers: {numbers}, Solution: {solution}")

# print(question)