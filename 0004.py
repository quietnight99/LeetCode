

import os

def list_files(directory):
    file_list = []
    # 遍历目录中的所有文件和子目录
    for root, dirs, files in os.walk(directory):
        # 将找到的文件添加到列表中
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# 调用函数并打印结果
directory = './'
file_names = list_files(directory)
for file_name in file_names:
    print(file_name)
