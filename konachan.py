# -*- coding:utf-8 -*-
import os
import urllib.parse

import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809',
}


def ua():
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    }
    return headers


def printf(out):
    log_output = open('../log.txt', 'a+')
    print(out, file=log_output)
    print(out)
    log_output.close()


# 找到所有附件
def down(url):
    global r, file_count, sum_pic, down_name, down_size
    for item in bs.find_all('a', class_="directlink largeimg"):
        str0 = item.get('href')
        if str0 is None:
            return 0
        str1 = str(str0)
        where = str1.find('-')
        str2 = str1[where + 13:]
        str3 = urllib.parse.unquote(str2)[3:]
        where2 = str3.find(' ')

        down_name = str3[where2 + 1:]
        while os.path.exists(down_name):
            r = requests.get(url=str1, headers=ua(), timeout=6, proxies=proxies)
            down_size = eval(r.headers['Content-Length'])

            if os.path.getsize(down_name) == down_size:
                printf(f'图片{down_name}存在，跳过')
                break
            else:
                while os.path.exists(down_name):
                    D = down_name.find('.')
                    down_name = down_name[:D] + ' ' + down_name[D:]

        try:
            r = requests.get(url=str1, headers=ua(), timeout=6, proxies=proxies)
        except:
            printf('请求失败！\n再次尝试')
            try_count = 1
            while try_count < 4:
                try:
                    r = requests.get(url=str1, headers=ua(), timeout=6, proxies=proxies)
                    try_count = 4
                except:
                    printf(f'第{try_count}次尝试失败，再次尝试')
                    try_count += 1
            else:
                printf(f'下载{down_name}失败')
        try:
            r = requests.get(url=str1, headers=ua(), timeout=6, proxies=proxies)
            with open(down_name, 'wb') as f:
                f.write(r.content)
        except:
            printf(f'文件{down_name}写入失败！再次尝试')
            try_count = 1
            while try_count < 4:
                try:
                    r = requests.get(url=str1, headers=ua(), timeout=6, proxies=proxies)
                    with open(down_name, 'wb') as f:
                        f.write(r.content)
                except:
                    printf(f'第{try_count}次尝试失败，再次尝试')
                    try_count += 1
            else:
                printf(f'文件{down_name}写入失败')
        else:
            sum_pic += 1
            printf(f"下载第{page}页第{file_count}张总第{sum_pic}图片:{down_name} 完成！")

        file_count = file_count + 1
    return 1


os.chdir(input('输出目录：\n'))
tag = input('请输入Tag\n')
if os.path.exists(tag):
    os.chdir(f'.\\{tag}')
else:
    os.makedirs(tag)
    os.chdir(f'.\\{tag}')

sum_pic = 0
from_page=eval(input('开始页数：'))
for page in range(from_page, 22222):
    url = 'https://konachan.com/post?page=' + str(page) + '&tags=' + tag
    resp = requests.get(url, proxies=proxies).text  # 获取网页文件
    bs = BeautifulSoup(resp, "lxml")
    file_count = 1
    if not down(url):
        break
printf('下载完成')
a = input('按任意键退出')
