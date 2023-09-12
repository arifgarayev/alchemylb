from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

from src.utils.common import Utils


class GoogleSheet:

    scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    def __init__(self, service_account_file_path, sheet_id, worksheet_name):
        self.service_account_file = service_account_file_path
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.service_account_file, GoogleSheet.scopes)
        self.service_sheets = build('sheets', 'v4', credentials=self.credentials)
        self.sheet_id = sheet_id
        self.worksheet_name = worksheet_name
        self.cell_range_insert = 'A4'


    def add_data_new(self, *args, **kwargs):
        value_range_body = {
            'majorDimension': 'ROWS',
            'values': (args,)
        }

        self.service_sheets.spreadsheets().values().append(spreadsheetId=self.sheet_id, valueInputOption='USER_ENTERED',
                                                           range=self.worksheet_name + "!" + self.cell_range_insert,
                                                           body=value_range_body).execute()

