# -*- coding:utf-8 -*-
import os
import re
import requests
from bs4 import BeautifulSoup

remove = '\\/?*|<">: '


# 设置UA
def ua():
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    }
    return headers


# 下载单个页面内所有文件
def down_url(url):  # 定义函数
    global r, item, soup, bs
    try:
        resp = requests.get(url).text  # 获取网页文件
        bs = BeautifulSoup(resp, "lxml")
    except:
        print('获取网页文件失败！')
    # 计算附件数量
    name = []
    file_count = 0
    # 找到所有附件
    try:
        for item in bs.find_all('a', class_="post__attachment-link"):
            str0 = item.string
            str1 = str(str0)
            str1 = str1.strip()
            str1 = str1.lstrip('Download ')
            print('发现文件' + str1)  # 输出发现文件
            name.append(str1)
            file_count += 1
    except:
        print('找出所有附件失败！')
    try:
        item = bs.find('span')
        item = item.string
        for e in remove:
            item = item.replace(e, "")

        soup = bs.select('a.post__attachment-link')
    except:
        print('选择文件所在链接失败！')
    # 检查文件目录是否存在
    if os.path.exists('.//' + item):
        print('文件夹已存在，跳过创建')
        pass
    else:
        os.makedirs('.//' + item)
        print('已创建"' + item + '"文件夹')
    os.chdir('.//' + item)
    print('已进入该文件夹')

    # 遍历附件
    for i in range(file_count):
        down_name = name[i]
        for e in remove:
            down_name = down_name.replace(e, "")

        print(f"准备开始下载 {down_name} 文件..")
        # 检查附件是否存在
        if os.path.exists(down_name):
            print('文件存在，已跳过')
            pass
        else:
            # 下载附件
            try:
                down_url = 'https://kemono.party/' + soup[i].get("href")
                r = requests.get(url=down_url, headers=ua(), timeout=6, stream=True)
            except:
                print(f'下载{down_name}失败！')
            try:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                print(f"下载 {down_name} 文件完成！")
            except:
                print('写入文件失败！')

    # 下载图片
    pic_count = 0  # 计数便于命名
    try:
        for item in bs.find_all('a', class_="fileThumb", href=re.compile('data')):  # 找到原画质图片位置
            pic_count += 1
            pic_soup = item.get('href')
            # 遍历下载图片
            down_name = str(pic_count) + str(pic_soup)[-4:]  # 多图片按顺序命名
            for e in remove:
                down_name = down_name.replace(e, "")

            print(f"开始下载 {down_name} 文件..")  # 输出开始下载文件
            # 检查图片是否存在
            if os.path.exists(down_name):
                print('图片文件存在，已跳过')
                pass
            else:
                # 下载图片文件
                down_url = 'https://kemono.party/' + str(pic_soup)
                try:
                    r = requests.get(url=down_url, headers=ua(), timeout=6)
                except:
                    print('请求失败！')
                try:
                    with open(down_name, 'wb') as f:
                        f.write(r.content)
                except:
                    print(f'文件{down_name}写入失败！')
                else:
                    print(f"下载图片 {down_name} 完成！")
        print('下载图片任务完成')
        os.chdir('..//')
        print('已回到上级目录')  # 回到上级目录
    except:
        print('下载该页面图片失败！')



file_path = 'task_server.txt'
down_path = 'E:/22'
with open(file_path, encoding='utf-8') as file_obj:
    while True:
        os.chdir(down_path)
        line = file_obj.readline()
        line = line.rstrip()
        print(line)
        if line == '':
            break
        print('开始下载该链接下的画师：' + line)
        url = line
        resp = requests.get(url).text
        bs = BeautifulSoup(resp, "lxml")
        t1 = bs.find_all('a')
        href_list = []
        # 创建画师文件夹
        role = str(bs.find('span', itemprop="name"))
        role = role[22:]
        role = role[:-7]
        for e in remove:
            role = role.replace(e, "")

        if os.path.exists('.//' + role):
            pass
        else:
            os.makedirs('.//' + role)
            print('已创建画师文件夹：' + role)
        os.chdir('.//' + role)
        print(line)
        print('已进入画师文件夹' + role)
        for t2 in t1:
            t3 = t2.get('href')
            href_list.append(t3)
        final_list = []
        for id in href_list:
            if id not in final_list:
                final_list.append(id)
        num = len(final_list)
        for i in range(num):
            # 找到页面总数以及页面所有链接
            if ('fanbox/' or 'patron' or 'fantia') and 'user/' and 'o=' in str(final_list[i]):  # 判断是否为页面链接
                url = 'https://kemono.party' + str(final_list[i])  # 指定链接
                print('准备下载该页面下的单个页面所含文件：' + url)
                # 分析单个页面
                resp2 = requests.get(url).text
                bs2 = BeautifulSoup(resp2, "lxml")
                t12 = bs2.find_all('a')
                href_list2 = []
                # 获取页面链接列表
                for t22 in t12:
                    t32 = t22.get('href')
                    href_list2.append(t32)
                final_list2 = []
                # 去除重复链接
                for id in href_list2:
                    if id not in final_list2:
                        final_list2.append(id)
                num = len(final_list2)
                for i in range(num):
                    if ('fanbox/' or 'patron' or 'fantia') and 'user/' and 'post/' in str(
                            href_list2[i]):  # 判断是否为含资源的页面
                        url = 'https://kemono.party' + str(href_list2[i])  # 设置url链接
                        # down_url(url)  # 执行下载
                        print('已完成此链接下载：' + url)

print('所有下载任务完成')
