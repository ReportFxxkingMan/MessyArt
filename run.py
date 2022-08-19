#%%
import pandas as pd
from data.column_name import COL_DICT
from module.database.google_sheet import (
    connect_google_sheet,
    check_sheet,
    data_to_sheet,
)
from module.database.variable import (
    SPREADSHEET_ID,
    SPREADSHEET_RANGE,
)

#%%
if __name__ == "__main__":
    new_df = pd.read_table("data/mock_data.tsv", sep="\s{2,}", engine="python")
    new_df = new_df.rename(columns=COL_DICT)

    sheet = connect_google_sheet()
    df = check_sheet(sheet, SPREADSHEET_ID, SPREADSHEET_RANGE)
    response = data_to_sheet(sheet, SPREADSHEET_ID, SPREADSHEET_RANGE, new_df)

# %%
