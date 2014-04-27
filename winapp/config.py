# -*- coding:utf-8 -*-
import logging
import logging.config

#配置文件
#装载logging.conf文件
logging.config.fileConfig('logging.conf')
# logger = logging.getLogger()		#rootlogger
logger = logging.getLogger('filelog')




#mysql
HOST = "localhost"
USER = "root"
PASSWD = ""
DBNAME = "mitiyu_dev"
PORT  = 3306