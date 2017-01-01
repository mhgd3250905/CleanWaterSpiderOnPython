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
    TSMCList = []

    # print(html)

    items = re.findall(r'{\"title\":\".+?}', html)

    print(len(items))
    for item in items:
        # print(item)
        titleRe = re.findall(r"\"title\":\"(.*?)\",", item)
        imgUrlRe = re.findall(r"\"imgUrl\":\"(.*?)\"", item)
        contentUrlRe = re.findall(r"\"url\":\"(.*?)\",", item)
        #获取到的内容需要进行unicode解码

        title=UnicodeUtils.unicodeToStr(titleRe[0])

        if imgUrlRe:
            imgUrl=UnicodeUtils.unicodeToStr(imgUrlRe[0])
        else:
            imgUrl=""

        contentUrl=UnicodeUtils.unicodeToStr(contentUrlRe[0])

        print(title)
        print(imgUrl)
        print(contentUrl)

            # 生成DataBean并加入到列表中
        TSMCBean = Bean.DataBean(title, contentUrl, imgUrl)
        TSMCList.append(TSMCBean)
        print('==================================================================')

    return TSMCList
