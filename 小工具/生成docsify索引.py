import os
import sys
import shutil
import time

path = './.backup'
file_dir = '../'


# 如果目录不存在则新建目录
def mkdir(dir_path):
	isExists = os.path.exists(dir_path)
	if not isExists:
		os.mkdir(dir_path)


# 生成导航栏目录md文字
# filetype 为README或_navbar
# pre_str1 一级索引前置
# pre_str2 二级索引前置
def generate(filetype, pre_str1, pre_str2):
	filename = filetype + ".md"
	filename_backup = filetype + "_backup" + time.strftime("%Y_%m_%d_%H%M%S", time.localtime()) + ".md"
	print("备份文件名:" + filename_backup)
	print("文件名:" + filename)
	# 备份文件
	target_filepath = path + "/" + filename_backup
	print("备份路径为" + target_filepath)
	if os.path.exists("./" + filename):
		shutil.copyfile("./" + filetype + ".md", target_filepath)
		print("备份成功")
		os.remove("./" + filename)
		print("删除成功")

	print("当前路径为：" + os.getcwd())

	fo = open(filename, 'w', encoding='utf8')
	# 添加主页
	homepage = pre_str1 + ' [Home](README)\n'
	fo.write(homepage)
	print(homepage)
	for root, dirs, files in os.walk(file_dir):
		root = root[2:]
		if root != '' and root[0] != '.' and '\\' not in root:
			# 索引标题 如 * OpenCV
			start_index = pre_str1 + " " + root + "\n"
			print(start_index)
			fo.write(start_index)
			# 该文件夹中内容
			for file in files:
				if os.path.splitext(file)[1] == '.md':  # 想要保存的文件格式
					str1 = "{} [{}](/{}/{})\n".format(pre_str2, file[0:-3], root, str(file))
					print(str1)
					fo.write(str1)


if __name__ == '__main__':
	mkdir(path)
	generate('_navbar', "*", "    *")
	generate('README', "#", "####")
