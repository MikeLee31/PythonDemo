import os
import urllib.request


# 下载图片 url 图片url;filepath 保存路径;filename 保存名字
def url_download_img(url, filepath, filename):
    try:
        # 如果没有这个path则直接创建
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        # 提取图片url的格式如http://img.1.jpg为.jpg
        file_suffix = os.path.splitext(url)[1]
        print(file_suffix)
        final_name = '{}/{}{}'.format(filepath, filename, file_suffix)
        # 拼接文件名。
        print(final_name)
        # 利用urllib.request.urltrieve方法下载图片
        urllib.request.urlretrieve(url, filename=final_name)
        print("下载完成")
    except IOError as e:
        print(1, e)
    except Exception as e:
        print(2, e)


if __name__ == '__main__':
    url = 'http://img.jingtuitui.com/759fa20190115144450401.jpg'
    url_download_img(url, "Spider/img", "pcio")
