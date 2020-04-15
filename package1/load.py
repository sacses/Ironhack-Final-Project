import os
import pygsheets
import pandas as pd


def load_sheets_token():
    sheets_key = os.getenv('SHEETS_API_TOKEN_PATH')
    sheets_name = os.getenv('WORKBOOK_NAME')
    return sheets_key, sheets_name


def data_dump(data, keys, name):
    client = pygsheets.authorize(service_file=keys)
    print("-----------------Authorized--------------------")
    workbook = client.open(name)
    print("-----------------Sheet Opened------------------")
    sheet = workbook[0]
    print("-----------------First Sheet Accessed----------")
    sheet.clear(fields='*')
    print("-----------------Previous records erased------------------")
    sheet.set_dataframe(data, (1, 1))
    print("-----------------Data Updated------------------")


def complete_load(data):
    keys, name = load_sheets_token()
    return data_dump(data, keys, name)




