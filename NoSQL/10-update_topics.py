#!/usr/bin/env python3
"""
function that changes all topics of a school document based on the names
"""


def update_topics(mongo_collection, name, topics):
    """
    Actualizar los documentos que coincidan con el nombre dado
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
