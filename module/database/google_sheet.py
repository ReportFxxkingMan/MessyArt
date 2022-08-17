import os
import logging
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from module.common.exceptions import GoogleCredentialException


def connect_google_sheets():
    try:
        load_dotenv()
    except GoogleCredentialException as e:
        logging.error(e)

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    credential = ServiceAccountCredentials.from_json_keyfile_name(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"], scope
    )
    gc = gspread.authorize(credential)

    return gc
