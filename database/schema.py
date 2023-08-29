from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float, Identity
from sqlalchemy import URL, select
from decouple import config
import logging


class Database:
    def __init__(self):
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
        url_object = URL.create(
            'mysql+pymysql',
            username=config('DB_USER'),
            password=config('DB_PASS'),
            host="127.0.0.1",
            port=3306,
            database=config('DB_SCHEMA'),
        )
        self.engine = create_engine(url_object)
        self.metaData = MetaData()

        self.web_files = Table(
            'web_files', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('name', String(300)),
        )
        self.trails = Table(
            'trails', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('name', String(300)),
        )
        self.units = Table(
            'units', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('name', String(300)),
        )
        self.traits = Table(
            'traits', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('name', String(300)),
            Column('number', Integer),
            Column('description', String(500)),
            Column('co_trait_name', String(200)),
            Column('variable_name', String(200)),
            Column('co_id', String(400)),
        )
        # Find this file and load
        self.genotypes = Table(
            'genotypes', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('c_id', Integer),
            Column('s_id', Integer),
            Column('cross_name', String(600)),
            Column('history', String(600)),
        )
        # Find this file and load
        self.locations = Table(
            'locations', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('number', Integer),
            Column('country', String(600)),
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
        self.raw_collections = Table(
            'raw_collections', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('trail_id', Integer, ForeignKey("trails.id"), nullable=False),
            Column('trait_id', Integer, ForeignKey("traits.id"), nullable=False),
            Column('genotype_id', Integer, ForeignKey("genotypes.id"), nullable=False),
            Column('location_id', Integer, ForeignKey("locations.id"), nullable=False),
            Column('occurrence', Integer),
            Column('cycle', String(4)),
            Column('gen_number', Integer),
            Column('repetition', Integer),
            Column('sub_block', Integer),
            Column('value', String(100)),
        )

        self.metaData.create_all(self.engine)

    def insert_location(self, array_dictionary):
        with self.engine.connect() as conn:
            result = conn.execute(self.locations.insert(), array_dictionary)
            print(result)
            conn.commit()

    def insert_genotypes(self, array_dictionary):
        with self.engine.connect() as conn:
            result = conn.execute(self.genotypes.insert(), array_dictionary)
            print(result)
            conn.commit()

    def insert_raw(self, array_dictionary):
        for item in array_dictionary:
            item['trail_id'] = self.insert_raw_trail( trail_name=item.pop('trails.name'))
            print(item)
            return '1'

    def insert_raw_trail(self, trail_name):
        with self.engine.connect() as conn:
            stmt = select(self.trails.c.id).where(self.trails.c.name == trail_name)
            result = conn.execute(stmt).first()
            if result:
                return result.id
            conn.execute(self.trails.insert(), {'name': trail_name})
            conn.commit()
            result = conn.execute(stmt).first()
            if result:
                return result.id
        return 0

