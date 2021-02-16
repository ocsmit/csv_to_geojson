csv_to_geojson.py
-----------------

Little cli tool to convert csv column to GeoJSON Feature Collection.

Usage:
python csv_to_geojson.py input.csv output.json "GeoJSON Field" "Propery 1" "Property 2" ...

Can use ogr2ogr to convert to different formats from this.

e.g. ogr2ogr -f "ESRI Shapefile" example.shp example.json

