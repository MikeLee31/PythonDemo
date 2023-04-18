import os
import shutil
import sys
import re
from sys import exit


# 拷贝文件
#     不可用于文件夹
# 用法如下
#     s = "D:\\requirements.txt"
#     t = "D:\\Code\\requirements.txt"
#     copyfile(s, t)
def copyfile(source, target):
    try:
        shutil.copyfile(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())


# 新建文件夹
#     新建成功返回真,否则返回假
# 用法如下
#     mkdir('E:\ThunderCloud')
def mkdir(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        os.mkdir(path)
        return True
    else:
        return False

# 列出文件夹结构
# 用法如下
#     traverse_path('E:\ThunderCloud')
def traverse_path(root_path, layer=0):
    print("--" * layer, end="")
    print("目录：" + root_path.split('\\')[-1])

    lis = os.listdir(root_path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(lis)):
        path = os.path.join(root_path, lis[i])
        is_file = os.path.isfile(path)
        if is_file:
            print("--" * (layer+1), end="")
            print(lis[i])
        else:
            # print(path)
            traverse_path(path, layer + 1)


if __name__ == '__main__':
    traverse_path('E:\ThunderCloud')
