import os
import shutil
import sys
import re
from sys import exit
import sys
import hashlib


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


# 移动文件
#     不可用于文件夹
# 用法如下
#     s = "D:\\requirements.txt"
#     t = "D:\\Code\\requirements.txt"
#     copyfile(s, t)
def movefile(source, target):
    try:
        shutil.move(source, target)
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
            print("--" * (layer + 1), end="")
            print(lis[i])
        else:
            # print(path)
            traverse_path(path, layer + 1)


# 列出文件夹下所有的目录与文件
def get_all_item_dir(path):
    file_dir = {}
    item_name_str_list = os.listdir(path)
    for i in range(0, len(item_name_str_list)):
        item_name_str = item_name_str_list[i]
        item_path = os.path.join(path, item_name_str)
        if os.path.isfile(item_path):
            file_dir[item_name_str] = item_path
        if os.path.isdir(item_path):
            temp_dir = get_all_item_dir(item_path)
            file_dir.update(temp_dir)
    return file_dir


# 计算MD5
def calMD5(path):
    with open(path, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    return file_md5

def example(path, suffix):
    # 列出文件夹下所有的目录与文件
    lis = os.listdir(path)
    print(len(lis))
    for i in range(0, len(lis)):
        # 拼接链接
        name = lis[i]
        temp_path = os.path.join(path, lis[i])
        # 如果是文件
        if os.path.isfile(temp_path):
            pass

        # 如果是目录
        if os.path.isdir(temp_path):
            pass

def add_suffix(path, suffix):
    # 列出文件夹下所有的目录与文件
    lis = os.listdir(path)
    print(len(lis))
    for i in range(0, len(lis)):
        # 拼接链接
        name = lis[i]
        temp_path = os.path.join(path, lis[i])
        # 如果是文件
        if os.path.isfile(temp_path):
            # 获得.隔开的标签
            str_filename = lis[i].split('.')
            # 如果不存在该标签
            # print(str_filename.count(suffix))
            if str_filename.count(suffix) == 0:
                str_filename.insert(-1, suffix)
                new_name = os.path.join(path,'.'.join(str_filename))
                os.rename(temp_path,new_name)



if __name__ == '__main__':
    root = "D:\Download\WW\HEVC"
    add_suffix(root,'HEVC')
