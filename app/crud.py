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


def create_trait(trait: schemas.Trait):
    db_entity = models.Trait.filter(
        models.Trait.name == trait.name).filter(models.Trait.number == trait.number).first()
    if db_entity:
        return db_entity
    db_entity = models.Trait(
        name=trait.name,
        number=trait.number,
        description=trait.description,
        co_trait_name=trait.co_trait_name,
        variable_name=trait.variable_name,
        co_id=trait.co_id,
    )
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


def create_location(location: schemas.Location):
    db_entity = models.Location.filter(
        models.Location.number == location.number
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.Location(
        number=location.number,
        country=location.country,
        description=location.description,
        institute_name=location.institute_name,
        cooperator=location.cooperator,
        latitude=location.latitude,
        latitude_degrees=location.latitude_degrees,
        latitude_minutes=location.latitude_minutes,
        longitude=location.longitude,
        longitude_degrees=location.longitude_degrees,
        longitude_minutes=location.longitude_minutes,
        altitude=location.altitude,
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


def find_trait_by_number(number: int):
    trait = models.Trait.filter(models.Trait.number == number).first()
    if not trait:
        raise ValueError("The trait does not exist")
    return trait


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