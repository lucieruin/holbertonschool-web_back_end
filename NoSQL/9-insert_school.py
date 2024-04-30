#!/usr/bin/env python3
""" inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ insert a new document """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
