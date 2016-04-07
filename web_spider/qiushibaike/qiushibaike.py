__author__ = 'aaronzark'
# -*- coding:utf-8 -*-
#糗事百科抓取

import re
import urllib
import urllib2

class QSBK:
	def  __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
		self.headers = {'User-Agent': self.user_agent}
		self.url = 'http://www.qiushibaike.com/hot/page/'

	def getOnePage(self, pageIndex):
		try:
			request = urllib2.Request(self.url+str(pageIndex), headers = self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode
		except urllib2.URLError, e:
			if e.hasatrr(e, 'reason'):
				print u"连接糗事百科失败，错误原因", e.reason
				return pageCode

	def analyseOnePage(self, pageIndex):
		pageCode = self.getOnePage(pageIndex)
		if not pageCode:
			print u'页面加载失败'
			return None
		pattern = re.compile(r'<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)<!--.*?-->.*?</div>.*?<div.*?class="number">(.*?)</i>.*?class="number">(.*?)</i>', re.S)
		qiushi_info = re.findall(pattern, pageCode)
		for qiushi in qiushi_info:
			print 
			print u'发帖人：', qiushi[0], qiushi[1].replace('<br/>', '')
			print qiushi[2], u'好笑', qiushi[3], u'评论'
			print
			print '---------------------------------------------'

	def start(self):
		for i in range(3): 
			print '-------------欢迎进入糗事百科-------------'
		print '----------------------------------第1页----------------------------------'
		print '----------------------------------第1页----------------------------------'
		while True:
			self.analyseOnePage(self.pageIndex)
			order = raw_input('是否进入下一页？ y or n:') 
			if order == 'y':
				self.pageIndex += 1
				print '----------------------------------' + u'第' + str(self.pageIndex) + u'页' + '----------------------------------'
				print '----------------------------------' + u'第' + str(self.pageIndex) + u'页' + '----------------------------------'
			else:
				break

spider = QSBK()
spider.start()