import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from data.column_name import COL_DICT


def connectGoogleSheets():
  scope = [
      "https://spreadsheets.google.com/feeds",
      "https://www.googleapis.com/auth/drive",
  ]

  json_key_path = "./cred/inner-geography-307404-91afac00e32e.json"

  credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
  gc = gspread.authorize(credential)
  
  return gc


df = pd.read_table("data/mock_data.tsv", sep="\s{2,}", engine="python")
df = df.rename(columns=COL_DICT)
