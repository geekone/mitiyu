# -*- coding:utf-8 -*-

import urllib2
import MySQLdb
import sys
import config
import time
from BeautifulSoup import BeautifulSoup


"""抓取8bo首页的新闻列表"""

#抓取列表，返回列表
def read_list_page(url_addr):
	list_data = []
	try:
		req = urllib2.Request(url_addr)
		req.add_header("User-Agent","eric")
		res = urllib2.urlopen(req,timeout=30)
		html = res.read()
		soup = BeautifulSoup(html)
		dd_list = soup.findAll("dd",{"class":"bnews bbox"})
		for dd in dd_list:
			div_list = dd.findAll("div",{"class":"link"})
			for div in div_list:
				a = div.find("a",{"class":"txt"})
				_title = a.text
				_url = a.get("href")
				data = {'title':_title,'url':_url}
				list_data.append(data)
	except Exception,e:
		config.logger.error(e)
		sys.exit(1)
	return list_data


def insert_listdata(listdata):
	conn = MySQLdb.connect(host=config.HOST,user=config.USER,passwd=config.PASSWD,db=config.DBNAME,charset="utf8")
	cur = conn.cursor()
	try:
		for data in listdata:
			sql = "SELECT * FROM t_articles_tmp where url = '%s'"%(data['url'])
			cur.execute(sql)
			if cur.fetchone() == None:	#判断是否有重复
				title = data['title']
				url = data['url']
				fromto = '8bo'
				sql = "INSERT INTO t_articles_tmp(title,url,fromto) VALUES ('%s','%s','%s')" %(title,url,fromto)
				cur.execute(sql)
		conn.commit()
	except Exception,e:
		config.logger.error(e)
		sys.exit(1)
	finally:
		cur.close()
		conn.close()


#从数据库取出要抓取详细内容的列表
def get_list_fromdb():
	list_data = []
	conn = MySQLdb.connect(host=config.HOST,user=config.USER,passwd=config.PASSWD,db=config.DBNAME,charset="utf8")
	cur = conn.cursor()
	try:
		sql = "SELECT * FROM  t_articles_tmp where fromto = '8bo'"
		cur.execute(sql)
		list_data = cur.fetchall()
	except Exception,e:
		config.logger.error(e)
		sys.exit(1)
	finally:
		cur.close()
		conn.close()
	return list_data


#抓取详细内容并更新数据库	data 是数据库的row 一行数据 data[0]编号 data[1] title  data[2] url
def update_content(data):
	try:
		_id = data[0]
		_url = data[2]
		url_addr = "http://www.8bo.com/" + _url
		req = urllib2.Request(url_addr)
		req.add_header("User-Agent","eric")
		res = urllib2.urlopen(req,timeout=30)
		html = res.read()
		soup = BeautifulSoup(html)
		div = soup.find("div",{"class":"t_fsz"})
		# _created_arr  =  div.text.split(u" ")
		# _pubdate =  str(_created_arr[0])
		# div = soup.find("div",{"id":"endtext1"})
		_content = div.prettify()
		_content = str(_content).replace("'","’")
		_created = time.time()
		#更新数据
		conn = MySQLdb.connect(host=config.HOST,user=config.USER,passwd=config.PASSWD,db=config.DBNAME,charset="utf8")
		cur = conn.cursor()
		sql = "UPDATE t_articles_tmp SET content = '%s',created = '%d' WHERE id= '%d'" %(_content,_created,_id)
		cur.execute(sql)
		conn.commit()
	except Exception,e:
		print e
		# config.logger.error(e)
		sys.exit(1)
	finally:
		cur.close()
		conn.close()



if __name__ == "__main__":
	#测试 抓取列表
	url_addr = "http://www.8bo.com/"
	listdata = read_list_page(url_addr)
	insert_listdata(listdata)
	listdata = get_list_fromdb()
	for data in listdata:
		update_content(data)
		print data[0]
		time.sleep(2)