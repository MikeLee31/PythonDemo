import os
import regex as re
import time


def list_root(rootdir):
    root = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    if len(root) <= 10:
        print(root)
    else:
        print(root[0:5], end="")
        print("...")
    for i in range(0, len(root)):
        file_path = os.path.join(rootdir, root[i])
        # 如果是目录
        if os.path.isdir(file_path) and root[i][0] != '.':
            print("进入目录--" + root[i])
            list_root(file_path)
            print("退出目录--" + root[i])
            print()
        if os.path.isfile(file_path):
            # 判断是否是md文件
            flag1 = file_path.find(".md")
            # 如果是视频文件
            if flag1 != -1:
                print("发现笔记文件：" + root[i])
                # 打开md文件然后进行替换
                copy_md_file_path = file_path[0:-3] + "_backup.md"
                print(copy_md_file_path)
                with open(file_path, 'r', encoding='utf8') as fr, \
                        open(copy_md_file_path, 'w', encoding='utf8') as fw:
                    data = fr.read()
                    data = re.sub('https://gitee.com/lh253514942/img_bed/raw/master', 'D:/Photos/img_bed', data)
                    fw.write(data)  # 新文件一次性写入原文件内容
                # 删除原文件
                os.remove(file_path)
                # 重命名新文件名为原文件名
                os.rename(copy_md_file_path, file_path)
                print(f'{file_path}替换完成...')
                time.sleep(1)


if __name__ == '__main__':
    list_root("D:\BaiduNetdiskWorkspace\code_data_lh\md")
