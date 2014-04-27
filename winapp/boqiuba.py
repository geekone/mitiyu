# -*- coding:utf-8 -*-

import urllib2
import MySQLdb
import sys
import config
import time
from BeautifulSoup import BeautifulSoup

"""抓取播球吧的新闻列表 与 zuqiu168.py的差不多"""


#初始化mysql数据库，包括清理，新建
def initdb():
	conn = 	MySQLdb.connect(host=config.HOST,user=config.USER,passwd=config.PASSWD,db=config.DBNAME,charset="utf8")
	cur = conn.cursor()
	try:
		sql = "DROP TABLE IF EXISTS t_articles_tmp"   #清除旧的联赛表，并新建
		cur.execute(sql)
		sql = """CREATE TABLE IF NOT EXISTS articles_tmp (
		    id integer NOT NULL AUTO_INCREMENT,
		    title varchar(255) NOT NULL,
		    url varchar(255) NOT NULL,
		    content text DEFAULT NULL,
		    created integer DEFAULT NULL,
		    pubdate varchar(45),
		    fromto varchar(45) NOT NULL,PRIMARY KEY(id)
		);"""
		cur.execute(sql)
	except Exception,e:
		config.logger.error(e)
		sys.exit(1)
	finally:
		cur.close()
		conn.close()


#抓取列表，返回列表
def read_list_page(url_addr):
	list_data = []
	try:
		req = urllib2.Request(url_addr)
		req.add_header("User-Agent","eric")
		res = urllib2.urlopen(req,timeout=30)
		html = res.read()
		soup = BeautifulSoup(html)
		div = soup.find("div",{"class":"endpage artlist"})
		li_list = div.findAll("li")		#发现所有的li
		if len(li_list) == 0:	#如果列表为0，直接返回空的list
			return list_data
		else:
			for li in li_list:
				a = li.find("a")
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
			if cur.fetchone() == None:
				title = data['title']
				url = data['url']
				fromto = "boqiuba"
				sql = "INSERT INTO t_articles_tmp(title,url,fromto)  VALUES ('%s','%s','%s')" %(title,url,fromto)
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
		sql = "SELECT * FROM  t_articles_tmp where fromto = 'boqiuba'"
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
		url_addr = "http://www.boqiuba.com" + _url
		req = urllib2.Request(url_addr)
		req.add_header("User-Agent","eric")
		res = urllib2.urlopen(req,timeout=30)
		html = res.read()
		soup = BeautifulSoup(html.decode("gbk").encode("utf-8"))
		div = soup.find("div",{"class":"auor"})
		_created_arr  =  div.text.split(u" ")
		_pubdate =  str(_created_arr[0])
		div = soup.find("div",{"id":"endtext1"})
		_content = div.prettify()
		_content = str(_content).replace("'","’")
		_created = time.time()
		#更新数据
		conn = MySQLdb.connect(host=config.HOST,user=config.USER,passwd=config.PASSWD,db=config.DBNAME,charset="utf8")
		cur = conn.cursor()
		sql = "UPDATE t_articles_tmp SET content = '%s',pubdate = '%s',created = '%d' WHERE id= '%d'" %(_content,_pubdate,_created,_id)
		cur.execute(sql)
		conn.commit()
	except Exception,e:
		print e
		# config.logger.error(e)
		sys.exit(1)
	finally:
		cur.close()
		conn.close()





def do_main():
	# initdb() #初始数据库
	url_addr = "http://www.boqiuba.com/zuqiu/"
	listdata = read_list_page(url_addr)
	insert_listdata(listdata)
	listdata = get_list_fromdb()
	for data in listdata:
		update_content(data)
		print data[0]
		time.sleep(2)



if __name__ == "__main__":
	do_main()
	#测试抓取列表
	# url_addr = "http://www.boqiuba.com/zuqiu/"
	# listdata = read_list_page(url_addr)
	# insert_listdata(listdata)

	#测试读取数据库取出新闻列表　url
	# listdata = get_list_fromdb()
	# for data in listdata:
		# print data[0] ,data[1]

	#测试更新新闻详细内容
	# listdata = get_list_fromdb()
	# for data in listdata:
	# 	update_content(data)
	# 	print data[0]
	# 	time.sleep(2)
		

