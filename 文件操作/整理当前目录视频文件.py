import os
import LhFileUtils


def show_current_dir_list(path):
    # 列出文件夹下所有的目录与文件
    current_dir_list = os.listdir(path)
    # print(current_dir_list)
    for i in range(0, len(current_dir_list)):
        item_name_str = current_dir_list[i]
        item_path = os.path.join(path, item_name_str)
        name = ''
        try:
            if item_name_str.find('-') != -1:
                if os.path.isdir(item_path):
                    name = item_name_str.split('_')[-1]
                else:
                    name = item_name_str[:-4].split('_')[-1]
                    # print(name)
        except Exception as r:
            print(r, item_name_str)
            continue
        LhFileUtils.mkdir(f"{path}\\{name}")
        now_item_path = item_path
        target_item_path = f"{path}\\{name}\\{item_name_str}"
        print(now_item_path)
        print(target_item_path)
        LhFileUtils.movefile(now_item_path, target_item_path)


if __name__ == '__main__':
    root = 'E:\ThunderCloud'
    show_current_dir_list(root)
