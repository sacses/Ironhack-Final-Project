import os
import pygsheets
import pandas as pd
from dotenv import load_dotenv


def load_sheets_token():
    load_dotenv()
    sheets_key = os.getenv('SHEETS_API_TOKEN_PATH')
    sheets_name = os.getenv('WORKBOOK_NAME')
    return sheets_key, sheets_name


def data_dump(data, keys, name):
    client = pygsheets.authorize(service_file=keys)
    workbook = client.open(name)
    sheet = workbook[0]
    sheet.clear(fields='*')
    sheet.set_dataframe(data, (1,1))


def complete_load(data):
    keys, name = load_sheets_token()
    return data_dump(data, keys, name)




