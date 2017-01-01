# -*- coding: utf-8 -*-

from Bmob import BmobUtils
from ContentSpider import ContentHtmlSpider
from HtmlUtils import HtmlGetUtils
from ListHtmlSpider import ItHomeHtmlDealUtils


class IT:

    #http://wap.ithome.com/ithome/getajaxdata.aspx?page=2&type=wapcategorypage
    def startSpider(self):
        '''
        针对IT之家的爬虫
        :return:
        '''
        #首先删除表
        # BmobUtils.deleteBmobClass("ITBean")

        # 爬虫正式开始
        for i in range(1, 11):
            url = 'http://www.ithome.com/ithome/getajaxdata.aspx?page=%d&type=indexpage' % (i)
            print(url)
            html = HtmlGetUtils.getHtml(url)
            # print(html)
            datalist = ItHomeHtmlDealUtils.dealHtml(html)
            # contentList=ContentHtmlSpider.getContentIndex(datalist,'WX')
            BmobUtils.insertListBmob('ITBean', datalist)
            # BmobUtils.insertContentBmob('ItContentBean',contentList)
            print("经过不懈的努力，开哥爬下了IT之家第 %d 页" % i)



