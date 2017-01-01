# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from EveryBean import Bean
import re
from CodeUtils import UnicodeUtils

# 返回DataBeanList
def dealHtml(html):
    '''
    处理虎嗅网第二部分的内容
    :param url:
    :return: List<HXBean>
    '''
    GGList = []

    # print(html)

    items = re.findall(r'{\"Id\":.+?}', html)

    print(len(items))
    for item in items:
        # print(item)
        title = re.findall(r"\"Title\":\"(.*?)\",", item)
        imgUrl = re.findall(r"\"Portrait\":\"(.*?)\",", item)
        reUrl = re.findall(r"\"Reurl\":\"(.*?)\",", item)
        if reUrl and title and imgUrl:
            contentUrl='http://www.svinsight.com/app/reading/%s.html' % reUrl[0]
        #获取到的内容需要进行unicode解码

            print(title[0])
            print(imgUrl[0])
            print(contentUrl)

            # 生成DataBean并加入到列表中
            GGBean = Bean.DataBean(title[0], contentUrl, imgUrl[0])
            GGList.append(GGBean)
            print('==================================================================')

    return GGList
