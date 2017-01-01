# -*- coding: utf-8 -*-
class DataBean:
    def __init__(self,title,contentUrl,imgUrl):
        self.title=title
        self.contentUrl=contentUrl
        self.imgUrl=imgUrl

    def getTitle(self):
       return self.title

    def getContentUrl(self):
        return self.contentUrl

    def getImgUrl(self):
        return self.imgUrl