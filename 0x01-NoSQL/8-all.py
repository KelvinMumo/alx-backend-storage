#!/usr/bin/env python3
"""
lists all documents in a collection
"""


def list_all(mongo_collection):
    """list all docs in a collection
    :param mongo_collection
    :return: docs
    """
    return mongo_collection.find()
