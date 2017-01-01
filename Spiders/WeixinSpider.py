# -*- coding: utf-8 -*-


from Bmob import BmobUtils
from ContentSpider import ContentHtmlSpider
from HtmlUtils import HtmlGetUtils
from ListHtmlSpider import WeixinHtmlDealUtils


#http://weixin.sogou.com/wapindex/wap/0612/wap_9/0.html

class WX:

    def startSpider(self):
        '''
        微信资讯爬虫统筹地
        :return:
        '''
        #清空一下数据表
        # BmobUtils.deleteBmobClass('WeixinBean')

        headers={
            'Accept':'*/*',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'X-Requested-With':'XMLHttpRequest'
        }

        #开始爬
        for i in range(1,11):
            #&lastDate=2016/12/12 0:03:00
            url='http://weixin.sogou.com/wapindex/wap/0612/wap_9/%d.html' % i
            html= HtmlGetUtils.getHtml(url, headers=headers)
            print(html)
            datalist= WeixinHtmlDealUtils.dealHtml(html)
            # contentList=ContentHtmlSpider.getContentIndex(datalist,'WX')
            BmobUtils.insertListBmob('WeixinBean', datalist)
            # BmobUtils.insertContentBmob('WeixinContentBean',contentList)
            print("经过不懈的努力，开哥爬下了微信订阅号第 %d 页" % i)

