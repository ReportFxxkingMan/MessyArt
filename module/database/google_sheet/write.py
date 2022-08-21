from typing import Dict
import pandas as pd
import googleapiclient


def _num_transform(x: pd.Series) -> pd.Series:
    """
    Change str series to numeric series before insert
    Args:
        x (pd.Series)
    Returns:
        pd.Series
    """
    x = x.replace("-", "0", regex=True)
    x = x.replace(",", "", regex=True).astype(int)
    return x


def _data_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    change columns before insert
    Args:
        df (pd.DataFrame)
    Returns:
        df (pd.DataFrame)
    """
    df = df.assign(
        timestamp=df["date"] + " " + df["timestamp"],
        amount=_num_transform(df["amount"]),
        product_discount=_num_transform(df["product_discount"]),
        payment_discount=_num_transform(df["payment_discount"]),
        card_payment=_num_transform(df["card_payment"]),
        cash_payment=_num_transform(df["cash_payment"]),
        easy_payment=_num_transform(df["easy_payment"]),
    )
    return df


def append_sheet(
    sheet: googleapiclient.discovery.Resource,
    SPREADSHEET_ID: str,
    SPREADSHEET_RANGE: str,
    df: pd.DataFrame,
) -> Dict:
    """
    upload data to google spreadsheet
    Args:
        sheet (googleapiclient.discovery.Resource): connected google sheet api
        SPREADSHEET_ID (str): spreadsheet name to look up
        SPREADSHEET_RANGE (str): spreadsheet range to look up
        df (pd.DataFrame): data to upload
    Returns:
        Dict: upload response
    """
    df = _data_transform(df)
    request = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SPREADSHEET_RANGE,
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": df.values.tolist()},
    )
    response = request.execute()
    return response
