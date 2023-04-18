import time

import requests
from bs4 import BeautifulSoup


def get_content(target):
    req = requests.get(url=target)
    req.encoding = 'gbk'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0' * 4)
    return content


if __name__ == '__main__':
    server = 'https://www.qbiqu.com'
    book_name = '星界使徒_'

    target = 'https://www.qbiqu.com/77_77840/'
    req = requests.get(url=target)
    req.encoding = 'gbk'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    chapters = bs.find('div', id='list')
    chapters = chapters.find_all('a')
    chapters = chapters[9:]
    print(chapters)
    book_name = book_name + chapters[-1].string[0:3] + '.txt'
    print(book_name)

    for chapter in chapters:
        chapter_name = chapter.string
        url = server + chapter.get('href')
        time.sleep(4)
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
        print(chapter_name+"下载完成")
