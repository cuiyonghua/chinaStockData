import tushare as ts
from readconfig import ReadConfig

print(ts.__version__)

class TushareData:
    def __init__(self, *args, **kwargs):
        config = ReadConfig().getConfig()
        self._token = config['tushare']['token']
        ts.set_token(self._token)
        self.tusharePro = ts.pro_api()
    
    def getTushare(self):
        return self.tusharePro

    def getBasicStockInfo(self):
        allStockList = self.tusharePro.stock_basic(exchange_id='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        return allStockList

