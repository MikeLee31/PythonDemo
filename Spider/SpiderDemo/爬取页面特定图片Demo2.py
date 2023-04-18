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
def download_img(web_url, sleep_time=6):
    # 使用selenium库调用ChromeDriver操作Chrome
    # 导入chromedriver配置路径
    config = Service(r"D:\Code\chromedriver.exe")
    # 加载配置路径
    browser = webdriver.Chrome(service=config)
    # 访问网页
    browser.get(web_url)
    # 等待6s让网页内容加载出来
    sleep(sleep_time)

    # 使用BeautifulSoup4（bs4）解析文档
    # 第一个参数为 网页源代码 第二个参数为解析器使用 'lxml' 或者 'xml'都可以
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # 具体参见bs4库中find_all的说明文档
    # 该局意思为查找a标签中class属性为nbg的内容
    img_obj = soup.find_all('a', 'bigImage')[0].img
    print(img_obj)
    title_obj = soup.find_all('h3')[0]
    print(title_obj)
    title_name = title_obj.string
    img_url = '{}{}'.format('https://www.javbus.com', img_obj['src'])
    print(img_url)

    # 保存图片
    url_download_img(img_url, './img', title_name)

    # 记得关闭游览器
    browser.quit()

# https://www.javbus.com/pics/cover/8qy2_b.jpg
if __name__ == '__main__':
    url1 = 'https://www.javbus.com/star/u4m'
    url2 = 'https://www.javbus.com/IPX-811'

    download_img(url2)
