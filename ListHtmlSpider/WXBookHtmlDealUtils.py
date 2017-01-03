# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from EveryBean import Bean
import re
from CodeUtils import UnicodeUtils

# 返回DataBeanList
def dealHtml(html):
    '''
    处理微信检索中所有的内容 json样式中包含的xml
    :param url:
    :return: List<HXBean>
    '''
    dataList = []

    print(html)

    items = re.findall(r'\{\"fetchtime\".+?\"\}', html)

    print(len(items))

    for item in items:
        # print(item)
        titleRe = re.findall(r'\"title\"\:\"(.*?)\"\,', item)
        imgUrlRe = re.findall(r'\"imglink\"\:\"(.*?)\"\,', item)
        contentUrlRe = re.findall(r'url\":\"(.*?)\"\,', item)
        # #获取到的内容需要进行unicode解码
        #
        title=UnicodeUtils.unicodeToStr(titleRe[0])
        # print(title)

        if imgUrlRe:
            imgUrl=UnicodeUtils.unicodeToStr(imgUrlRe[0])
        else:
            imgUrl=""

        contentUrl=UnicodeUtils.unicodeToStr(contentUrlRe[0])

        print(title)
        print(imgUrl)
        print(contentUrl)

        # 生成DataBean并加入到列表中
        dataBean = Bean.DataBean(title, contentUrl, imgUrl)
        dataList.append(dataBean)
        print('==================================================================')

    return dataList
