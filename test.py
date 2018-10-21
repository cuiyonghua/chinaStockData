import sys, os
import pandas as pd 
import numpy as np

sys.path.append(os.path.abspath('./'))
from tusharedb import TushareDB
from tusharedata import TushareData

db = TushareDB()
rows = db.do_query("SELECT * FROM tushare.all_stock_list")
# print(rows);

conn = db.getdbcon()

writeEngine = db.getWriteEngine()


tushareIns = TushareData()
allStockInfo = tushareIns.getBasicStockInfo()
print(allStockInfo)

# allStockInfo.to_sql(name='test', con=writeEngine, if_exists = 'append', index=False)
