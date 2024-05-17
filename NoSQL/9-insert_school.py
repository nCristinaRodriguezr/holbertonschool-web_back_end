#!/usr/bin/env python3
"""
function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insertar el nuevo documento en la colección
    Retornar el _id del nuevo documento
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
