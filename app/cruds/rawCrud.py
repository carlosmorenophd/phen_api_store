from app import models, schemas
from csv import writer
import os

# TODO: Convertir en dinamica para poder seleccionar con una lista de traits
# TODO: soportar la unidad dentro de los traits
query_raw_all = "SELECT raj.id, raj.occurrence, raj.`cycle`, raj.gen_number, raj.repetition, raj.sub_block, raj.plot, raj.genotype_id, raj.location_id, \
g.cross_name, l.country , l.description , l.institute_name , \
raj.value_1,'t/ha' as u_1,  raj.value_2, 'g' as u_2, raj.value_3,'cm' as u_3, raj.value_5, '1-5' as u_5, raj.value_6, 'dias' as u_6, raj.value_12, 'dias' as u_12, raj.value_14, 'doble digito' as u_14 \
FROM raw_all_join raj \
LEFT JOIN genotype g ON g.id =raj.genotype_id \
LEFT JOIN location l ON l.id = raj.location_id "


def get_raw_all_join_by_id(id: int):
    cursor = models.db.execute_sql(
        "{}WHERE raj.id = {}; ".format(query_raw_all, id))
    return cursor


def get_raw_join_by_cycle_genotype_id(cycle: str, genotype_id: int):
    cursor = models.db.execute_sql(
        "{} WHERE raj.`cycle` = {} and raj.genotype_id = {} ; "
        .format(query_raw_all, cycle, str(genotype_id)))
    return cursor
