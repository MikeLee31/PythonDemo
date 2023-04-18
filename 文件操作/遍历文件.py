import os



rootdir = 'E:\ThunderCloud'
lis = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0, len(lis)):
    # 拼接链接
    path = os.path.join(rootdir, lis[i])
    # 如果是文件
    if os.path.isfile(path):
        pass

    # 如果是目录
    if os.path.isdir(path):
        pass



