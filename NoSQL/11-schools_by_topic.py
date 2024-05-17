#!/usr/bin/env python3
"""
function that returns the list of school having a specific topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    Buscar todas las escuelas que tienen el tema específico
    """
    cursor = mongo_collection.find({"topics": topic})
    schools = [school for school in cursor]
    return schools
