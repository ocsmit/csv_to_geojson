# Title: csv_to_geojson.py
# Author: Owen Smith
# About:CLI tool to convert a column containing GeoJSON entries to a single GeoJSON
#       Object.
# Usage: python csv_to_geojson.py input.csv output.json "GeoJSON Field" "Prop 1" "2" ...


import json
# TODO: Implement with only csv library.
import pandas as pd
import sys
import getopt


def csv_to_json(csv_in, outfile, json_field, fields):

    # Read csv into Pandas dataframe
    df = pd.read_csv(csv_in) #"./pfi_small_grains.csv")

    # Get JSON field and convert to list
    geojsons = df[json_field].tolist()

    # Create dictonary object of property name and property values.
    field_dict = {}
    for i in fields:
        field_dict[i] = df[i].tolist()

    # List of keys
    keys = list(field_dict.keys())

    # Create GeoJSON object
    # Iterate over each entry and deconstruct
    features = []
    for i in range(len(geojsons)):
        # load json string into dict object
        entry = json.loads(geojsons[i])
        # Get feature coordinates and geometry type
        coordinates = entry["coordinates"]
        ty = entry["type"]
        # Iterate over entries respective property fields and get the
        # corresponding property values.
        prop = {}
        for j in keys:
            prop[j] = field_dict[j][i]
        # Append entry to full feature list
        features.append({"type": "Feature", "geometry": {"type": ty,
                        "coordinates": coordinates}, "properties": prop})

    # Create main JSON object and add sub headers
    fc = {"type": "FeatureCollection", "features": features}

    # Write output json with proper formatting
    with open(outfile, 'w') as f:
        f.write(json.dumps(fc, indent=2))

# RUN
if __name__ == "__main__":
    # Get commandline arguments
    args = sys.argv
    # Skip first 'self' arg, get input csv
    csv = args[1]
    # Read outfile
    outfile = args[2]
    # JSON is second arg
    json_field = args[3]
    # Last arguments are property fields
    prop_fields = args[4:]

    # run function
    csv_to_json(csv, outfile, json_field, prop_fields)
