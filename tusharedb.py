from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
import logging
import records
from readconfig import ReadConfig


class TushareDB:
    '''
    '''
    def __init__(self, *args, **kwargs):
        config = ReadConfig().getConfig()
        self._dburl = "mysql+pymysql://"+config['mysql']['user']+":"+config['mysql']['passwd']+"@"+config['mysql']['host']+":3306/"+config['mysql']['db']+"?charset=utf8mb4"
        self._conn = records.Database(self._dburl)
        self._writeEngine = create_engine(self._dburl,echo=True)

    def getdbcon(self):
        return self._conn

    def getWriteEngine(self):
        return self._writeEngine
    
    def do_query(self, sql):
        '''
            Query the DataWarehouse with SQL command
        '''
        connect = self.getdbcon()
        # if self.debug:
        #     LOG.debug(sql)
        rows = connect.query(sql)
        return rows.export('df')


