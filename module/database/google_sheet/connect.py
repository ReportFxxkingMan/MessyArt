import os
import logging
from dotenv import load_dotenv
import googleapiclient
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

    service = build(serviceName="sheets", version="v4", credentials=creds,)
    sheet = service.spreadsheets()

    return sheet
