from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float, Identity
from sqlalchemy import URL
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
        self.traits = Table(
            'traits', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('name', String(300)),
            Column('trait_number', Integer),
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
        self.trait_captures = Table(
            'trait_captures', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('web_file_id', Integer, ForeignKey("web_files.id"), nullable=False),
            Column('trait_id', Integer, ForeignKey("traits.id"), nullable=False),
            Column('genotype_id', Integer, ForeignKey("genotypes.id"), nullable=False),
            Column('g_id', Integer),
            Column('genotype_number', String(200)),
        )
        self.trait_capture_locations = Table(
            'trait_capture_locations', self.metaData,
            Column('id', Integer, primary_key=True),
            Column('location_id', Integer, ForeignKey("locations.id"), nullable=False),
            Column('trait_capture_id', Integer, ForeignKey("trait_captures.id"), nullable=False),
            Column('number', Integer),
            Column('value_number', Float),
            Column('value_string', String(600)),
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
