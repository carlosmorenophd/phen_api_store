from app import models, schemas
from csv import writer
import os

# TODO: Convertir en dinamica para poder seleccionar con una lista de traits
query_raw_all = "SELECT raj.id, raj.occurrence, raj.`cycle`, raj.gen_number, raj.repetition, raj.sub_block, raj.plot, raj.genotype_id, raj.location_id, \
g.cross_name, l.country , l.description , l.institute_name , \
raj.value_1,'t/ha' as u_1,  raj.value_2, 'g' as u_2, raj.value_3,'cm' as u_3, raj.value_5, '1-5' as u_5, raj.value_6, 'dias' as u_6, raj.value_12, 'dias' as u_12, raj.value_14, 'doble digito' as u_14 \
FROM raw_all_join raj \
LEFT JOIN genotype g ON g.id =raj.genotype_id \
LEFT JOIN location l ON l.id = raj.location_id "

# TODO: soportar la unidad dentro de los traits
def get_raw_join_all(raw_filter: schemas.RawAllFilter) -> str:
    name_csv = "text.csv"
    if os.path.exists(name_csv):
        os.remove(name_csv)
    write_on_csv(name_csv=name_csv, list_element=["padre", "tipo", "id", "occurencia", "ciclo", "gen numero", "repeticion", "sub bloque", "plot", "genotipo id", "locacion id", "nombre genotipo", "pais", "ciudad", "instituto", "GRAIN_YIELD", "GRAIN_YIELD Unidad",
                 "1000_GRAIN_WEIGHT", "1000_GRAIN_WEIGHT Unidad", "PLANT_HEIGHT", "PLANT_HEIGHT Unidad", "AGRONOMIC_SCORE", "AGRONOMIC_SCORE Unidad", "DAYS_TO_HEADING", "DAYS_TO_HEADING Unidad", "DAYS_TO_MATURITY", "DAYS_TO_MATURITY Unidad", "TEST_WEIGHT", "TEST_WEIGHT Unidad"])
    for id in raw_filter.ids:
        cursor = models.db.execute_sql(
            "{}WHERE raj.id = {}; ".format(query_raw_all, id))
        for row in cursor.fetchall():
            write_on_csv(name_csv=name_csv, list_element=[
                         "", "principal", *row,])
            cursor_same_genotype = models.db.execute_sql(
                "{} WHERE raj.`cycle` = {} and raj.genotype_id = {} ; ".format(query_raw_all, row[2], row[7]))
            for row_child in cursor_same_genotype:
                tipo = "otro experimento"
                if row_child[10] == "MEXICO" and row_child[12] == "CIMMYT":
                    tipo = "control"
                write_on_csv(name_csv=name_csv, list_element=[
                             row[0], tipo, *row_child,])
    return "OK"


def write_on_csv(name_csv, list_element):
    with open(name_csv, 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list_element)
        f_object.close()
