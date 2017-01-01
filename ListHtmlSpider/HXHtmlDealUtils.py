# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from EveryBean import Bean
# 返回DataBeanList
def dealFirstHtml(html):
    '''
    处理html
    :param html:
    :return:返回Bilibili List
    '''
    HXList=[]

    soup=BeautifulSoup(html,'html.parser')
    # print(soup)
    itemUl=soup.find('ul','article-append-box')
    items=itemUl.findAll('li')
    # print(items)

    for item in items:
        #获取标题
        title =item.find('div','article-md-title').text
        print(title)

        print(item)
        # 获取内容链接
        if len(item.findAll('a'))==1:
            firstUrl = 'https://m.huxiu.com/' + item.findAll('a')[0]['href']
        else:
            firstUrl='https://m.huxiu.com/'+item.findAll('a')[1]['href']

        print(firstUrl)

        #获取图片链接
        imgUrl=item.find('img','lazy')['data-original']
        print(imgUrl)

        # 生成DataBean并加入到列表中
        weixinBean=Bean.DataBean(title, firstUrl, imgUrl)
        HXList.append(weixinBean)
        print('==================================================================')
    return HXList

def dealSecondHtml(html):
    '''
    处理虎嗅网第二部分的内容
    :param url:
    :return: List<HXBean>
    '''
    HXList = []

    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    items = soup.findAll('li')
    # print(items)

    for item in items:
        # 获取标题
        title = item.find('div', 'article-md-title').text
        print(title)

        # 获取内容链接
        firstUrl = 'https://m.huxiu.com/' + item.findAll('a')[1]['href']
        print(firstUrl)

        # 获取图片链接
        imgUrl = item.find('img', 'lazy')['data-original']
        print(imgUrl)

        # 生成DataBean并加入到列表中
        weixinBean = Bean.DataBean(title, firstUrl, imgUrl)
        HXList.append(weixinBean)
        print('==================================================================')
    return HXList
