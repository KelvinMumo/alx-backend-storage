#!/usr/bin/env python3
"""
inserts a new document
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document
    """
    new_docs = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
