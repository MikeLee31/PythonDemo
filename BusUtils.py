import os
import cv2
"""
添加后缀
删除最后的_
获取视频信息-一般是帧高

"""


# 添加后缀,同时改大写
def add_last(path, suffix_name):
    # 列出文件夹下所有的目录与文件
    current_dir_list = os.listdir(path)
    for i in range(0, len(current_dir_list)):
        item_name_str = current_dir_list[i]
        item_path = os.path.join(path, item_name_str)
        # 改大写
        new_name = item_name_str.upper()
        new_item_path = os.path.join(path,new_name)
        if os.path.isfile(item_path):
            item_suffix = item_name_str.split('.')[-1]
            os.rename(item_path, new_item_path[:-4] + "_" + suffix_name +'.'+ item_suffix)

# 添加后缀,同时改大写
def add_frame_height(path):
    # 列出文件夹下所有的目录与文件
    current_dir_list = os.listdir(path)
    for i in range(0, len(current_dir_list)):
        item_name_str = current_dir_list[i]
        # 获得文件路径
        item_path = os.path.join(path, item_name_str)
        suffix_name = get_video_info(item_path)+"p"
        print(suffix_name)
        # 改大写
        new_name = item_name_str.upper()
        new_item_path = os.path.join(path,new_name)
        if os.path.isfile(item_path):
            item_suffix = item_name_str.split('.')[-1]
            # os.rename(item_path, new_item_path[:-4] + "_" + suffix_name +'.'+ item_suffix)

# 去除最后的_
def remove_lats(path):
    # 列出文件夹下所有的目录与文件
    current_dir_list = os.listdir(path)
    for i in range(0, len(current_dir_list)):
        item_name_str = current_dir_list[i]
        item_path = os.path.join(path, item_name_str)
        # 去除最后的_
        new_name=''
        if item_name_str[-5]=='_':
            new_name = item_name_str[:-1]
        else:
            new_name = item_name_str
        new_item_path = os.path.join(path, new_name)
        if os.path.isfile(item_path):
            item_suffix = item_name_str.split('.')[-1]
            os.rename(item_path, new_item_path[:-4] + '.' + item_suffix)

# 获取视频帧高
def get_video_info(filepath):
    # 打开视频文件
    cap = cv2.VideoCapture(filepath)
    # 视频的帧数
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 视频的帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 视频帧高
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    return str(int(height))

if __name__ == '__main__':
    root = 'E:\ThunderCloud\\6.4'
    add_frame_height(root)
