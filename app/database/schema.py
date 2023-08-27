from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float
engine = create_engine("mysql+pymysql://userMysql:mysqlP@127.0.0.1:3306/CIMMYT_DATA?charset=utf8mb4")
meta = MetaData()

def create_entities():
    Table(
        'web_files', meta, 
        Column('id', Integer, primary_key = True), 
        Column('name', String(300)), 
    )
    Table(
        'trait', meta, 
        Column('id', Integer, primary_key= True),
        Column('name', String(300)), 
        Column('description', String(500)), 
        Column('co_trait_name', String(200)), 
        Column('variable_name', String(200)), 
        Column('co_id', String(400)), 
    )
    # Find this file and load
    Table(
        'genotype', meta, 
        Column('id', Integer, primary_key = True), 
        Column('c_id', Integer), 
        Column('s_id', Integer), 
        Column('cross_name', String(600)), 
        Column('history', String(600)), 
    )
    # Find this file and load
    Table(
        'location', meta,
        Column('id', Integer, primary_key = True), 
        Column('location_number', Integer),
        Column('country_location', String(600)),
        Column('description', String(600)),
        Column('institute_name', String(600)),
        Column('cooperator', String(600)),
        Column('latitud', String(10)),
        Column('latitud_degress', Integer),
        Column('latitud_minutes', Integer),
        Column('longitude', String(10)),
        Column('longitude_degress', Integer),
        Column('longitude_minutes', Integer),
        Column('longitude_minutes', Integer),
        Column('altitude', Integer),
    )
    Table(
        'trait_capture', meta,
        Column('id', Integer, primary_key = True), 
        Column('web_file_id', Integer, ForeignKey("web_file.id"), nullable=False),
        Column('trait_id', Integer, ForeignKey("trait.id"), nullable=False),
        Column('genotype_id', Integer, ForeignKey("genotype.id"), nullable=False),
        Column('g_id', Integer),
        Column('genotype_number', String(200)),
    )
    Table(
        'trait_capture_location', meta,
        Column('id', Integer, primary_key = True), 
        Column('location_id', Integer, ForeignKey("location.id"), nullable=False),
        Column('trait_capture_id', Integer, ForeignKey("trait_capture.id"), nullable=False),
        Column('number', Integer),
        Column('value_number', Float),
        Column('value_string', String(600)),
    )
    

    meta.create_all(engine)