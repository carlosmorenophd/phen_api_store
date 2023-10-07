import os
from app.schemas import customs, schemas
from csv import writer
from app.cruds import (
    locationCrud,
    rawCrud,
    trailCrud,
    unitCrud,
    webFileCrud,
    traitCrud,
)
from app.services.MeanRawCountryInstituteService import MeanRawCountryInstitute


def get_raw_join_all(raw_filter: customs.RawAllFilter) -> str:
    """ To delete
    Args:
        raw_filter (schemas.RawAllFilter): _description_

    Returns:
        str: _description_
    """
    name_csv = "text.csv"
    if os.path.exists(name_csv):
        os.remove(name_csv)
    write_on_csv(name_csv=name_csv, list_element=["padre", "tipo", "id", "occurencia", "ciclo", "gen numero", "repeticion", "sub bloque", "plot", "genotipo id", "locacion id", "nombre genotipo", "pais", "ciudad", "instituto", "GRAIN_YIELD", "GRAIN_YIELD Unidad",
                 "1000_GRAIN_WEIGHT", "1000_GRAIN_WEIGHT Unidad", "PLANT_HEIGHT", "PLANT_HEIGHT Unidad", "AGRONOMIC_SCORE", "AGRONOMIC_SCORE Unidad", "DAYS_TO_HEADING", "DAYS_TO_HEADING Unidad", "DAYS_TO_MATURITY", "DAYS_TO_MATURITY Unidad", "TEST_WEIGHT", "TEST_WEIGHT Unidad", "mean", "grain_yield_class"])
    mean = MeanRawCountryInstitute(
        country="MEXICO", institute="CIMMYT", index_country=10, index_institute=12, index_data=13)
    for id in raw_filter.ids:
        cursor = rawCrud.get_raw_all_join_by_id(id)
        for row in cursor.fetchall():
            mean.clean()
            cursor_same_genotype = rawCrud.get_raw_join_by_cycle_genotype_id(
                cycle=row[2], genotype_id=int(row[7]))
            for row_child in cursor_same_genotype:
                mean.add_item(row_child=row_child)

            write_on_csv(name_csv=name_csv, list_element=[
                "", "principal", *row, mean.get_mean(),
                mean.get_tag(data_parent=float(row[13]))])
            if raw_filter.is_details:
                for row_child in cursor_same_genotype:
                    type = "otro experimento"
                    if row_child[10] == "MEXICO" and row_child[12] == "CIMMYT":
                        type = "control"
                    write_on_csv(name_csv=name_csv, list_element=[
                        row[0], type, *row_child, ])
    return "OK"


def get_raw_join_all_trait(raw_filter: customs.RawAllFilter) -> str:
    print(raw_filter)
    name_csv = "text.csv"
    if 1 in raw_filter.trait_ids:
        raise ValueError(
            "Trait id 1 can't be adding by the user in automatic is adding")
    if os.path.exists(name_csv):
        os.remove(name_csv)
    list_head = ["padre", "tipo", "id", "occurencia", "ciclo", "gen numero",
                 "repeticion", "sub bloque", "plot",
                 "genotipo id", "locacion id", "nombre genotipo", "pais",
                 "ciudad", "instituto", "GRAIN_YIELD"]
    trait_ids = raw_filter.trait_ids
    trait_ids.insert(0, 1)
    traits = rawCrud.get_list_trait(trait_ids=trait_ids)
    for trait in traits:
        list_head.append(trait.name)
    list_head.extend(["mean", "grain_yield_class"])
    write_on_csv(name_csv=name_csv, list_element=list_head)
    mean = MeanRawCountryInstitute(
        country="MEXICO",
        institute="CIMMYT",
        index_country=10,
        index_institute=12,
        index_data=13
    )
    for id in raw_filter.ids:
        # print("ID to work", id)
        cursor = rawCrud.get_raw_by_id_with_trait(id=id, trait_ids=trait_ids)
        for row in cursor.fetchall():
            mean.clean()
            cursor_same_genotype = rawCrud.get_raw_by_cycle_genotype_id_with_trait(
                trait_ids=trait_ids,
                cycle=row[2],
                genotype_id=int(row[7])
            )
            for row_child in cursor_same_genotype:
                mean.add_item(row_child=row_child)
            write_on_csv(name_csv=name_csv, list_element=[
                "", "principal", *row, mean.get_mean(),
                mean.get_tag(data_parent=float(row[13]))])
            if raw_filter.is_details:
                # print("Adding child", cursor_same_genotype)
                cursor_same_genotype = rawCrud.get_raw_by_cycle_genotype_id_with_trait(
                    trait_ids=trait_ids,
                    cycle=row[2],
                    genotype_id=int(row[7])
                )
                for row_child in cursor_same_genotype:
                    # print("Child id", row_child[0])
                    type = "otro experimento"
                    if row_child[10] == "MEXICO" and row_child[12] == "CIMMYT":
                        type = "control"
                    write_on_csv(name_csv=name_csv, list_element=[
                        row[0], type, *row_child, ])
    return "OK"


def write_on_csv(name_csv, list_element):
    with open(name_csv, 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list_element)
        f_object.close()


def save_raw_data(raw_data: customs.RawData):
    # : str
    # location_number: int
    # location_country: str
    # trait_number: int
    # trait_name: str
    # field_occurrence: int
    # field_description: str
    # field_agricultural_cycle: str
    # unit_name: str
    # web_file_name: str
    # genotype_c_id: int
    # genotype_s_id: int
    # genotype_name: str
    # genotype_number: int
    # repetition: int
    # sub_block: int
    # plot: int
    # value_data: str
    # hash_raw: str
    db_location = locationCrud.find_by_country_number(
        country=raw_data.location_country,
        number=raw_data.location_number,
    )
    if not db_location:
        raise ValueError("Can not find location : {}".format(
            raw_data.location_number
        ))
    db_trail = trailCrud.find_by_name(
        name=raw_data.trial_name,
    )
    if not db_trail:
        raise ValueError("Can not found trail {}".format(
            raw_data.trial_name
        ))

    db_unit = unitCrud.get_or_create(
        unit=schemas.UnitCreate(
            name=raw_data.unit_name,
        )
    )
    db_web_file = webFileCrud.get_or_create(
        web_file=schemas.WebFileCreate(
            name=raw_data.web_file_name
        )
    )

    db_trait = traitCrud.find_by_name_number(
        name=raw_data.trait_name,
        number=raw_data.trait_number
    )

    # trail = dict()
    # trail["name"] = raw_collection.pop("trails.name")
    # response = requests.post(
    #     url="{}/trails/".format(self.url_base),
    #     headers={"Accept": "application/json"},
    #     json=trail,
    # )
    # if not response.ok:
    #     raise ConnectionError(response.text())
    # raw_collection["trail_id"] = response.json()["id"]
    # number = raw_collection.pop("locations.number")
    # raw_collection.pop("locations.country")
    # raw_collection.pop("locations.description")
    # response = requests.get(
    #     url="{}/locations/".format(self.url_base),
    #     headers={"Accept": "application/json"},
    #     params={"number": int(number)},
    # )
    # if not response.ok:
    #     raise ConnectionError(response.text())
    # raw_collection["location_id"] = response.json()["id"]
    # ids = {
    #     "c_id": raw_collection.pop("genotypes.c_id"),
    #     "s_id": raw_collection.pop("genotypes.s_id"),
    # }
    # raw_collection.pop("genotypes.cross_name")
    # response = requests.get(
    #     url="{}/genotypes/".format(self.url_base),
    #     headers={"Accept": "application/json"},
    #     params=ids,
    # )
    # if not response.ok:
    #     raise ConnectionError(response.text())
    # raw_collection["genotype_id"] = response.json()["id"]
    # trait = {
    #     "name": raw_collection.pop("traits.name"),
    #     "number": raw_collection.pop("traits.trait_number"),
    #     "description": "",
    #     "co_trait_name": "",
    #     "variable_name": "",
    #     "co_id": "",
    # }
    # response = requests.post(
    #     url="{}/traits/".format(self.url_base),
    #     headers={"Accept": "application/json"},
    #     json=trait,
    # )
    # if not response.ok:
    #     raise ConnectionError(response.text())
    # raw_collection["trait_id"] = response.json()["id"]

    # response = requests.post(
    #     url="{}/units/".format(self.url_base),
    #     headers={"Accept": "application/json"},
    #     json={"name": raw_collection.pop("units.name")},
    # )
    # if not response.ok:
    #     raise ConnectionError(response.text())
    # raw_collection["unit_id"] = response.json()["id"]
