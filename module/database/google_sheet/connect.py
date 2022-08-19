import os
import logging
import pandas as pd
import googleapiclient
from typing import Dict
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from module.common.exceptions import GoogleCredentialException
from module.database.google_sheet.variables import SPREADSHEET_SCOPES


def connect_google_sheet() -> googleapiclient.discovery.Resource:
    """
    connect and authorize google api sheet

    Returns:
        googleapiclient.discovery.Resource: connected spreadsheet api
    """

    try:
        load_dotenv()
    except GoogleCredentialException as e:
        logging.error(e)

    creds = Credentials.from_authorized_user_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=SPREADSHEET_SCOPES,
    )

    service = build(
        serviceName="sheets",
        version="v4",
        credentials=creds,
    )
    sheet = service.spreadsheets()

    return sheet


def check_sheet(
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
    print("Successful Response")

    values = response.get("values", [])
    df = pd.DataFrame(values[1:], columns=values[0])

    return df


def data_to_sheet(
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
    request = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SPREADSHEET_RANGE,
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": df.values.tolist()},
    )
    response = request.execute()
    print("Successful Response")

    return response["updates"]
