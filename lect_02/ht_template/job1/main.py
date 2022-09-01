"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
import os
from flask import Flask, request
from flask import typing as flask_typing

import api
import storage


API_AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")

if not API_AUTH_TOKEN:
    print("API_AUTH_TOKEN environment variable must be set")


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer

    Proposed POST body in JSON:
    {
      "data: "2022-08-09",
      "raw_dir": "path/to/target/"
    }
    """
    input_data: dict = request.json
    # TODO: implement me
    # NB: you should handle the request and call these functions:
    # api.get_sales()
    # storage.save_to_disk()

    return {
               "message": "Data retrieved successfully from API",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)