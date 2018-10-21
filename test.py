import sys, os
import pandas as pd 
import numpy as np
import datetime

currentDT = datetime.datetime.now()

currectDate = currentDT.strftime("%Y%m%d")
print(currectDate)


sys.path.append(os.path.abspath('./'))
from tusharedb import TushareDB
from tusharedata import TushareData
from readconfig import ReadConfig

config = ReadConfig().getConfig()
token = config['tushare']['token']


db = TushareDB()
rows = db.do_query("SELECT * FROM tushare.all_stock_list")
# print(rows);

conn = db.getdbcon()

writeEngine = db.getWriteEngine()


tushareIns = TushareData()
allStockInfo = tushareIns.getBasicStockInfo()
print(allStockInfo)

# allStockInfo.to_sql(name='test', con=writeEngine, if_exists = 'append', index=False)
for ts_code in allStockInfo['ts_code']:
    eachStock_qfq = tushareIns.getStockDetailInfo(ts_code, currectDate, currectDate)
    eachStock_qfq.to_sql(name='stock_info_qfq', con=writeEngine, if_exists = 'append', index=False)
    print(eachStock_qfq)
