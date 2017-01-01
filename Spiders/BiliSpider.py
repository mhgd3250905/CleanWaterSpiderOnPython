# -*- coding: utf-8 -*-
import datetime
import time

from Bmob import BmobUtils
from HtmlUtils import HtmlGetUtils
from ListHtmlSpider import BiliHtmlDealUtils


class BL:

    def startSpider(self):
        '''
        对哔哩哔哩进行爬虫程序，这里大概是一个统筹地
        :return:
        '''

        #获取url中需要的日期参数
        date1=time.strftime("%Y-%m-%d", time.localtime())
        date2=(datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")

        #首先删除表
        # BmobUtils.deleteBmobClass("BiliBean")


       #爬虫正式开始
        for i in range(1,11):
            url='http://www.bilibili.com/mobile/list/default-95-%d-%s~%s.html' % (i,date2,date1)
            print(url)
            html= HtmlGetUtils.getHtml(url)
            datalist= BiliHtmlDealUtils.dealHtml(html)
            BmobUtils.insertListBmob('BiliBean', datalist)
            print("经过不懈的努力，开哥爬下了哔哩哔哩第 %d 页" % i)