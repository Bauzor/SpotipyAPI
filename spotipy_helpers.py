# -*- coding: utf-8 -*-
"""Spotipy Helper Functions

This module contains functions that will be used for the purpose of making the code of 
my other scripts for data processing easier to read and work with.

Todo:
    *nothing for now

"""

from collections import Iterable

primitive_and_none = (str, int, bool, float)

def is_prim(thing):
    return isinstance(thing, primitive_and_none)


def flatten(package, string="", product={}):
    """flatten takes in a header row and a key who has a value that is also a dictionary and
    creates new header row titles with the original header row concatenated with the keys of the dictionary that 
    have values that are also not dictionaries. In the case that there are more dictionaries inside, we perform temp onto
    those keys.

    key = 'string'
    value = {} or [] or 'string'
    """

    for init_key in package:
        key = string + init_key

        if isinstance(package, dict):

            if is_prim(package[init_key]) or package[init_key] == None:
                product[key] = package[init_key]
                
            elif isinstance(package[init_key], list):
                i = 0
                key = key + "-"
                while(i < len(package[init_key])):
                    flatten(package[init_key][i], key, product)   
                    i += 1                             
            elif isinstance(package[init_key], dict):
                key = key + "-"
                flatten(package[init_key], key, product)
    return product
