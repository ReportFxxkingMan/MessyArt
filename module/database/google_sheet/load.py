import pandas as pd
import googleapiclient


def load_sheet(
    sheet: googleapiclient.discovery.Resource,
    SPREADSHEET_ID: str,
    SPREADSHEET_RANGE: str,
) -> pd.DataFrame:
    """
    check sheet's value from google spreadsheet api
    Args:
        sheet (googleapiclient.discovery.Resource): connected google sheet api
        SPREADSHEET_ID (str): spreadsheet name to look up
        SPREADSHEET_RANGE (str): spreadsheet range to look up
    Returns:
        pd.DataFrame: dataframe from google sheet
    """
    request = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE)
    response = request.execute()

    values = response.get("values", [])
    df = pd.DataFrame(values[1:], columns=values[0])

    return df
