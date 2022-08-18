import pandas as pd
from data.column_name import COL_DICT
from module.database.google_sheet import connect_google_sheet
from module.database.variable import (
    SPREADSHEET_ID,
    RANGE,
    )

def check_sheet(sheet, SPREADSHEET_ID, RANGE):
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')

    for row in values:
        print(row)


if __name__ == "__main__":
    df = pd.read_table("data/mock_data.tsv", sep="\s{2,}", engine="python")
    df = df.rename(columns=COL_DICT)

    sheet = connect_google_sheet()
    check_sheet(sheet, SPREADSHEET_ID, RANGE)
