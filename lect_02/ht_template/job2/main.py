from flask import Flask, request
from flask import typing as flask_typing
from lect_02.ht_template.job2 import api

app = Flask(__name__)

"""
Proposed POST body in JSON:
    {
      "stg_dir": "/path/to/my_dir/stg/sales/2022-08-09" 
      "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09",
      
    }
    
"""


@app.route('/', methods = ['POST'])
def main() -> flask_typing.ResponseReturnValue:

    input_date: dict = request.json

    if not input_date.get('raw_dir'):
        return {
            "message": "raw_dir is missed",
               }, 400

    if not input_date.get('stg_dir'):
        return {
            "message": "stg_dir is missed",
               }, 400

    api.modify_to_avro(input_date.get('raw_dir'), input_date.get('stg_dir'))

    return {
               "message": "Data retrieved successfully from API",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)

