from avroutil import get_fastavro_schema
import fhir
import fastavro
import io
import json


def encode(obj, schema):
    fastavro.validate(obj, schema)
    buffer = io.BytesIO()
    fastavro.schemaless_writer(buffer, schema, obj)
    return buffer.getvalue()

for resource_type, resource in fhir.examples.items():
    avro_schema = get_fastavro_schema(resource_type)

    try:
        resource = json.loads(resource)
        avro_data = encode(resource, avro_schema)
        with open(f'avro/{resource_type}.avro', 'wb+') as avro_output_file:
            avro_output_file.write(avro_data)
    except Exception as e:
        print(f'{resource_type}: {e}')
        continue
