# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from bs4 import BeautifulSoup
import requests
import os
import urllib.request


# 下载图片 url 图片url;filepath 保存路径;filename 保存名字
def url_download_img(img_url, filepath, file_name):
    # 使用异常模块
    try:
        # 如果没有这个path则直接创建
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        # 提取图片url的格式如http://img.1.jpg为.jpg
        file_suffix = os.path.splitext(img_url)[1]
        print(file_suffix)
        # 拼接存储的完整路径
        final_name = '{}/{}{}'.format(filepath, file_name, file_suffix)
        print(final_name)
        # 利用urllib.request.urltrieve方法下载图片
        urllib.request.urlretrieve(img_url, filename=final_name)
        print("下载完成")
    except IOError as e:
        print(1, e)
    except Exception as e:
        print(2, e)


# 查找某一个标签中特定class名字的内容
# web_url 网页的url;tag_name 标签名字;class_name 网页中类的名字
def download_img(web_url, tag_name, class_name):
    # 使用selenium库调用ChromeDriver操作Chrome
    # 导入chromedriver配置路径
    config = Service(r"D:\Code\chromedriver.exe")
    # 加载配置路径
    browser = webdriver.Chrome(service=config)
    # 访问网页
    browser.get(web_url)
    # 等待6s让网页内容加载出来
    sleep(20)

    # 使用BeautifulSoup4（bs4）解析文档
    # 第一个参数为 网页源代码 第二个参数为解析器使用 'lxml' 或者 'xml'都可以
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # 具体参见bs4库中find_all的说明文档
    # 该局意思为查找a标签中class属性为nbg的内容
    a_item = soup.find_all(tag_name, class_name)
    # a_item为一个列表,列表中是 bs4.element.Tag 对象
    for a in a_item:
        # a为一个bs4.element.Tag对象
        # print(a.text)
        # 获得图片url
        url = get_imgurl(a)
        # 获得需要的图片名字
        filename = get_imgname(a)
        # 下载图片
        url_download_img(url, "img", filename)
    # 记得关闭游览器
    browser.quit()


def get_imgurl(tag):
    u = tag.a.img['src']
    print(u)
    return u


def get_imgname(tag):
    name = tag.find_all_next('span', 'movie-name-text')
    print(name[0].a.string)
    return name[0].a.string


if __name__ == '__main__':
    # url1 = 'https://movie.douban.com/chart'
    url2 = 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action='
    download_img(url2, 'div', 'movie-content')
