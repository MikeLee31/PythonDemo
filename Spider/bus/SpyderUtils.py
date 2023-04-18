import urllib.request

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def down_pic(url, path):  # 传入url和path下载图片
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, path)


# selenium初始化
def selenium_init():
    # 使用selenium库调用ChromeDriver操作Chrome
    # 导入chromedriver配置路径
    config = Service(r"D:\Code\chromedriver.exe")
    # 加载配置路径
    return webdriver.Chrome(service=config)


# js指令移动到底部
def move_bottom(browser):
    js_bottom = "var q=document.documentElement.scrollTop=10000"
    browser.execute_script(js_bottom)


# 获取头部Header
def get_header():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
    }
    return header
