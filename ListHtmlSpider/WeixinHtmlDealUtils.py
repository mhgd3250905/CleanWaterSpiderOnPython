# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from EveryBean import Bean
import re
# 返回DataBeanList
def dealHtml(html):
    '''
    处理html
    :param html:
    :return:返回Bilibili List
    '''
    WXList=[]
    items=re.findall(r'<li d(.*?)<\/li>',html)


    # soup=BeautifulSoup(html,'html.parser')
    # # print(soup)
    # items=soup.find_all('li')


    for item in items:
        # print(item)
        #获取标题
        title = re.findall(r'news_txt_box2\"><h3>(.*?)<\/h3><\/div>',item)[0]
        print(title)
        # 获取内容链接

        contentUrl=re.findall(r'id=\".+\" href=\"(.*?)\" class=\"news_lst_tab2',item)[0]
        print(contentUrl)
        #获取图片链接
        imgUrl=re.findall(r'news_lst_thumb2\"><img src=\"(.*?)\" width=',item)[0]
        print(imgUrl)

        # 生成DataBean并加入到列表中
        weixinBean=Bean.DataBean(title, contentUrl, imgUrl)
        WXList.append(weixinBean)

        print('==================================================================')


    return WXList