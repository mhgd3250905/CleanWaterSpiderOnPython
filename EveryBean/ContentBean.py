# -*- coding: utf-8 -*-
class ContentBean:
    def __init__(self,contentUrl,contentHtml):
        self.contentUrl=contentUrl
        self.contentHtml=contentHtml

    def getContentUrl(self):
        return self.contentUrl

    def getContentHtml(self):
        return self.contentHtml