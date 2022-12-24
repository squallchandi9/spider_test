# -*- coding:utf-8 -*-
import os
import urllib.parse
import requests
from bs4 import BeautifulSoup

path = '.\\'

remove = '},{'
remove2 = '"'

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
    log_output = open('../log.txt', 'a+', encoding='utf-8')
    print(out, file=log_output)
    print(out)
    log_output.close()


if os.path.exists('.\\outputs'):
    os.chdir('.\\outputs')
else:
    os.makedirs('.\\outputs')
    os.chdir('.\\outputs')

file_name = ['120日元.zip', '3days.zip', '40日40夜之雨.zip', 'AIR.zip', 'AIR-v2.5.zip', 'cafe_liitle_wish.zip',
             'clannad.zip', 'D.C.P.C.zip', 'eden[伊甸园].zip', 'eden‛＊.zip', 'ef - the first tale.zip',
             'ef - the latter tale.zip', 'Ever17.zip', 'ever17[时空轮回].zip', 'fate stay night.zip',
             'freefriends2.zip', 'Gift～ギフト～.zip', 'G弦上的魔王.zip', 'loli痴女.zip', 'LOLI的时间.zip',
             'lovely quest.zip', 'NOeSIS 虚假的记忆物语.zip', 'Petit Fleur~拂过小镇的旋律之风~.zip', 'Rewrite hf!.zip',
             'Rewrite.zip', 'Scarlett日常的境界线.zip', 'sweet pool.zip', 'The World of Rapest_for_Android.zip',
             'Tiny Dungeon1 魔族篇.zip', 'Tiny Dungeon2 龙族篇.zip', 'Tiny Dungeon3 神族篇.zip',
             'Tiny Dungeon4 完结篇.zip', 'Wind -a breath of heart.zip', '一生一次的机会.zip', '万有引力少女.zip',
             '不存在的圣诞节.zip', '东月西阳.zip', '公主假日.zip', '公主恋人.zip', '初音岛1.zip', '初音岛2.zip',
             '刻痕.zip', '勇者大战魔物娘.zip', '勇者大战魔物娘3章整合汉化[Ons]1.02版.zip', '和怪物谈恋爱吧!.zip',
             '和爱丽丝酱同棲!.zip', '堕天使 前編 銀髪の少女と世界の異変.zip', '堕天使 後編 漆黒い翼を白濁に染めて.zip',
             '夕阳染红的坡道.zip', '夜明前的琉璃色.zip', '天使の日曜日.zip', '天使的工作.zip', '失意之棒-いらいら欲棒.zip',
             '女仆咖啡帕露菲.zip', '女装学园.zip', '女装山脉.zip', '女装海峡.zip', '妹妹与保健体育.zip',
             '妹妹大作战.zip', '妹调教日记.zip', '妹调教日记FD.zip', '孤独少女的百合物语.zip',
             '学校发生过的恐怖故事.zip', '实妹.zip', '实妹相伴的大泉君.zip', '寒蝉鸣泣之时.zip', '寒蝉鸣泣之时礼.zip',
             '将全部的歌献给未来的你.zip', '少女爱上姐姐.zip', '尘骸魔京.zip', '巡音露卡的事件簿1.zip',
             '巡音露卡的事件簿2.zip', '幼性反应.zip', '幼驯染成了大总统.zip', '恋爱0公里.zip', '恋爱少女与守护之盾.zip',
             '恋爱蜡笔.zip', '悠久之翼FD天使的日曜日.zip', '悠久之翼上篇.zip', '悠久之翼下篇.zip', '悠之空.zip',
             '意识流.zip', '', '我和傲娇妹妹的故事XD.zip', '我所希冀的未来.zip', '时间停止.zip', '星之梦.zip',
             '智代after.zip', '暗黑女王外传.zip', '暗黑女王本传.zip', '月姬PLUS-DISC.zip', '未来的歌献给未来的你.zip',
             '朱-Aka-.zip', '架向星空之桥.zip', '染紅的街道.zip', '柚子美夏.zip', '桃色恋恋.zip', '梦见之药.zip',
             '樱舞少女的轮舞曲 ~女装主角们的受难日~.zip', '樱舞少女的轮舞曲的轮舞曲本篇共通线.zip', '歌月十夜.zip',
             '死埋葬1.7z', '死埋葬2.7z', '死埋葬3.7z', '死神之吻乃离别之味.zip', '水仙1+2.zip', '水色.zip',
             '永不消失的彩虹.zip', '永不落幕的前奏诗.zip', '注视着你瞳里的未来的歌谣.zip', '海猫鸣泣之时 羽.zip',
             '海猫鸣泣之时 翼.zip', '海猫鸣泣之时[出题篇] ep1-4.zip', '海猫鸣泣之时[解题篇] 散 ep5-8.zip', '游海传.zip',
             '灯穗奇谭.zip', '盛夏之梦.zip', '秋之回忆2.zip', '秋之回忆3.zip', '秋之回忆4.zip', '秘密游戏杀手皇后.zip',
             '秽翼的尤斯蒂娅.zip', '突然之间发现我已恋上你.zip', '精爆双姬.zip', '糖糖危机-莉菠炭的侍奉编.zip',
             '纯白交响曲（全年龄）.zip', '绿坝娘的河月蟹日.zip', '缘之空.zip', '缸底.zip', '美少女万华镜2.5.zip',
             '美少女万华镜2.zip', '美少女万华镜3.zip', '美少女万华镜4罪与罚的少女v1.0.zip', '美少女万华镜5v3.0.zip',
             '美少女万花镜1.zip', '色亡.zip', '花与少女的祝福.zip', '花与少女的祝福FD皇家花束.zip', '花归葬.zip',
             '苍蓝眼瞳的人偶.zip', '虫之岛.zip', '触装天使serika.zip', '诉说谎言的记忆.zip', '诚哥的逆袭.zip',
             '该死的妹子.zip', '超级糖果.zip', '车轮之国 向日葵少女.zip', '车轮之国FD悠久的少年少女.zip',
             '这里是幻想郷!.zip', '遥仰凰华.zip', '铃音之歌 初音之声.zip', '银色.zip', '间接之恋.zip',
             '青空下的约定.zip', '青鸟的虚像.zip', '风-心灵之息.zip', '鬼哭街.zip', '魔王大人的求婚.zip',
             '魔界公主艾奇德娜.zip', '麻衣的诱惑.zip', '黑色星期天-Sombre Dimanche-.zip']


def search(name):
    dot = name.find('.')
    name1 = name[:dot]
    for root, dirs, files in os.walk('..//'):  # path 为根目录
        for i in files:
            if name1 in str(i):
                return 1
        for i in dirs:
            if name1 in str(i):
                return 1
        for i in root:
            if name1 in str(i):
                return 1

    return 0


def download1(down_name):
    # 下载附件
    global r, down_size, count_f
    try:

        down_url_f = 'https://shinnku.com/api/download/gal/ons/' + str(down_name)
        printf('正在尝试下载链接:' + down_url_f)
        r = requests.get(url=down_url_f, headers=ua(), timeout=6, stream=True, proxies=proxies)
        down_size = eval(r.headers['Content-Length'])
        count_f = 0
    except:
        printf(f'下载{down_name}失败！')
    try:
        with open(down_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=51200):
                if chunk:
                    f.write(chunk)
        file_size = os.path.getsize(down_name)
        if file_size == down_size:
            if os.path.getsize(down_name) > 10000:
                printf(f"下载 {down_name} 文件完成！")
            else:
                printf('该下载链接有误，尝试其它链接')
        else:
            os.remove(down_name)
            while file_size == down_size and count_f <= 3:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                count_f += 1
            if count_f == 4:
                printf('下载失败')
            else:
                printf(f'下载{down_name}完成')
    except:
        printf(f'写入文件{down_name}失败！')


def download2(down_name):
    # 下载附件
    global r, down_size, count_f
    try:

        down_url_f = 'https://shinnku.com/api/download/gal2/ons/' + str(down_name)
        printf('正在尝试下载链接:' + down_url_f)
        r = requests.get(url=down_url_f, headers=ua(), timeout=6, stream=True, proxies=proxies)
        down_size = eval(r.headers['Content-Length'])
        count_f = 0
    except:
        printf(f'下载{down_name}失败！')
    try:
        with open(down_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=51200):
                if chunk:
                    f.write(chunk)
        file_size = os.path.getsize(down_name)
        if file_size == down_size:
            if os.path.getsize(down_name) > 10000:
                printf(f"下载 {down_name} 文件完成！")
            else:
                printf('该下载链接有误，尝试其它链接')
        else:
            os.remove(down_name)
            while file_size == down_size and count_f <= 3:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                count_f += 1
            if count_f == 4:
                printf('下载失败')
            else:
                printf(f'下载{down_name}完成')
    except:
        printf(f'写入文件{down_name}失败！')


def download3(down_name):
    # 下载附件
    global r, down_size, count_f
    try:

        down_url_f = 'https://shinnku.com/api/download/mkw/ons/' + str(down_name)
        printf('正在尝试下载链接:' + down_url_f)
        r = requests.get(url=down_url_f, headers=ua(), timeout=6, stream=True, proxies=proxies)
        down_size = eval(r.headers['Content-Length'])
        count_f = 0
    except:
        printf(f'下载{down_name}失败！')
    try:
        with open(down_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=51200):
                if chunk:
                    f.write(chunk)
        file_size = os.path.getsize(down_name)
        if file_size == down_size:
            if os.path.getsize(down_name) > 10000:
                printf(f"下载 {down_name} 文件完成！")
            else:
                printf('该下载链接有误，尝试其它链接')
        else:
            os.remove(down_name)
            while file_size == down_size and count_f <= 3:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                count_f += 1
            if count_f == 4:
                printf('下载失败')
            else:
                printf(f'下载{down_name}完成')
    except:
        printf(f'写入文件{down_name}失败！')


def download4(down_name):
    # 下载附件
    global r, down_size, count_f
    try:

        down_url_f = 'https://shinnku.com/api/download/02/ons/' + str(down_name)
        printf('正在尝试下载链接:' + down_url_f)
        r = requests.get(url=down_url_f, headers=ua(), timeout=6, stream=True, proxies=proxies)
        down_size = eval(r.headers['Content-Length'])
        count_f = 0
    except:
        printf(f'下载{down_name}失败！')
    try:
        with open(down_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=51200):
                if chunk:
                    f.write(chunk)
        file_size = os.path.getsize(down_name)
        if file_size == down_size:
            if os.path.getsize(down_name) > 10000:
                printf(f"下载 {down_name} 文件完成！")
            else:
                printf('该下载链接有误，尝试其它链接')
        else:
            os.remove(down_name)
            while file_size == down_size and count_f <= 3:
                with open(down_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=51200):
                        if chunk:
                            f.write(chunk)
                count_f += 1
            if count_f == 4:
                printf('下载失败')
            else:
                printf(f'下载{down_name}完成')
    except:
        printf(f'写入文件{down_name}失败！')


for k in file_name:

    if search(k):
        printf(f'文件{k}在子目录存在')
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
                        printf(f'文件{k}下载失败！')

                        os.remove(k)

printf('所有任务完成')
a = input('按任意键退出')
