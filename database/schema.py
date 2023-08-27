from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float
from sqlalchemy import URL
from decouple import config

url_object = URL.create(
    'mysql+pymysql',
    username=config('DB_USER'),
    password=config('DB_PASS'),
    host="127.0.0.1",
    port=3306,
    database=config('DB_SCHEMA'),
)

engine = create_engine(url_object)
meta = MetaData()


def create_entities():
    Table(
        'web_files', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String(300)),
    )
    Table(
        'traits', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String(300)),
        Column('description', String(500)),
        Column('co_trait_name', String(200)),
        Column('variable_name', String(200)),
        Column('co_id', String(400)),
    )
    # Find this file and load
    Table(
        'genotypes', meta,
        Column('id', Integer, primary_key=True),
        Column('c_id', Integer),
        Column('s_id', Integer),
        Column('cross_name', String(600)),
        Column('history', String(600)),
    )
    # Find this file and load
    Table(
        'locations', meta,
        Column('id', Integer, primary_key=True),
        Column('location_number', Integer),
        Column('country_location', String(600)),
        Column('description', String(600)),
        Column('institute_name', String(600)),
        Column('cooperator', String(600)),
        Column('latitude', String(10)),
        Column('latitude_degrees', Integer),
        Column('latitude_minutes', Integer),
        Column('longitude', String(10)),
        Column('longitude_degrees', Integer),
        Column('longitude_minutes', Integer),
        Column('altitude', Integer),
    )
    Table(
        'trait_captures', meta,
        Column('id', Integer, primary_key=True),
        Column('web_file_id', Integer, ForeignKey("web_files.id"), nullable=False),
        Column('trait_id', Integer, ForeignKey("traits.id"), nullable=False),
        Column('genotype_id', Integer, ForeignKey("genotypes.id"), nullable=False),
        Column('g_id', Integer),
        Column('genotype_number', String(200)),
    )
    Table(
        'trait_capture_locations', meta,
        Column('id', Integer, primary_key=True),
        Column('location_id', Integer, ForeignKey("locations.id"), nullable=False),
        Column('trait_capture_id', Integer, ForeignKey("trait_captures.id"), nullable=False),
        Column('number', Integer),
        Column('value_number', Float),
        Column('value_string', String(600)),
    )

    meta.create_all(engine)
