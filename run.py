import pandas as pd
import googleapiclient
from module.database.google_sheet.connect import connect_google_sheet
from module.database.google_sheet.variables import (
    SPREADSHEET_ID,
    SPREADSHEET_RANGE,
)
from data.column_name import COL_DICT


def check_sheet(
    sheet: googleapiclient.discovery.Resource,
    SPREADSHEET_ID: str,
    SPREADSHEET_RANGE: str,
) -> None:
    """
    check sheet's value from google spreadsheet api

    Args:
        sheet (googleapiclient.discovery.Resource): connected google sheet api
        SPREADSHEET_ID (str): spreadsheet name to look up
        SPREADSHEET_RANGE (str): spreadsheet range to look up
    """

    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE)
        .execute()
    )
    values = result.get("values", [])
    if not values:
        print("No data found.")

    for row in values:
        print(row)


if __name__ == "__main__":
    df = pd.read_table("data/mock_data.tsv", sep="\s{2,}", engine="python")
    df = df.rename(columns=COL_DICT)

    sheet = connect_google_sheet()
    check_sheet(sheet, SPREADSHEET_ID, SPREADSHEET_RANGE)
