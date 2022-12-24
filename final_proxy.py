# -*- coding:utf-8 -*-
import os
import re
import requests
from bs4 import BeautifulSoup

remove = '\\/?*|<">: \t \n'
page = 0
down_size_p = 11279
'''
proxies = {
    'http': 'socks5://127.0.0.1:10808',
    'https': 'socks5://127.0.0.1:10808',
}
'''
proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809',
}


# response = requests.get(url, proxies=proxies)


# 设置UA
def ua():
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    }
    return headers


# 下载单个页面内所有文件
def down_url(url):  # 定义函数
    global bs, item, soup, r, down_size, count, count_f, down_name
    try:
        resp = requests.get(url, proxies=proxies).text  # 获取网页文件
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
    if os.path.exists('.\\' + item):
        print(f'{item}已存在，跳过创建')
        pass
    else:
        for e in remove:
            item = item.replace(e, "")
        print(item)
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
        dot = down_name.find('.')
        down_name_gs = down_name[dot:]
        if os.path.exists(down_name) or ('psd' or 'PSD' or 'clip' or 'CLIP') in down_name_gs:
            print(f'文件{down_name}存在或为psd文件或为clip文件，已跳过')
            pass
        else:
            # 下载附件
            try:
                down_url_f = 'https://kemono.party/' + soup[i].get("href")
                r = requests.get(url=down_url_f, headers=ua(), timeout=6, stream=True, proxies=proxies)
                down_size = eval(r.headers['Content-Length'])
                count_f = 0
            except:
                print(f'下载{down_name}失败！')
            try:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                file_size = os.path.getsize(down_name)
                if file_size == down_size:
                    print(f"下载 {down_name} 文件完成！")
                else:
                    os.remove(down_name)
                    while file_size == down_size and count_f <= 5:
                        with open(down_name, 'wb') as f:
                            for chunk in r.iter_content(chunk_size=51200):
                                if chunk:
                                    f.write(chunk)
                        count_f += 1
                    if count_f == 6:
                        print('下载失败')
                    else:
                        print(f'下载{down_name}完成')
            except:
                print(f'写入文件{down_name}失败！')

    # 下载图片
    pic_count = 0  # 计数便于命名
    try:
        for item in bs.find_all('a', class_="fileThumb", href=re.compile('data')):  # 找到原画质图片位置
            pic_count += 1
            pic_soup = item.get('href')
            # 遍历下载图片
            where_Dot = str(pic_soup).rfind('.')
            down_name = str(pic_count) + str(pic_soup)[where_Dot:]  # 多图片按顺序命名
            for e in remove:
                down_name = down_name.replace(e, "")
            print(f"开始下载 {down_name} 文件..")  # 输出开始下载文件
            # 检查图片是否存在

            if os.path.exists(down_name):
                if os.path.getsize(down_name) != down_size_p:
                    print(f'图片文件{down_name}存在，已跳过')
                    continue
                else:
                    os.remove(down_name)
            # 下载图片文件
            down_url_p = 'https://kemono.party/' + str(pic_soup)
            try:
                r = requests.get(url=down_url_p, headers=ua(), timeout=6, proxies=proxies)
            except:
                print('请求失败！')
            try:
                with open(down_name, 'wb') as f:
                    f.write(r.content)
            except:
                print(f'文件{down_name}写入失败！')
            while os.path.getsize(down_name) == down_size_p:
                os.remove(down_name)
                r = requests.get(url=down_url_p, headers=ua(), timeout=6, proxies=proxies)
                with open(down_name, 'wb') as f:
                    f.write(r.content)
            else:
                print(f"下载图片 {down_name} 完成！")
        print(f'下载图片{down_name}任务完成')

        print('已回到上级目录')  # 回到上级目录
    except:
        print('下载该页面图片失败！')
    os.chdir('..//')


print('选择多画师下载模式需要在该程序目录下存在"task2.txt",且每行只有一个链接\n选择y进入多画师模式，选择n进入普通模式')
que = input('是否选择多画师下载模式（y/n）\n')
if que == 'y':

    file_path = 'task2.txt'
    down_path = input('请输入下载路径，需要是绝对路径：\n')
    with open(file_path, encoding='utf-8') as file_obj:
        while True:
            os.chdir(down_path)
            line = file_obj.readline()
            line = line.rstrip()
            if line == '':
                break
            print('开始下载该链接下的画师：' + line)
            url = line
            resp = requests.get(url, proxies=proxies).text
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
                href_list2 = []
                # 找到页面总数以及页面所有链接
                if ('fanbox/' or 'patron' or 'fantia' or 'gumroad') and 'user/' and 'o=' in str(
                        final_list[i]):  # 判断是否为页面链接
                    page += 1
                    url = 'https://kemono.party' + str(final_list[i])  # 指定链接
                    print('准备下载该页面下的单个页面所含文件：' + url)
                    # 分析单个页面
                    resp2 = requests.get(url, proxies=proxies).text
                    bs2 = BeautifulSoup(resp2, "lxml")
                    t12 = bs2.find_all('a')

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
                        if ('fanbox/' or 'patron' or 'fantia' or 'gumroad') and 'user/' and 'post/' in str(
                                href_list2[i]):  # 判断是否为含资源的页面
                            url = 'https://kemono.party' + str(href_list2[i])  # 设置url链接
                            print('开始下载：' + url)
                            down_url(url)  # 执行下载

            href_list2 = []
            if page == 0:
                for i in range(num):
                    if ('fanbox/' or 'patron' or 'fantia' or 'gumroad') and 'user/' and 'post/' in str(
                            final_list[i]):  # 判断是否为含资源的页面
                        href_list2.append(final_list[i])

                # 去除重复链接
                final_list2 = []
                for id in href_list2:
                    if id not in final_list2:
                        final_list2.append(id)
                num = len(final_list2)
                for i in range(num):
                    if ('fanbox/' or 'patron' or 'fantia' or 'gumroad') and 'user/' and 'post/' in str(
                            href_list2[i]):  # 判断是否为含资源的页面
                        url = 'https://kemono.party' + str(href_list2[i])  # 设置url链接
                        down_url(url)  # 执行下载
                        print('开始下载：' + url)
            os.chdir('..//')  # 回到上级目录
            print('已回到上级目录')
    print('所有下载任务完成')
    a = input('按任意键退出')
elif que == 'n':
    down_path = input('请输入下载路径，需要是绝对路径：\n')
    os.chdir(down_path)
    url = input('请输入下载链接：\n')
    resp = requests.get(url, proxies=proxies).text
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
        href_list2 = []
        # 找到页面总数以及页面所有链接
        if ('fanbox/' or 'patron' or 'fantia' or 'gumroad') and 'user/' and 'o=' in str(final_list[i]):  # 判断是否为页面链接
            page += 1
            url = 'https://kemono.party' + str(final_list[i])  # 指定链接
            print('准备下载该页面下的单个页面所含文件：' + url)
            # 分析单个页面
            resp2 = requests.get(url, proxies=proxies).text
            bs2 = BeautifulSoup(resp2, "lxml")
            t12 = bs2.find_all('a')

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
                if ('fanbox/' or 'patron' or 'fantia' or 'gumroad') and 'user/' and 'post/' in str(
                        href_list2[i]):  # 判断是否为含资源的页面
                    url = 'https://kemono.party' + str(href_list2[i])  # 设置url链接
                    down_url(url)  # 执行下载
                    print('开始下载：' + url)

    href_list2 = []
    if page == 0:
        for i in range(num):
            if ('fanbox/' or 'patron' or 'fantia' or 'gumroad') and 'user/' and 'post/' in str(
                    final_list[i]):  # 判断是否为含资源的页面
                href_list2.append(final_list[i])

        # 去除重复链接
        final_list2 = []
        for id in href_list2:
            if id not in final_list2:
                final_list2.append(id)
        num = len(final_list2)
        for i in range(num):
            if ('fanbox/' or 'patron' or 'fantia' or 'gumroad') and 'user/' and 'post/' in str(
                    href_list2[i]):  # 判断是否为含资源的页面
                url = 'https://kemono.party' + str(href_list2[i])  # 设置url链接
                down_url(url)  # 执行下载
                print('开始下载：' + url)
    print('所有下载任务完成')
    a = input('按任意键退出')
else:
    print('非法输入！\n程序已退出')
a = input('按任意键退出')
