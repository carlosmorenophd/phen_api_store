from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine("mysql+pymysql://userMysql:mysqlP@127.0.0.1:3306/CIMMYT_DATA?charset=utf8mb4")
meta = MetaData()

def create_entities():
    web_files = Table(
        'web_files', meta, 
        Column('id', Integer, primary_key = True), 
        Column('name', String(300)), 
    )
    meta.create_all(engine)