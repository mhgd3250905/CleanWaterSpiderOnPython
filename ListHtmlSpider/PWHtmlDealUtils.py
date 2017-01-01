# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from EveryBean import Bean
import re
from CodeUtils import UnicodeUtils

# 返回DataBeanList
def dealFirstHtml(html):
    '''
    处理html
    :param html:
    :return:返回Bilibili List
    '''
    PWList=[]

    soup=BeautifulSoup(html,'html.parser')
    # print(soup)
    items=soup.findAll('section','section-post')
    # print(items)

    for item in items:
        print(type(item))
        #获取标题
        titleRe=item.find('div','news-item')
        if titleRe:
            title=titleRe.find('h2','title').text
            print(title)

        # 获取内容链接
        contentRe=item.find('div','news-item')
        if contentRe:
            contentUrl=contentRe.find('h2','title').find('a')['href']
            print(contentUrl)

        #获取图片链接
        imgRe=item.find('div','news-thumb')
        if imgRe:
            imgStr=imgRe['style']
            imgUrl=re.findall(r'background-image: url\((.*?)\);',imgStr)[0]
            print(imgUrl)

        # 生成DataBean并加入到列表中
        weixinBean=Bean.DataBean(title, contentUrl, imgUrl)
        PWList.append(weixinBean)
        print('==================================================================')
    return PWList

def dealSecondHtml(html):
    '''
    处理虎嗅网第二部分的内容
    :param url:
    :return: List<HXBean>
    '''
    PWList = []

    # print(html)

    items = re.findall(r"\{\"id\".+?\}", html)
    print(len(items))
    for item in items:
        # print(item)
        title = re.findall(r"\"title\":\"(.*?)\",", item)
        imgUrl = re.findall(r"\"img\":\"(.*?)\",", item)
        contentUrl = re.findall(r"\"link\":\"(.*?)\",", item)
        #获取到的内容需要进行unicode解码
        print(UnicodeUtils.unicodeToStr(title[0]))
        print(UnicodeUtils.unicodeToStr(imgUrl[0]))
        print(UnicodeUtils.unicodeToStr(contentUrl[0]))

        # 生成DataBean并加入到列表中
        PWBean = Bean.DataBean(title, contentUrl, imgUrl)
        PWList.append(PWBean)
        print('==================================================================')

    return PWList
