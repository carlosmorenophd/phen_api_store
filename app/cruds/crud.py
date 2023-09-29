from app import models, schemas


def create_web_file(web_file: schemas.WebFile):
    db_find = models.WebFile.filter(
        models.WebFile.name == web_file.name).first()
    if db_find:
        return db_find
    db_entity = models.WebFile(name=web_file.name)
    db_entity.save()
    return db_entity


def create_trail(trail: schemas.Trail):
    db_entity = models.Trail.filter(models.Trail.name == trail.name).first()
    if db_entity:
        return db_entity
    db_entity = models.Trail(name=trail.name)
    db_entity.save()
    return db_entity


def create_unit(unit: schemas.Unit):
    db_entity = models.Unit.filter(models.Unit.name == unit.name).first()
    if db_entity:
        return db_entity
    db_entity = models.Unit(name=unit.name)
    db_entity.save()
    return db_entity


def create_genotype(genotype: schemas.Genotype):
    db_entity = models.Genotype.filter(
        models.Genotype.c_id == genotype.c_id).filter(models.Genotype.s_id == genotype.s_id)
    print(db_entity)
    if db_entity:
        return db_entity.first()
    db_entity = models.Genotype(
        c_id=genotype.c_id,
        s_id=genotype.s_id,
        cross_name=genotype.cross_name,
        history_name=genotype.history_name,
    )
    db_entity.save()
    return db_entity


def create_crop_ontology(crop_ontology: schemas.CropOntology):
    db_entity = models.CropOntology.filter(
        models.CropOntology.name == crop_ontology.name
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.CropOntology(
        name=crop_ontology.name, ontology_db_id=crop_ontology.ontology_db_id
    )
    db_entity.save()
    return db_entity


def create_trait_ontology(trait_ontology: schemas.TraitOntology):
    db_entity = models.TraitOntology.filter(
        models.TraitOntology.trait_db_id == trait_ontology.trait_db_id
    ).first()
    if db_entity:
        return db_entity
    crop_ontology = models.CropOntology.filter(
        models.CropOntology.id == trait_ontology.crop_ontology_id
    ).first()
    if not crop_ontology:
        raise ValueError("The crop ontology is not valid")
    db_entity = models.TraitOntology(
        trait_db_id=trait_ontology.trait_db_id,
        name=trait_ontology.name,
        class_family=trait_ontology.class_family,
        description=trait_ontology.description,
        crop_ontology=crop_ontology,
    )
    db_entity.save()
    return db_entity


def create_method_ontology(method_ontology: schemas.MethodOntology):
    db_entity = models.MethodOntology.filter(
        models.MethodOntology.method_db_id == method_ontology.method_db_id
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.MethodOntology(
        method_db_id=method_ontology.method_db_id,
        name=method_ontology.name,
        class_family=method_ontology.class_family,
        description=method_ontology.description,
        formula=method_ontology.formula,
    )
    db_entity.save()
    return db_entity


def create_scale_ontology(scale_ontology: schemas.ScaleOntology):
    db_entity = models.ScaleOntology.filter(
        models.ScaleOntology.scale_db_id == scale_ontology.scale_db_id
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.ScaleOntology(
        scale_db_id=scale_ontology.scale_db_id,
        name=scale_ontology.name,
        data_type=scale_ontology.data_type,
        valid_values=scale_ontology.valid_values,
    )
    db_entity.save()
    return db_entity


def create_variable_ontology(variable_ontology: schemas.VariableOntology):
    db_entity = models.VariableOntology.filter(
        models.VariableOntology.observation_variable_db_id
        == variable_ontology.observation_variable_db_id
    ).first()
    if db_entity:
        return db_entity
    trait_ontology = models.TraitOntology.filter(
        models.TraitOntology.id == variable_ontology.trait_ontology_id
    ).first()
    if not trait_ontology:
        raise ValueError("The Crop Ontology is not valid")
    trait = models.Trait.filter(
        models.Trait.id == variable_ontology.trait_id).first()
    if not trait:
        raise ValueError("The Trait is not valid")
    method_ontology = models.MethodOntology.filter(
        models.MethodOntology.id == variable_ontology.method_ontology_id
    ).first()
    if not method_ontology:
        raise ValueError("The Method Ontology is not valid")
    scale_ontology = models.ScaleOntology.filter(
        models.ScaleOntology.id == variable_ontology.scale_ontology_id
    ).first()
    if not scale_ontology:
        raise ValueError("The Scale Ontology is not valid")
    db_entity = models.VariableOntology(
        name=variable_ontology.name,
        synonyms=variable_ontology.synonyms,
        growth_stage=variable_ontology.growth_stage,
        observation_variable_db_id=variable_ontology.observation_variable_db_id,
        trait_ontology=trait_ontology,
        trait=trait,
        method_ontology=method_ontology,
        scale_ontology=scale_ontology,
    )
    db_entity.save()
    return db_entity


def create_raw_collection(raw_collection: schemas.RawCollection):
    trail = models.Trail.filter(
        models.Trail.id == raw_collection.trail_id).first()
    if not trail:
        raise ValueError("The Trail is not valid")
    trait = models.Trait.filter(
        models.Trait.id == raw_collection.trait_id).first()
    if not trait:
        raise ValueError("The Trait is not valid")
    genotype = models.Genotype.filter(
        models.Genotype.id == raw_collection.genotype_id
    ).first()
    if not genotype:
        raise ValueError("The Genotype is not valid")
    location = models.Location.filter(
        models.Location.id == raw_collection.location_id
    ).first()
    if not location:
        raise ValueError("The Location is not valid")
    unit = models.Unit.filter(models.Unit.id == raw_collection.unit_id).first()
    if not unit:
        raise ValueError("The Unit is not valid")

    db_entity = models.RawCollection.filter(
        models.RawCollection.hash_raw == raw_collection.hash_raw
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.RawCollection(
        occurrence=raw_collection.occurrence,
        cycle=raw_collection.cycle,
        gen_number=raw_collection.gen_number,
        repetition=raw_collection.repetition,
        sub_block=raw_collection.sub_block,
        plot=raw_collection.plot,
        value_data=raw_collection.value_data,
        trail=trail,
        trait=trait,
        genotype=genotype,
        location=location,
        unit=unit,
        hash_raw=raw_collection.hash_raw,
    )
    db_entity.save()
    return db_entity


def search_trail_by_name(name: str):
    return list(models.Trail.filter(models.Trail.name % name))


def search_location_by_number(number: int):
    return models.Location.filter(models.Location.number == number).first()


def find_genotype_by_ids(c_id: int, s_id: int):
    genotype = models.Genotype.filter(
        models.Genotype.s_id == s_id
    ).filter(models.Genotype.c_id == c_id)
    print(genotype)
    if not genotype:
        raise ValueError("The genotype does not exist")
    return genotype.first()


def search_raw_collection(id: int, raw_collection: schemas.RawCollectionFilter):
    query = models.RawCollection.select()
    if raw_collection.occurrence != 0:
        query = query.where(
            models.RawCollection.occurrence == raw_collection.occurrence)
    if raw_collection.cycle != "":
        query = query.where(models.RawCollection.cycle == raw_collection.cycle)
    if raw_collection.gen_number != 0:
        query = query.where(models.RawCollection.gen_number ==
                            raw_collection.gen_number)
    if raw_collection.repetition != 0:
        query = query.where(models.RawCollection.repetition ==
                            raw_collection.repetition)
    if raw_collection.sub_block != 0:
        query = query.where(models.RawCollection.sub_block ==
                            raw_collection.sub_block)
    if raw_collection.plot != 0:
        query = query.where(models.RawCollection.plot == raw_collection.plot)
    if raw_collection.value_data != "":
        query = query.where(models.RawCollection.value_data ==
                            raw_collection.value_data)
    if raw_collection.trail_id != 0:
        query = query.where(models.RawCollection.trail_id ==
                            raw_collection.trail_id)
    if raw_collection.trait_id != 0:
        query = query.where(models.RawCollection.trait_id ==
                            raw_collection.trait_id)
    if raw_collection.genotype_id != 0:
        query = query.where(models.RawCollection.genotype_id ==
                            raw_collection.genotype_id)
    if raw_collection.location_id != 0:
        query = query.where(models.RawCollection.location_id ==
                            raw_collection.location_id)
    if raw_collection.unit_id != 0:
        query = query.where(models.RawCollection.unit_id ==
                            raw_collection.unit_id)
    # if raw_collection.location_ids:
    #     list_location = []
    #     for location_id in raw_collection.location_ids:
    #         list_location.append(models.Location.get_by_id(location_id))
    #     query = query.where(
    #         models.RawCollection.occurrence << list_location)
    return query.execute()


<<<<<<< HEAD:app/cruds/crud.py
def special_query_ids(target: schemas.EntityTarget) -> list[schemas.ResponseTarget]:
    if target == schemas.EntityTarget.genotype:
        return list(map(lambda id: schemas.ResponseTarget(id=id.id, name=id.cross_name), models.Genotype.select(models.Genotype.id, models.Genotype.cross_name).order_by(models.Genotype.id).execute()))
    elif target == schemas.EntityTarget.location:
        return list(map(lambda id: schemas.ResponseTarget(id=id.id, name=id.description), models.Location.select(models.Location.id, models.Location.description).order_by(models.Location.id).execute()))
    elif target == schemas.EntityTarget.trait:
        return list(map(lambda id: schemas.ResponseTarget(id=id.id, name=id.name), models.Trait.select(models.Trait.id, models.Trait.name).order_by(models.Trait.id).execute()))
    elif target == schemas.EntityTarget.repetition:
        return list(map(lambda id: schemas.ResponseTarget(id=int(id.repetition), name=str(id.repetition)), models.RawCollection.select(models.RawCollection.repetition).distinct().order_by(models.RawCollection.repetition).execute()))
    elif target == schemas.EntityTarget.cycle:
        return list(map(lambda id: schemas.ResponseTarget(id=int(id.cycle), name=id.cycle), models.RawCollection.select(models.RawCollection.cycle).distinct().order_by(models.RawCollection.cycle).execute()))
    raise ValueError("Unsupported target")
=======
def find_trait_by_name(name: str):
    trait = models.Trait.filter(models.Trait.name == name).first()
    if not trait:
        raise ValueError("The trait does not exist")
    return trait


def update_trait(id: int, trait: schemas.Trait):
    db_entity = models.Trait.filter(models.Trait.id == id).first()
    if not db_entity:
        raise ValueError("The trait does not exist")
    db_entity.co_trait_name = trait.co_trait_name
    db_entity.variable_name = trait.variable_name
    db_entity.co_id = trait.co_id
    db_entity.save()
    return db_entity

def get_raw_join_all(genotype_id: int, cycle: str)-> str:
    cursor = models.db.execute_sql("SELECT id, occurrence, `cycle`, gen_number, repetition, sub_block, plot, genotype_id, location_id, value_1, value_2, value_3, value_4, value_5, value_6, value_7, value_8, value_9, value_10, value_11, value_12, value_13, value_14, value_15, value_16, value_17, value_18, value_19, value_20, value_21, value_22, value_23, value_24, value_25, value_26, value_27, value_28, value_29, value_30, value_31, value_32, value_33, value_34, value_35, value_36, value_37, value_38, value_39, value_40, value_41, value_42, value_43, value_44, value_45, value_46, value_47, value_48, value_49, value_50, value_51, value_52, value_53, value_54, value_55, value_56, value_57, value_58, value_59, value_60, value_61, value_62, value_63, value_64, value_65, value_66 FROM phenotipyc_db.raw_all_join WHERE genotype_id = {} AND `cycle`= {};".format(genotype_id, cycle))
    for row in cursor.fetchall():
        print(row)
    return "OK"
>>>>>>> main:app/crud.py
