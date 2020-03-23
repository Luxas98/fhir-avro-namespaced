import glob
import json
from fastavro import parse_schema

schema_files = glob.glob('fhir_fastavro/schema/*.avsc')
schema_files.sort()

fastavro_mappings = {}

for schema_file in schema_files:
    with open(schema_file, 'r') as avro_json_file:
        schema_json = json.load(avro_json_file)

        try:
            schema = parse_schema(schema_json)
            if 'name' in schema_json:
                resource_type = schema_json["name"]
                print(f'Adding schema for {resource_type}')
                fastavro_mappings[resource_type] = schema
        except Exception as e:
            print(e)
            continue

def get_fastavro_schema(resource_type):
    return fastavro_mappings[resource_type]