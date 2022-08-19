import os
import logging
import googleapiclient
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from module.common.exceptions import GoogleCredentialException

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

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = Credentials.from_authorized_user_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"], SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    
    return sheet
