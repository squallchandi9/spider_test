# -*- coding:utf-8 -*-
import os
import urllib.parse
import requests
from bs4 import BeautifulSoup

path = '.\\'

remove = '},{'
remove2 = '"'


def printf(out):
    log_output = open('../log.txt', 'a+')
    print(out, file=log_output)
    print(out)
    log_output.close()


if os.path.exists('.\\outputs'):
    os.chdir('.\\outputs')
else:
    os.makedirs('.\\outputs')
    os.chdir('.\\outputs')

file_name = []
file_se = []


def search(name):
    dot = name.find('.')
    name1 = name[:dot]
    for root, dirs, files in os.walk(path):  # path 为根目录
        for i in files:
            if name1 in str(i):
                print('文件存在于' + str(i))
                return 1
        for i in dirs:
            if name1 in str(i):
                print('文件存在于' + str(i))
                return 1
        for i in root:
            if name1 in str(i):
                print('文件存在于' + str(i))
                return 1
        if name1 in dirs or name1 in files:  # 判断是否找到文件
            return 1
    return 0


def download1(down_name):
    # 下载附件
    global r, down_size, count_f
    try:

        down_url_f = 'https://shinnku.com/api/download/gal/krkr/' + str(down_name)
        print('正在尝试下载链接:' + down_url_f)
        r = requests.get(url=down_url_f, timeout=6, stream=True)
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
            if os.path.getsize(down_name) > 10000:
                print(f"下载 {down_name} 文件完成！")
            else:
                print('该下载链接有误，尝试其它链接')
        else:
            os.remove(down_name)
            while file_size == down_size and count_f <= 3:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                count_f += 1
            if count_f == 4:
                print('下载失败')
            else:
                print(f'下载{down_name}完成')
    except:
        print(f'写入文件{down_name}失败！')


def download2(down_name):
    # 下载附件
    global r, down_size, count_f
    try:

        down_url_f = 'https://shinnku.com/api/download/gal2/krkr/' + str(down_name)
        print('正在尝试下载链接:' + down_url_f)
        r = requests.get(url=down_url_f, timeout=6, stream=True)
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
            if os.path.getsize(down_name) > 10000:
                print(f"下载 {down_name} 文件完成！")
            else:
                print('该下载链接有误，尝试其它链接')
        else:
            os.remove(down_name)
            while file_size == down_size and count_f <= 3:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                count_f += 1
            if count_f == 4:
                print('下载失败')
            else:
                print(f'下载{down_name}完成')
    except:
        print(f'写入文件{down_name}失败！')


def download3(down_name):
    # 下载附件
    global r, down_size, count_f
    try:

        down_url_f = 'https://shinnku.com/api/download/mkw/krkr/' + str(down_name)
        print('正在尝试下载链接:' + down_url_f)
        r = requests.get(url=down_url_f, timeout=6, stream=True)
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
            if os.path.getsize(down_name) > 10000:
                print(f"下载 {down_name} 文件完成！")
            else:
                print('该下载链接有误，尝试其它链接')
        else:
            os.remove(down_name)
            while file_size == down_size and count_f <= 3:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                count_f += 1
            if count_f == 4:
                print('下载失败')
            else:
                print(f'下载{down_name}完成')
    except:
        print(f'写入文件{down_name}失败！')


def download4(down_name):
    # 下载附件
    global r, down_size, count_f
    try:

        down_url_f = 'https://shinnku.com/api/download/02/krkr/' + str(down_name)
        print('正在尝试下载链接:' + down_url_f)
        r = requests.get(url=down_url_f, timeout=6, stream=True)
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
            if os.path.getsize(down_name) > 10000:
                print(f"下载 {down_name} 文件完成！")
            else:
                print('该下载链接有误，尝试其它链接')
        else:
            os.remove(down_name)
            while file_size == down_size and count_f <= 3:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                count_f += 1
            if count_f == 4:
                print('下载失败')
            else:
                print(f'下载{down_name}完成')
    except:
        print(f'写入文件{down_name}失败！')


f = open("../txt.txt", "r", encoding='utf-8')  # 设置文件对象
txt = f.read()
f.close()  # 关闭文件
bs = BeautifulSoup(txt, "lxml")
bs = bs.string

# name = input('请输入您要查找的文件名：')
# answer = search(name)

for e in remove:
    txt = bs.replace(e, ",")

txt = txt.split(',')

for k in txt:
    for e in remove2:
        l = k.replace(e, "")
    if 'name' in l:
        if ('.7z' or '.zip' or '.rar') not in l:

            j = str(l)[5:]
            print(j)
            file_name.append(j)
print(len(file_name))
print(file_name)


'''
for k in txt:
    if 'name' in str(k):
        if ('.7z' or '.zip' or '.rar') not in k:
            j = str(k)[8:]
            j = j[:-1]
            file_name.append(j)
print(file_name)
'''
'''
for k in file_name:
    h=k
    if '.7z' not in k:
        k = k + '.7z'
        h = k
    if search(k):
        print('文件在子目录存在')
        continue
    else:
        download1(k)
        if os.path.getsize(k) < 10000:
            os.remove(k)
            download2(k)
            if os.path.getsize(k) < 10000:
                os.remove(k)
                download3(k)
                if os.path.getsize(k) < 10000:
                    os.remove(k)
                    download4(k)
                    # 判断是否存在分支
                    if os.path.getsize(k) < 10000:

                        print(f'文件{k}下载失败！')

                        os.remove(k)


'''

print('所有任务完成')
a = input('按任意键退出')
