#!/usr/bin/env python3
import geocoder
import sys
import os
import yaml
import base64
from typing import List

def convert_location(locations: List[str], keys: List[str]) -> str:
    key_use_counter = 0
    key_counter = 0

    mappings = {
    "Western Sahara" : "W. Sahara",
    "Congo Republic" : "Congo",
    "DR Congo" : "Dem. Rep. Congo",
    "Eswatini" : "eSwatini",
    "North Macedonia" :"Macedonia",
    "United States" : "United States of America",
    "Ivory coast": "Côte d'Ivoire",
    "Falkland Islands" : "Falkland Is.",
    "French Southern Territories" : "Fr. S. Antarctic Lands",
    "Central African Republic" : "Central African Rep.",
    "Equatorial Guinea" : "Eq. Guinea",
    "Solomon Islands" : "Solomon Is.",
    "Bosnia and Herzegovina" : "Bosnia and Herz.",
    "South Sudan" : "S. Sudan" }

    result = []

    for x in locations:
        g = geocoder.geonames(x, key=keys[key_counter],featureClass='A')
        key_use_counter += 1
        if g.country != None:
            country = g.country
            if country in mappings.keys():
                country = mappings[country]
                result.append(country)
            else:
                result.append(country)
    
    return result

if __name__ == "__main__":
    command = sys.argv[1]
    argument = [str(os.environ[f"LOCATIONS_{i}"]) for i in range(int(os.environ["LOCATIONS"]))]
    argument_keys = [str(os.environ[f"KEYS_{i}"]) for i in range(int(os.environ["KEYS"]))]

    functions = {
        "convert_location": convert_location,
    }
    output = functions[command](argument, argument_keys)
    print("--> START CAPTURE")
    print(yaml.dump({"output": output}))
    print("--> END CAPTURE")