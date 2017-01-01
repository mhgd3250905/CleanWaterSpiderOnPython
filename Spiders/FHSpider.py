# -*- coding: utf-8 -*-

from Bmob import BmobUtils
from ContentSpider import ContentHtmlSpider
from HtmlUtils import HtmlGetUtils
from ListHtmlSpider import FHHtmlDealUtils
import re
import time


class FH:

    #http://itech.ifeng.com/7_1/data.shtml?_=1481811245339
    def startSpider(self):
        '''
        针对凤凰网科技频道的爬虫
        :return:
        '''
        #首先删除表
        # BmobUtils.deleteBmobClass("FHBean")


        # 爬虫正式开始
        for i in range(0, 10):
            myTime='%d' % (time.time()*1000)

            url = 'http://itech.ifeng.com/7_%d/data.shtml?_=%s' % (i,myTime)
            # print(url)
            #返回内容：getListDatacallback(...)
            #所以需要处理一下
            html = HtmlGetUtils.getHtml(url)
            datalist = FHHtmlDealUtils.dealHtml(html)
            BmobUtils.insertListBmob('FHBean', datalist)
            print("经过不懈的努力，开哥爬下了IT之家第 %d 页" % i)



