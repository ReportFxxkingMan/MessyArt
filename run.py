import pandas as pd
from data.column_name import COL_DICT
from module.database.google_sheet.connect import connect_google_sheet
from module.database.google_sheet.load import load_sheet
from module.database.google_sheet.write import append_sheet
from module.database.google_sheet.variables import (
    SPREADSHEET_ID,
    SPREADSHEET_RANGE,
)


if __name__ == "__main__":
    new_df = pd.read_table("data/mock_data.tsv", sep="\s{2,}", engine="python")
    new_df = new_df.rename(columns=COL_DICT)

    sheet = connect_google_sheet()
    df = load_sheet(sheet, SPREADSHEET_ID, SPREADSHEET_RANGE)
    response = append_sheet(sheet, SPREADSHEET_ID, SPREADSHEET_RANGE, new_df)
