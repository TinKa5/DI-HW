import requests
import os
from lect_02.ht_template.job1.storage import save_to_disk

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
ENDPOINT = 'sales'
AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")
RAW_DIR_FIELD = 'raw_dir'
DATE_FIELD = 'date'
FILE_NAME_PATTERN = 'sales_{}_{}.json'


if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")


def get_sales(date: dict):
    page = 1
    while True:
        response = get_response(date, page)
        if response.status_code != 200:
            break
        print("Status code", response.status_code)
        save_to_disk(response.json(), date[RAW_DIR_FIELD], FILE_NAME_PATTERN.format(date[DATE_FIELD], page))
        page += 1
    pass


def get_response(date: dict, page: int) -> requests.Response:
    return requests.get(
        url=os.path.join(API_URL, ENDPOINT),
        params={'date': date[DATE_FIELD], 'page': page},
        headers={'Authorization': AUTH_TOKEN}
    )
