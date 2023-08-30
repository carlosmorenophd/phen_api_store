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
        self.meta_data = MetaData()

        self.web_files = Table(
            'web_files', self.meta_data,
            Column('id', Integer, primary_key=True),
            Column('name', String(300)),
        )
        self.trails = Table(
            'trails', self.meta_data,
            Column('id', Integer, primary_key=True),
            Column('name', String(300)),
        )
        self.units = Table(
            'units', self.meta_data,
            Column('id', Integer, primary_key=True),
            Column('name', String(300)),
        )
        self.traits = Table(
            'traits', self.meta_data,
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
            'genotypes', self.meta_data,
            Column('id', Integer, primary_key=True),
            Column('c_id', Integer),
            Column('s_id', Integer),
            Column('cross_name', String(600)),
            Column('history', String(600)),
        )
        # Find this file and load
        self.locations = Table(
            'locations', self.meta_data,
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
            'raw_collections', self.meta_data,
            Column('id', Integer, primary_key=True),
            Column('trails_id', Integer, ForeignKey("trails.id"), nullable=False),
            Column('traits_id', Integer, ForeignKey("traits.id"), nullable=False),
            Column('genotypes_id', Integer, ForeignKey("genotypes.id"), nullable=False),
            Column('locations_id', Integer, ForeignKey("locations.id"), nullable=False),
            Column('occurrence', Integer),
            Column('cycle', String(4)),
            Column('gen_number', Integer),
            Column('repetition', Integer),
            Column('sub_block', Integer),
            Column('value', String(100)),
        )

        self.meta_data.create_all(self.engine)

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
            item['trails_id'] = self.insert_raw_trail(trail_name=item.pop('trails.name'))
            item['locations_id'] = self.insert_raw_location(
                location=dict(number=item.pop('locations.number'), country=item.pop('locations.country'),
                              description=item.pop('locations.description')))
            item['genotypes_id'] = self.insert_raw_genotype(
                genotype=dict(c_id=item.pop('genotypes.c_id'), s_id=item.pop('genotypes.s_id'),
                              cross_name=item.pop('genotypes.cross_name')))
            item['traits_id'] = self.insert_raw_trait(
                trait=dict(number=item.pop('traits.trait_number'), name=item.pop('traits.name')))
            item['units_id'] = self.insert_raw_unit(unit=dict(name=item.pop('units.name')))
            with self.engine.connect() as conn:
                conn.execute(self.raw_collections.insert(), item)
                conn.commit()

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

    def insert_raw_location(self, location):
        with self.engine.connect() as conn:
            stmt = select(self.locations.c.id).where(location['number'] == self.locations.c.number)
            result = conn.execute(stmt).first()
            if result:
                return result.id
            conn.execute(self.locations.insert(), location)
            conn.commit()
            result = conn.execute(stmt).first()
            if result:
                return result.id
        return 0

    def insert_raw_genotype(self, genotype: dict) -> int:
        with self.engine.connect() as conn:
            stmt = select(self.genotypes.c.id).where(
                genotype['s_id'] == self.genotypes.c.s_id and genotype['c_id'] == self.genotypes.c.c_id)
            result = conn.execute(stmt).first()
            if result:
                return result.id
            conn.execute(self.genotypes.insert(), genotype)
            conn.commit()
            result = conn.execute(stmt).first()
            if result:
                return result.id
        return 0

    def insert_raw_trait(self, trait: dict) -> int:
        with self.engine.connect() as conn:
            stmt = select(self.traits.c.id).where(trait['number'] == self.traits.c.number)
            result = conn.execute(stmt).first()
            if result:
                return result.id
            conn.execute(self.traits.insert(), trait)
            conn.commit()
            result = conn.execute(stmt).first()
            if result:
                return result.id
        return 0

    def insert_raw_unit(self, unit: dict) -> int:
        with self.engine.connect() as conn:
            stmt = select(self.units.c.id).where(unit['name'] == self.units.c.name)
            result = conn.execute(stmt).first()
            if result:
                return result.id
            conn.execute(self.units.insert(), unit)
            conn.commit()
            result = conn.execute(stmt).first()
            if result:
                return result.id
        return 0
