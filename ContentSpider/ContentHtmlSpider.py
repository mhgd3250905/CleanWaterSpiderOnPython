# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from EveryBean import ContentBean
from HtmlUtils import HtmlGetUtils


def getContentIndex(list,type):
    '''
    把处理好的contentBean加入到List中进行返回
    :param list:
    :return:contentList
    '''

    contentBeanList=[]
    for item in list:
        contentUrl=item.getContentUrl()
        # print(contentUrl)
        contentHtml=''
        if type=='WX':
            #WX 方式采用的是真个HTML获取
            contentHtml=getWeixinContent(contentUrl)
        elif type=='Paopao':
            #Paopao网专用方式
            contentHtml=getPaopaoContent(contentUrl)

        # print(contentHtml)
        contentBean=ContentBean.ContentBean(contentUrl,contentHtml)
        contentBeanList.append(contentBean)

    return contentBeanList


def getPaopaoContent(url):
    '''
    访问目的网页然后去广告之后返回过来
    :param url:
    :return: 处理之后的html文本
    '''

    contentHtml=''
    content= HtmlGetUtils.getHtml(url)
    # print(content)
    soup = BeautifulSoup(content, 'html.parser')

    head=soup.find('head').prettify()
    # print(head)

    #网页不存在然后报错~
    print(url)
    # print(soup.find('div', 'title3').prettify())
    if soup.find('div', 'title3')!=None:
        divTitle=soup.find('div', 'title3').prettify()


        divMain=soup.find('div', 'main').prettify()
        # print(divMain)
        # divBottom=soup.find('div', 'tit').prettify()

        contentHtml='<!DOCTYPE HTML><html>'+\
                    head+\
                    '<body>'+\
                    divTitle+\
                    divMain+\
                    '</body></html>'

        # print(contentHtml)
    return contentHtml

def getWeixinContent(url):
    '''
    爬取微信文章内容
    :param url:
    :return:
    '''
    content= HtmlGetUtils.getHtml(url)
    return content

# def getITContent(url):
#     '''
#
#     :param url:
#     :return:contentHtml
#     '''
#     content= HtmlGetUtils.getHtml(url)
#
#     return content