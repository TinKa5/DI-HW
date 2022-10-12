import os
import glob
import json
from fastavro import writer, parse_schema

schema = {
    "doc": "Product rices",
    "name": "Prices",
    "type": "record",
    "fields": [
        {"name": "client", "type": "string"},
        {"name": "purchase_date", "type": {"type" : "int","logicalType": "date"}},
        {"name": "product", "type": "string"},
        {"name": "price", "type": "int"}
    ]
}


def modify_to_avro(raw_dir, stg_dir):
    clear_dir(stg_dir)
    files = glob.glob(raw_dir + "/*")
    for f in files:

        with open(f, 'r') as file:
            data = json.load(file)

        parsed_schema = parse_schema(schema)
        filename = get_filename(f)
        avro_path = os.path.normpath(os.path.join(stg_dir, filename) + ".avro");
        with open(avro_path, 'wb') as out:
            writer(out, parsed_schema, data)


def get_filename(path) -> str:
    return os.path.splitext(os.path.basename(path))[0]


def clear_dir(dir_path):
    files = glob.glob(dir_path+ "/*")
    for f in files:
        os.remove(f)
