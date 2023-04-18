# coding:utf-8

from time import sleep
from bs4 import BeautifulSoup
import os
from bus.SpyderUtils import *


def url_download_img(img_url, filepath, file_name):
    # 使用异常模块
    try:
        # 如果没有这个path则直接创建
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        # 提取图片url的格式如http://img.1.jpg为.jpg
        file_suffix = os.path.splitext(img_url)[1]
        # print("后缀为" + file_suffix)
        # 拼接存储的完整路径
        final_name = '{}/{}{}'.format(filepath, file_name, file_suffix)
        print("存储路径为" + final_name)
        # 下载图片
        if not os.path.exists(final_name):
            down_pic(img_url, final_name)
            print("下载完成")
        else:
            print(final_name + "已存在")
    except IOError as e:
        print(1, e)
    except Exception as e:
        print(2, e)


# 查找某一个标签中特定class名字的内容
# web_url 网页的url;tag_name 标签名字;class_name 网页中类的名字
def spyder(web_url, fold_name='default', sleep_time=6):
    browser = selenium_init()
    browser.get(web_url)
    # 等待6s让网页内容加载出来
    sleep(sleep_time)

    # 滚动到浏览器底部
    move_bottom(browser)
    sleep(sleep_time)

    # 使用BeautifulSoup4（bs4）解析文档
    # 第一个参数为 网页源代码 第二个参数为解析器使用 'lxml' 或者 'xml'都可以
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # 具体参见bs4库中find_all的说明文档
    link_items = soup.find_all('a', "movie-box")

    next_page = soup.find_all('a', id="next")

    for link_item in link_items:
        link = link_item['href']
        browser.get(link)
        sleep(sleep_time)
        soup2 = BeautifulSoup(browser.page_source, 'lxml')
        img_name = soup2.find_all('h3')[0].string
        print(img_name)
        img_url = "https://www.javbus.com/" + soup2.find_all('a', 'bigImage')[0]['href']
        print(img_url)
        # 下载图片
        url_download_img(img_url, 'E:\\Picture\\Actor\\' + fold_name, img_name)

    # 记得关闭游览器
    browser.quit()
    # 如果有下一页则接着爬
    if len(next_page) != 0:
        print(next_page[0])
        spyder("https://www.javbus.com" + next_page[0]['href'], fold_name, sleep_time)
    else:
        print("没有下一页,结束")


if __name__ == '__main__':
    # 枫花恋
    url1 = 'https://www.javbus.com/star/u4m'
    # 乙白沙耶香
    url2 = 'https://www.javbus.com/star/w5a'
    # 铃村爱里
    url3 = 'https://www.javbus.com/star/b64'
    # 三上悠亚
    url4 = 'https://www.javbus.com/star/okq'
    # 八卦海
    url5 = 'https://www.javbus.com/star/ws2'
    spyder(url5, fold_name="八卦海", sleep_time=1)
    print("全部已完成")

