from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def selenium_init():
    # 使用selenium库调用ChromeDriver操作Chrome
    # 导入chromedriver配置路径
    config = Service(r"D:\Code\chromedriver.exe")
    # 加载配置路径
    return webdriver.Chrome(service=config)


def get_user_name(web_url):
    browser = selenium_init()
    browser.get(web_url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    name = soup.find_all('title')
    browser.close()
    return name[0].text[:-8]


def getdyHeader():
    headers = {
        'accept-encoding': 'deflate',
        'accept-language': 'zh-CN,zh;q=0.9',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    }
    return headers

def get_user_videos_list():
    user_video_url = "https://www.iesdouyin.com/web/api/v2/aweme/post/"
    user_video_params = {
        'sec_uid': sec_uid,
        'count': '21',
        'max_cursor': '0',
        'aid': '1128',
        '_signature': '2Vx9mxAZh0o-K4Wdv7NFKNlcfY',
        'max_cursor': ''
    }
    video_urls = []
    max_cursor, video_count, user_name = None, 0, None
    while True:
        # time.sleep(1)
        if max_cursor:
            user_video_params['max_cursor'] = str(max_cursor)
        aweme_count = 0
        while True:
            res = requests.get(user_video_url, headers=headers, params=user_video_params)
            print(res.text)
            js = json.loads(res.text)
            if len(js['aweme_list']) != 0:
                break
            else:
                aweme_count = aweme_count + 1
                time.sleep(5)
            if aweme_count == 3:
                break

        if aweme_count == 3:
            print("当前用户无作品")
        else:
            if not user_name:
                user_name = js['aweme_list'][0]['author']['nickname']
            for i in js['aweme_list']:
                video_count += 1
                video_urls.append((i['video']['play_addr']['url_list'][0], i['desc']))
                time.sleep(0.1)
            if js.get('has_more'):
                max_cursor = js.get('max_cursor')
            else:
                break
