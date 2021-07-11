from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime


engine = create_engine('sqlite:///vizfin.db', echo=False)


class sql:
    

    def __init__(self,table):
        self._table = table;

    def create(self,df,desc):
        
        dir = pd.DataFrame()
        dir['table'] = [self._table]
        dir['desc'] =  [desc]
        dir.to_sql('directory',con=engine,if_exists='append',index_label="id")
        df.to_sql(self._table, con=engine, if_exists='fail',index_label='date')
        
        return engine.execute(f"SELECT * FROM {self._table}").fetchall()
    
    def empty(self):
        engine.execute(f"DELETE FROM {self._table}")

    def delete(self):
        engine.execute(f"DROP TABLE {self._table}")
    
    def update(self, data):
        df2 = data
        df2.to_sql(self._engine, con=engine, if_exists='append')
        return engine.execute(f"SELECT * FROM {target}").fetchall()
    
    def get(self, method):
        if method == 'sql':
            return engine.execute(f"SELECT * FROM {self._table}").fetchall()
        elif method == 'df':
            return pd.read_sql_query(f"SELECT * FROM {self._table}",con=engine)
